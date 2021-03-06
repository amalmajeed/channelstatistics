import requests
import json


class YTstats:

	def __init__(self,api_key,channel_id):
		self.api_key = api_key
		self.channel_id = channel_id
		self.channel_statistics = None
		self.channel_title = ''
		self.video_data = None

	def get_channel_statistics(self):
		url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&id={self.channel_id}&key={self.api_key}'
		#print(url)
		json_url = requests.get(url)
		#print("The response is :",json_url,"\n")
		# Getting the actual text of the website
		data = json.loads(json_url.text)
		self.channel_title = data["items"][0]["snippet"]["title"]
		#print("The data is : ",data,"\n")
		try:
			data = data["items"][0]['statistics']
		except:
			data = None
		self.channel_statistics = data
		return data

	def get_channel_video_data(self):
		# 1)get the video ids
		channel_videos = self._get_channel_videos(limit=50)

		# 2)get the video statistics - to do

	def _get_channel_videos(self,limit = None):
		url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date"
		if limit is not None and isinstance(limit, int):
			url+= "&maxResults="+str(limit)
		print(url)

	def _get_channel_videos_per_page(self,url):
		json_url = requests.get(url)
		data = json.loads(json_url.text)
		channel_videos = dict()
		#checking for items key
		if 'items' not in data:
			return channel_videos,None
		item_data = data['items']
		#return value for key nextPageToken else instead of KeyError return None
		nextPageToken = data.get("nextPageToken",None)
		# iterating over items to find videos
		for item in item_data:
			try:
				kind = item['id']['kind']
				if kind == "youtube#video":
					video_id = item['id']['videoId']
					# create an entry for the video to later fill with statistics about the video
					channel_videos[video_id] = {}
			except KeyError:
				print("Key Error encountered !")
		return channel_videos,nextPageToken


	def dump(self):
		if self.channel_statistics is None:
			return

		channel_title = self.channel_title 
		channel_title = channel_title.replace(" ","_").lower()
		file_name = channel_title + ".json"
		with open(file_name,"w") as f:
			json.dump(self.channel_statistics,f,indent = 4)
		print("file dumped !\n")
		f.close()

