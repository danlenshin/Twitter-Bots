from twython import Twython
import json
import random

#Loads keys from keys.json
keys = json.loads(open('keys.json').read())

#Account verification and Twython object initialization
apikey = keys[0]
apikeysecret = keys[1]
accesstoken = keys[2]
accesstokensecret = keys[3]
twython = Twython(apikey, apikeysecret, accesstoken, accesstokensecret)

lines = 1812 #Amount of lines in the script (update as needed)
line = random.randint(1, lines) #Random line
script = open('script.txt', 'r') #Opens script file as read

for i in range(line):
    scriptline = script.readline()

scriptline.strip() #Strip leading and trailing whitespace

response = twython.update_status(status=scriptline) #Tweet line