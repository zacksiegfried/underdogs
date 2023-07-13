# underdogs
## Scripts relating to the general analysis of professional sports
basic draftkings odds web scraping capabilities are contained in dkTools.py <br>
urlBuilder.py allows easy changing of selected sport, also contains minimal selection criteria (can be added to)

## cfb
College football analysis
### Example DK odds pull
Basic package imports
```
import requests
from bs4 import BeautifulSoup

import sys
import os
```
Changing path to underdogs directory and importing relevant scripts
```
sys.path.insert(0, os.path.dirname(os.path.abspath('')))

import urlBuilder
import dkTools
```
urlBuilder is used to create specific draft kings CFB url which can then be fed into requests
BeautifulSoup used to convert requests object to bs4 object
bs4 object 'soup' is passed to gameSelector() which returns a list of games with team names and odds
```
page = requests.get(urlBuilder.DKbuild('football/ncaaf', '?category=game-lines&subcategory=game'))
soup = BeautifulSoup(page.content, 'html5lib')

games = dkTools.gameSelector(soup):
```
Example output
```
for i in games:
  print(i)

[{'name': 'Navy', 'moneyline': '+800'}, {'name': 'Notre Dame', 'moneyline': '−1250'}]
[{'name': 'UTEP', 'moneyline': '+110'}, {'name': 'Jacksonville State', 'moneyline': '−130'}]
[{'name': 'Ohio', 'moneyline': '+155'}, {'name': 'San Diego State', 'moneyline': '−180'}]
```
