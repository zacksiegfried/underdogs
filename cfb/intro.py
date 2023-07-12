import requests
from bs4 import BeautifulSoup

import sys
import os
sys.path.insert(0, (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from urlBuilder import DKbuild

# importing html data
page = requests.get(DKbuild('football/ncaaf', '?category=game-lines&subcategory=game'))
soup = BeautifulSoup(page.content, 'html5lib')


# zipping function iterates through list 2 items at a time
def pairwise(list_data):
    return list(zip(*[iter(list_data)] * 2))


### Returns a list of lists with elements containing match up information. This is in the form of a dictionary with team:
# {'name': , 'moneyline: '}         # could extract more info

def gameSelector():
    """Under Construction -- fails if there is a missing odds value"""

    page = soup.find('div', class_ = 'sportsbook-offer-category-card')
    info_list = page.find_all('tbody', class_ = 'sportsbook-table__body')

    teams_list_raw = []
    for event in info_list:
        temp = event.find_all('tr')
        teams_list_raw.append(temp)
    teams_list = [item for sublist in teams_list_raw for item in sublist]

    # building list of indivdual game team names and odds
    games_list = []
    for i, j in pairwise(teams_list):

        game_data = []
        team1_data = {}
        team2_data = {}

        team1_data['name'] = i.find('div', class_ = 'event-cell__name-text').text
        team2_data['name'] = j.find('div', class_ = 'event-cell__name-text').text

        team1_data['moneyline'] = i.find('span', class_ = 'sportsbook-odds american no-margin default-color').text
        team2_data['moneyline'] = j.find('span', class_ = 'sportsbook-odds american no-margin default-color').text

        game_data.append(team1_data)
        game_data.append(team2_data)

        games_list.append(game_data)
        

    return(games_list)
    


if __name__ == "__main__":
    gameSelector()