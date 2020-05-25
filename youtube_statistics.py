import requests
import json


class YTstats:

	def __init__(self,api_key,channel_id):
		self.api_key = api_key
		self.channel_id = channel_id
		self.channel_statistics = None
		self.channel_title = ''

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

	def dump(self):
		if self.channel_statistics is None:
			return

		channel_title = self.channel_title 
		channel_title = channel_title.replace(" ","_").lower()
		file_name = channel_title + ".json"
		with open(file_name,"w") as f:
			json.dump(self.channel_statistics,f,indent = 4)
		print("file dumped !\n")

