import os
os.remove('Blacklist.json')

blacklistFile = open('Blacklist.json', 'w')
blacklistFile.write('[999999]')
blacklistFile.close()
