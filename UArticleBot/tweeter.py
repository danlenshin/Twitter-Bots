from twython import Twython
import json
import random

#Checks an extension with the blacklist array
def isBlacklisted(extension):
    for element in blacklist:
        if extension == element:
            return True
    
    return False

#Account verificaton
keys = json.loads(open('keys.json').read())
API_key = keys[0]
API_secret_key = keys[1]
Access_token = keys[2]
Access_token_secret = keys[3]
UArticlesBot = Twython(API_key, API_secret_key, Access_token, Access_token_secret)

articles = json.loads(open('UAList.json').read()) #Import array from json file
blacklist = json.loads(open('Blacklist.json').read()) #Import blacklist array
randomArticle = random.randrange(0, (len(articles)/2), 2) #Select random extension from array

#Get article extension and title using random article number
articleExtension = articles[randomArticle]
articleTitle = articles[randomArticle + 1]

#Checks articleExtension with blacklist array, and chooses another element if extension is blacklisted
while isBlacklisted(articleExtension):
    #Redefine article extension and title
    randomArticle = random.randrange(0, (len(articles)/2), 2)
    articleExtension = articles[randomArticle]
    articleTitle = articles[randomArticle + 1]

#Send tweet
UArticlesBot.update_status(status = 'Today\'s article is: %s\nen.wikipedia.org/wiki/%s' %(articleTitle, articleExtension))
