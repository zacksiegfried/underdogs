

### Possible League strings

# NFL = football/nfl
# CFB = football/ncaaf


### Possible bet category type

# Game Lines = ?category=game-lines&subcategory=game

def DKbuild(league, bet_type):
    """Returns full draftkings URL from input of relavent league string and bet category type"""

    base_url = 'https://sportsbook.draftkings.com/leagues/'
    url = base_url + str(league) + str(bet_type)

    return(url)