from twython import Twython
import json
import datetime
import time

#Loads keys into array from keys.json
keys = json.loads(open('keys.json').read())

#Account verification and Twython object initializer
API_key = keys[0]
API_secret_key = keys[1]
Access_token = keys[2]
Access_token_secret = keys[3]
TCBot = Twython(API_key, API_secret_key, Access_token, Access_token_secret)

#Gets current date and time information
now = datetime.datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))

#Checks times
if hour == 3 and minute == 28:
    video = open('328AM.mp4', 'rb')
    response = TCBot.upload_video(media=video, media_type='video/mp4')
    TCBot.update_status(status='', media_ids=[response['media_id']])
elif hour == 7 and minute == 59:
    video = open('759AM.mp4', 'rb')
    response = TCBot.upload_video(media=video, media_type='video/mp4')
    TCBot.update_status(status='', media_ids=[response['media_id']])
elif hour == 0 and minute == 0:
    video = open('1200AM.mp4', 'rb')
    response = TCBot.upload_video(media=video, media_type='video/mp4')
    TCBot.update_status(status='', media_ids=[response['media_id']])
elif hour == 20 and minute == 1:
    video = open('801PM.mp4', 'rb')
    response = TCBot.upload_video(media=video, media_type='video/mp4')
    TCBot.update_status(status='', media_ids=[response['media_id']])
