import requests
from bs4 import BeautifulSoup
from models.driver_model import *


"""
    1. Open the playersName.txt
    2. Use player career link and iterate over every player 
    2. Scrape the stats 
    3. Places the player information and stats into the position dictionary
    4. Uses as the params for the request for the API
"""

# Dictionary with all of the positions
OLINE = {"C",'OG','OT','LS','K','P'} # Offensive Line will not be added

# The positions that share the same type of stats
DEFENSE = ['Defensive End', 'Defensive Tackle', 'Linebacker', 'Cornerback','Safety']
RECEIVERS = ['Wide Receiver', 'Tight End']


QB_MAX = 13
RB_MAX = 9
WR_MAX = 10
DEFENSE_MAX = 15


# Opens the player file to get the name of the player 
player_file = open('players.txt', 'r')

for player in player_file:

    player = player.split("-")
    player_name = player[0].strip()
    player_id = player[1].strip()

    print(player_name)

    # Checking in for punctuation in the name to format 
    if player_name.find(".") != -1:
        player_name = player_name.replace('.', "")
    if player_name.find("'") != -1:
        player_name = player_name.replace("'", "")

    # Formats it
    player_name = player_name.replace(" ", "-")
        
    # Will enter the name into the f string with the player name found in the file
    player_link = f'https://www.espn.com/nfl/player/stats/_/id/{player_id}/{player_name}'  

    # Make a request and get the html of that page
    player_html = requests.get(player_link).text
    soup = BeautifulSoup(player_html, 'html.parser')

    # data that we are extracting
    player_details = []
    years = []
    stats = []

    try:
        # player data
        personal_details_container = soup.find(class_='PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap')
        details = personal_details_container.find_all('li')
        player_details.append(player_name.replace('-', ' '))
        for li in details:
            player_details.append(li.text)
        
        if player_details[2] in OLINE:
            continue
        else:
            # year and stats data
            stats_container = soup.find(class_='ResponsiveTable ResponsiveTable--fixed-left pt4')  
            years_table= stats_container.find_all(class_='Table__TBODY')[0]
            for row in years_table:
                years.append(row.text[0:4])

            stats_table = stats_container.find_all(class_='Table__TD') 
            # removing unnecessary info
            for i in range(len(years)*2):
                stats_table.pop(0)
            
            years.pop(len(years)-1)
            for row in stats_table:
                stats.append(row.text)

            blanks = stats.count('-')
            for i in range(blanks):
                idx = stats.index('-')
                stats[idx] = '0'

            player = None
            data = None  
            pos = player_details[3]
            for i in range(len(years)):
                if i < 1:
                    if pos == 'Quarterback':
                        player = QB(player_details[0],player_details[1],player_details[2],player_details[3],years[i],stats)
                        data = player.formatData()
                        for i in range(QB_MAX):
                            stats.pop(0)
                    
                    if pos == 'Running Back':
                        player = RB(player_details[0],player_details[1],player_details[2],player_details[3],years[i],stats)
                        data = player.formatData()
                        for i in range(RB_MAX):
                            stats.pop(0)
                    
                    if pos in RECEIVERS:
                        player = WR(player_details[0],player_details[1],player_details[2],player_details[3],years[i],stats)
                        data = player.formatData()
                        for i in range(WR_MAX):
                            stats.pop(0)
                    
                    if pos in DEFENSE:
                        player = Defense(player_details[0],player_details[1],player_details[2],player_details[3],years[i],stats)
                        data = player.formatData()
                        for i in range(DEFENSE_MAX):
                            stats.pop(0)
                        
                else:
                    if pos == 'Quarterback':
                        player.setStats(years[i], stats)
                        for i in range(QB_MAX):
                            stats.pop(0)
                        data = player.formatData()
                    
                    if pos == 'Running Back':
                        player.setStats(years[i], stats)
                        for i in range(RB_MAX):
                            stats.pop(0)
                        data = player.formatData()
                    
                    if pos in RECEIVERS:
                        player.setStats(years[i], stats)
                        for i in range(WR_MAX):
                            stats.pop(0)
                        data = player.formatData()
                        
                    if pos in DEFENSE:
                        stats.pop(0)
                        stats.pop(0)
                        player.setStats(years[i], stats)
                        for i in range(DEFENSE_MAX):
                            stats.pop(0)
                        data = player.formatData()
                r = requests.put(f"http://127.0.0.1:5000/NFL/{player_name}",data=data)
                print(r.json())
               
    except:
        print(player_name + ' not added')
    print()


        

                 
playerFile.close()