import json

class QB:
    def __init__(self,name,team,number,position,year,stats):
        self.name = name
        self.team = team
        self.position = position
        self.number = number
        self.year = year
        self.games = stats[0]
        self.completions = stats[1]
        self.attempts = stats[2]
        self.completionPercentage = stats[3]
        self.yards = stats[4]
        self.avgYards = stats[5]
        self.tds = stats[6]
        self.ints = stats[7]
        self.longestPass = stats[8]
        self.sacks = stats[9]
        self.fumbles = stats[10]
        self.passerRating = stats[11]
        self.qbr = stats[12]
        self.player_dict = {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            'number' : self.number,
        }

    def formatData(self):
        self.player_dict['year'] = self.year
        self.player_dict['GP'] = self.games
        self.player_dict['CMP'] = self.completions
        self.player_dict['ATT']= self.attempts
        self.player_dict['CMP%']= self.completionPercentage 
        self.player_dict['YDS'] =self.yards 
        self.player_dict['AVG'] = self.avgYards 
        self.player_dict['TDS'] = self.tds 
        self.player_dict['INT'] = self.ints 
        self.player_dict['LNG'] = self.longestPass 
        self.player_dict['SACK']= self.sacks 
        self.player_dict['FUM'] = self.fumbles
        self.player_dict['RTG'] = self.passerRating
        self.player_dict['QBR'] = self.qbr   
        return self.player_dict

    def setStats(self,year, stats):
        self.year = year
        self.games = stats[0]
        self.completions = stats[1]
        self.attempts = stats[2]
        self.completionPercentage = stats[3]
        self.yards = stats[4]
        self.avgYards = stats[5]
        self.tds = stats[6]
        self.ints = stats[7]
        self.longestPass = stats[8]
        self.sacks = stats[9]
        self.fumbles = stats[10]
        self.passerRating = stats[11]
        self.qbr = stats[12]
        

class RB:
    def __init__(self,name,team,number,position,year,stats):
        self.name = name
        self.team = team
        self.position = position
        self.number = number
        self.year = year
        self.games = stats[0]
        self.attempts = stats[1]
        self.yards = stats[2]
        self.avgYards = stats[3]
        self.tds = stats[4]
        self.longestRun = stats[5]
        self.rushing1stDowns = stats[6]
        self.fumbles=stats[7]
        self.rushingFumbleLost = stats[8]
        self.player_dict = {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            'number' : self.number
        }
    def formatData(self):
        self.player_dict['year']= self.year
        self.player_dict['GP']= self.games     
        self.player_dict['ATT']= self.attempts
        self.player_dict['YDS'] = self.yards
        self.player_dict['AVG'] = self.avgYards
        self.player_dict['TDS'] = self.tds 
        self.player_dict['LNG'] = self.longestRun
        self.player_dict['FD']= self.rushing1stDowns
        self.player_dict['FUM'] = self.fumbles
        self.player_dict['LST'] = self.rushingFumbleLost
        return self.player_dict

    def setStats(self,year,stats):
        self.year = year
        self.games = stats[0]
        self.attempts = stats[1]
        self.yards = stats[2]
        self.avgYards = stats[3]
        self.tds = stats[4]
        self.longestRun = stats[5]
        self.rushing1stDowns = stats[6]
        self.fumbles=stats[7]
        self.rushingFumbleLost = stats[8]


class WR:
    def __init__(self,name,team,number,position,year,stats):
        self.name = name
        self.team = team
        self.position = position
        self.number = number
        self.year = year
        self.games = stats[0]
        self.receptions = stats[1]
        self.targets = stats[2]
        self.yards = stats[3]
        self.avgYards = stats[4]
        self.tds = stats[5]
        self.longestRec = stats[6]
        self.receivingFirstDowns = stats[7]
        self.fumbles=stats[8]
        self.rushingFumbleLost = stats[9]
        self.player_dict = {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            'number' : self.number,
        }
        
    def formatData(self):
        self.player_dict['year'] = self.year
        self.player_dict['GP']= self.games    
        self.player_dict['REC']=self.receptions
        self.player_dict['TGTS']=self.targets
        self.player_dict['YDS'] =self.yards
        self.player_dict['AVG'] = self.avgYards
        self.player_dict['TDS'] = self.tds 
        self.player_dict['LNG'] = self.longestRec
        self.player_dict['FD'] = self.receivingFirstDowns
        self.player_dict['FUM'] = self.fumbles
        self.player_dict['LST'] = self.rushingFumbleLost
        return self.player_dict

    def setStats(self,year, stats):
        self.year = year
        self.games = stats[0]
        self.receptions = stats[1]
        self.targets = stats[2]
        self.yards = stats[3]
        self.avgYards = stats[4]
        self.tds = stats[5]
        self.longestRec = stats[6]
        self.receivingFirstDowns = stats[7]
        self.fumbles=stats[8]
        self.rushingFumbleLost = stats[9]

class Defense:
    def __init__(self,name,team,number,position,year,stats):
        self.name = name
        self.team = team
        self.position = position
        self.number = number
        self.year = year
        self.games = stats[0]
        self.totalTackles = stats[1]
        self.soloTackles = stats[2]
        self.assistedTackles = stats[3]
        self.sacks = stats[4]
        self.forcedFumbles = stats[5]
        self.fumblesRecovered = stats[6]
        self.fumbleYards = stats[7]
        self.interceptions = stats[8]
        self.intYards = stats[9]
        self.avgYardsIntercepted = stats[10]
        self.tds = stats[11]
        self.longestInterception =stats[12]
        self.passesDefended  = stats[13]
        self.stuffs = stats[14]
        self.player_dict = {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            'number' : self.number,
        }

    def formatData(self):
        self.player_dict['year']= self.year
        self.player_dict['GP']= self.games     
        self.player_dict['TOT']=self.totalTackles
        self.player_dict['SOLO']=self.soloTackles
        self.player_dict['AST']= self.assistedTackles 
        self.player_dict['SACK'] =self.sacks 
        self.player_dict['FF'] = self.forcedFumbles 
        self.player_dict['FR'] = self.fumblesRecovered     
        self.player_dict['YDS'] = self.fumbleYards 
        self.player_dict['INT']= self.interceptions
        self.player_dict['INT YARDS']= self.intYards
        self.player_dict['AVG']= self.avgYardsIntercepted
        self.player_dict['TDS']= self.tds
        self.player_dict['LNG'] = self.longestInterception
        self.player_dict['PD'] = self.passesDefended
        self.player_dict['STF'] =self.stuffs
        return self.player_dict

    def setStats(self,year, stats):
        self.year = year
        self.games = stats[0]
        self.totalTackles = stats[1]
        self.soloTackles = stats[2]
        self.assistedTackles = stats[3]
        self.sacks = stats[4]
        self.forcedFumbles = stats[5]
        self.fumblesRecovered = stats[6]
        self.fumbleYards = stats[7]
        self.interceptions = stats[8]
        self.intYards = stats[9]
        self.avgYardsIntercepted = stats[10]
        self.tds = stats[11]
        self.longestInterception =stats[12]
        self.passesDefended  = stats[13]
        self.stuffs = stats[14]

