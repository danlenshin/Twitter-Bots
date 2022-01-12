import urllib.request, urllib.error, urllib.parse
import random
import json
import os
from bs4 import BeautifulSoup
import time
from twython import Twython
import shutil
import requests
import sys

#Function to check if the site has an image link according to the img_link_regex
def siteHasImage(soup):
    if soup.find("div", {"id": "art-object-carousel"}).find("img"):
        if soup.find("div", {"id": "art-object-carousel"}).find("img")["src"] != "/content/dam/ngaweb/placeholders/placeholder-lg.svg": #Checks if the image url is not the "no image" placeholder
            return True
        else:
            return False
    else:
        return False

#Function to add a certain linkID to a list of pages without images
def addToBlacklist(number):
    blacklisted_linkIDs = json.loads(open('Blacklist.json').read())
    blacklisted_linkIDs.append(number)
    json.dump(blacklisted_linkIDs, open('Blacklist.json', 'w'))

#Checks a number with the blacklist
def isBlacklisted(number):

    #Checks if Blacklist.json is empty to prevent loading errors
    if os.stat("Blacklist.json").st_size == 0:
        return False

    blacklisted_linkIDs = json.loads(open('Blacklist.json').read())
    for element in blacklisted_linkIDs:
        if number == element:
            return True
    return False

extracted = [] #Array which contains extracted information from webpage
exitImgFindLoop = False #Boolean to track if the program should stop searching
findValidLink = True #Boolean which keeps track of whether or not to stop searching for a valid URL

#Twitter account authentification
keys = json.loads(open('keys.json').read())
API_key = keys[0]
API_secret_key = keys[1]
Access_token = keys[2]
Access_token_secret = keys[3]
ArtEveryHour = Twython(API_key, API_secret_key, Access_token, Access_token_secret)

attempts = 0 #Keeps track of the amount of times the bot has attempted to find an image

while not exitImgFindLoop:
    #Build link and catch 404 errors
    findValidLink = True
    linkID = random.randint(0, 100000)
    while isBlacklisted(linkID):
        linkID = random.randint(0, 100000)

    while findValidLink:
        link = 'https://www.nga.gov/collection/art-object-page.%d.html' %(linkID)
        try:
            raw = urllib.request.urlopen(link).read()
            findValidLink = False
        except:
            addToBlacklist(linkID)
            linkID = random.randint(0, 100000)
            while isBlacklisted(linkID):
                linkID = random.randint(0, 100000)

    soupLink = BeautifulSoup(raw, "lxml")

    if siteHasImage(soupLink):
        title = soupLink.find("meta", property="og:title")
        artist = soupLink.find("meta", property="og:description")
        img_link = soupLink.find("div", {"id": "art-object-carousel"}).find("img")
        extracted.append(title["content"])
        extracted.append(artist["content"])
        extracted.append(img_link["src"])
        exitImgFindLoop = True
    else:
        addToBlacklist(linkID)
        linkID = random.randint(0, 100000)
        while isBlacklisted(linkID):
            linkID = random.randint(0, 100000)

    time.sleep(2) #To prevent NGA servers from thinking something is up
    attempts += 1

    #To prevent perpetual looping
    if attempts > 500: 
        sys.exit(0)

#Download image to be sent
image_stream = requests.get(extracted[2], stream=True)
with  open('localImage.jpg', 'wb') as image:
    for chunk in image_stream:
        image.write(chunk)

#Send Tweet
artPhoto = open('localImage.jpg', 'rb')
response = ArtEveryHour.upload_media(media=artPhoto)
ArtEveryHour.update_status(status='%s, %s.\n%s'%(extracted[1], extracted[0], link), media_ids=[response['media_id']])
