import requests
from bs4 import BeautifulSoup


"""
    1. Use Team Link and iterate over every team 
    2. Scrape the names of players and Store them in a text file
    3. Use the names to loop over the stats
"""

teams = {
    'ari': "arizona-cardinals", 
    'atl': 'atlanta-falcons',
    'bal': 'baltimore-ravens',
    'buf': 'buffalo-bills',
    'car': 'carolina-panthers',
    'chi': 'chicago-bears',
    'cin': 'cincinnati-bengals',
    'cle': 'cleveland-browns',
    'dal': 'dallas-cowboys',
    'den': 'denver-broncos',
    'det': 'detriot-lions',
    'hou': 'houston-texans', 
    'gb': 'green-bay-packers',
    'ind': 'indianapolis-colts',
    'lar': 'los-angeles-rams', 
    'jax': 'jacksonville-jaguars', 
    'min': 'minnesota-vikings',
    'kc': 'kansas-city-chiefs',
    'no': 'new-orleans-saints',
    'lv': 'las-vegas-raiders',
    'nyg':'new-york-giants',
    'lac': 'los-angeles-chargers',
    'phi': 'philadelphia-eagles',
    'mia': 'miami-dolphins',
    'sf': 'san-francisco-49ers',
    'ne': 'new-england-patriots',
    'sea': 'seattle-seahawks',
    'nyj': 'new-york-jets', 
    'tb': 'tampa-bay-buccaneers', 
    'pit': 'pittsburgh-steelers',
    'wsh': 'washington-football-team',
    'ten': 'tennessee-titans' 
}

teams_abr = list(teams.keys())

# Puts all of the players into a textfile
file = open('players.txt', 'a')
for i in teams_abr:
    #  source link for the teams roster
    source = f'https://www.espn.com/nfl/team/roster/_/name/{i}' 

    # gets the html of the website
    roster = requests.get(source).text

    # creates a beautiful soup object to parse
    soup = BeautifulSoup(roster,'html.parser')

    
    # get the players table from the html class
    player_table = soup.find_all(class_="Table__TR Table__TR--lg Table__even")
    for i in player_table:
        player = i.find_all("a")
        for j in player:
            try:
                if j.text:
                    espn_id = j.attrs['href'].replace("http://www.espn.com/nfl/player/_/id/","").split("/")[0]
                    file.write(f"{j.text} - {espn_id}\n")
            except:
                continue
file.close()
