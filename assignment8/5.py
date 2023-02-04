import random

players = ['Ali', 'Mohammad', 'Beni', 'Saeed', 'Sami', 'Mehran', 'Arsalan', 'Sina', 'Arsha',
           'Mohsen', 'Navid', 'Arash', 'Sobhan', 'Nima', 'Khashayad', 'Mehdi', 'Kian', 'Parsa',
           'Shahab', 'Sohrab', 'Matin', 'Samyar']


class Person:

    def __init__(self, name, team):
        self.name = name
        self.team = team


class SoccerPlayer(Person):
    pass


random.shuffle(players)

for i in range(len(players)):
    if(i < 11):
        players[i] = SoccerPlayer(players[i], 'A')
    else:
        players[i] = SoccerPlayer(players[i], 'B')

for player in players:
    print('name : ', player.name, '      team : ', player.team)
