from twython import Twython
import json
import random
import datetime
import os

#Loads keys from keys.json
keys = json.loads(open('keys.json').read())

#Account verification and Twython object initialization
apikey = keys[0]
apikeysecret = keys[1]
accesstoken = keys[2]
accesstokensecret = keys[3]
twython = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

#Loads data from data.json
data = json.loads(open('data.json').read())

lines = 15 #Amount of lines in the song (update as needed)
line = data['am_line'] #Gets which line to tweet from data.json
link = data['fs_link'] #Gets link to fight song from data.json
song = open('song.txt', 'r') #Opens song file as read
now = datetime.datetime.now() #Gets today's date and time
hour = int(now.strftime("%H")) #Gets current hour

#Return corresponding line of alma mater and strip whitespace
for i in range(line):
    songline = song.readline()
songline = songline.strip()

#Checks if it is 9am on a saturday
if now.weekday() == 5 and hour == 9:
    #response = twython.update_status(status=link) #Tweet link to fight song
    print("Tweeted fight song")
else:
    #response = twython.update_status(status=songline)
    print("Tweeted:", songline)

#Updates data.json with next line
if line == 15:
    line = 1
else:
    line = line + 1

data['am_line'] = line
datafile = open('data.json', 'w')
datafile.write(json.dumps(data))
datafile.close()