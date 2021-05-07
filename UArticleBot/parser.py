import re
import json

#regex to extract a string containing the link extension and title from unusual articles page
regex_1 = re.compile('(?<=<td><b><a href="/wiki/)(.*)(?=</a>)')
regex_2 = re.compile('(?<=<td width="30%"><b><a href="/wiki/)(.*)(?=</a>)')

with open('Wikipedia:Unusual_articles', 'r') as raw:
    raw = raw.read() #Extract text data from HTML

    extracted = [] #Array of extracted (not processed) data from tables

    #Adds elements extracted from HTML by regex to array
    reg1 = re.findall(regex_1, raw)
    reg2 = re.findall(regex_2, raw)
    extracted = reg1 + reg2

processed = [] #Array of processed and separated names and titles from 

#For loop to add elements from extracted[] to processed[]
for element in extracted:
    #Find extension from extracted element (0 to first '"' character) and insert into processed[]
    extension_substr = element[0:element.find('"')]
    processed.append(extension_substr)

    #Find title from extracted element (first '>' character to end of string) and insert it into processed[]
    title_substr = element[element.find('>')+1:len(element)]
    processed.append(title_substr)

#Code to write processed[] array to a JSON file
with open('UAList.json', 'w') as jsonFile:
    json.dump(processed, jsonFile)
