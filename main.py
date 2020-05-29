# Reading API KEY
file = open("apikey.txt","r")
API_KEY = file.read()[:-1]
file.close()

# channel id - PowerfulJRE
channel_id = "UCzQUP1qoWDoEbmsQxvdjxgQ"

from youtube_statistics import YTstats



yt = YTstats(API_KEY,channel_id)


#data = yt.get_channel_statistics()
#yt.dump()

yt.get_channel_video_data()