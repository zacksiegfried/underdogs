

# function to group teams into their respective games
def pairwise(list_data):
    return list(zip(*[iter(list_data)] * 2))


### Returns a list of lists with elements containing match up information. This is in the form of a dictionary with team:
# {'name': , 'moneyline: '}
def gameSelector(soup):

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


        # extracting data for information that is always present (team name, )
        team1_data['name'] = i.find('div', class_ = 'event-cell__name-text').text
        team2_data['name'] = j.find('div', class_ = 'event-cell__name-text').text

        # extracting data for information that can be missing (odds, )
        team1_data['moneyline'] = i.find('span', class_ = 'sportsbook-odds american no-margin default-color')   
        team2_data['moneyline'] = j.find('span', class_ = 'sportsbook-odds american no-margin default-color')


        game_data.append(team1_data)
        game_data.append(team2_data)

        # extracting raw numerical value from bs4 object
        for team in game_data:
            if team['moneyline'] != None:
                team['moneyline'] = team['moneyline'].text


        games_list.append(game_data)


    return(games_list)