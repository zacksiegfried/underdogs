# underdogs
## Scripts relating to the betting analysis of college and professional sports
basic draftkings web scraping capabilities are contained in dkTools.py <br>
urlBuilder.py allows easy changing of selected sport, also contains minimal selection criteria (can be added to)

## cfb
College football analysis
### Example DraftKings odds pull
Basic package imports + changing path to underdogs directory to import relevant scripts
```
import requests
from bs4 import BeautifulSoup

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath('')))

import urlBuilder
import dkTools
```
urlBuilder is used to create specific draft kings CFB url which can then be fed into requests <br>
bs4 object 'soup' is passed to gameSelector() which returns a list of lists containing dictionaries with team names and odds
```
page = requests.get(urlBuilder.DK('football/ncaaf', '?category=game-lines&subcategory=game'))
soup = BeautifulSoup(page.content, 'html5lib')

games_list = dkTools.gameSelector(soup):
```
_**gameSelector() can only be applied to game-lines tab on DK webpage selected by '?category=game-lines&subcategory=game' as the 2nd variable passed to urlBuilder**_ <br>
<br>
Example output
```
for i in games_list:
  print(i)

[{'name': 'Navy', 'moneyline': '+800'}, {'name': 'Notre Dame', 'moneyline': '−1250'}]
[{'name': 'UTEP', 'moneyline': '+110'}, {'name': 'Jacksonville State', 'moneyline': '−130'}]
[{'name': 'Ohio', 'moneyline': '+155'}, {'name': 'San Diego State', 'moneyline': '−180'}]
...
```
