# Unusual Articles Twitter Bot

A Twitter bot which tweets a random article from Wikipedia's [List of Unusal Articles](https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles). Currently running on @UArticleBot which tweets once per day at 12:00 PM.

Needs two additional files in order to function:
* Blacklist.json - An array of URL paths which the bot will never tweet (Example element: "Koro_(medicine)"). Included in order to avoid the bot tweeting objectionable content. Needed for `tweeter.py` to function.
* UAList.json - Created by `parser.py` whenever it is run. Contains the titles and URL paths of all pages in the list of unusual articles. Needed for `tweeter.py` to function.