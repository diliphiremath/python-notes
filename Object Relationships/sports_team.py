class Player:
    def __init__(self,id,teamName,name):
        self.id = id
        self.teamName = teamName
        self.name = name

class Team:
    def __init__(self,name):
        self.players = []
        self.name = name
    
    def addPlayers(self,player):
        self.players.append(player)

    def getNumberOfPlayers(self):
        return len(self.players) 

class School:
    def __init__(self,name):
        self.teams = []
        self.name = name

    def addTeam(self,team):
        self.teams.append(team)

    def getTotalPlayersInSchool(self):
        total_players = 0
        for i in self.teams:
            total_players += i.getNumberOfPlayers()
        return total_players

school = School('Pillay')
team1 = Team('Red')
team2 = Team('Blue')
team1.addPlayers(Player(1,'Red','Harris'))
team1.addPlayers(Player(2,'Red','Carol'))
team2.addPlayers(Player(1,'Blue','Jhonny'))
team2.addPlayers(Player(2,'Blue','Sarra'))
school.addTeam(team1)
school.addTeam(team2)
print(school.getTotalPlayersInSchool())

