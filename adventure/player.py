import world

class player1:
    def __init__(self, name):
        self.name = name
        self.actions = ['Look', 'Move']
        self.place = 'a'
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def move(self, direction):
        if direction == 'right':
            places = getPlace('name')
            if player1.place == places[-1]:
                world.generatePlace()
            player1.place = chr(ord(player1.place) + 1)
        elif direction == 'left':
            places = getPlace('name')
            if player1.place != places[0]:
                # world.generatePlace()
                player1.place = chr(ord(player1.place) - 1)

    def look(self):
        print('You are in place ' + str(player1.place))
        print('The place right of you is ' + (chr(ord(player1.place) + 1)))
        print('The place left of you is ' + (chr(ord(player1.place) - 1)))
        player1.add_data(getPlace('enviroment'))
        player1.add_data(getPlace('weather'))
        player1.add_data(getPlace('object'))
        print(str(player1.data[0]).replace(",","")+" "+str(player1.data[1]).replace(",","")+" "+str(player1.data[2]))

def getPlace(attribute):
    files = open('places.txt', 'r')
    file = files.readlines()
    attributes = []
    for line in file:
        if attribute == 'name' and line[0] == player1.place:
            lines = line.split()[0]
            attributes.append(lines)
        elif attribute == 'enviroment' and line[0] == player1.place:
            lines = line.split()[1]
            attributes.append(lines)
        elif attribute == 'weather' and line[0] == player1.place:
            lines = line.split()[2]
            attributes.append(lines)
        elif attribute == 'object' and line[0] == player1.place:
            lines = line.split()[3]
            attributes.append(lines)
    return attributes

player1 = player1('1')