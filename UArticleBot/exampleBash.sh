#! /bin/bash

cd /path/to/UArticleBot
wget -q  en.wikipedia.org/wiki/Wikipedia:Unusual_articles -O Wikipedia:Unusual_articles
python3 parser.py
python3 tweeter.py
