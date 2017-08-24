import world

class player1:
    def __init__(self, name):
        self.name = name
        self.actions = ['Look', 'Move']
        self.place = 'a'
        self.data = []
        self.inventory = []

    def add_data(self, data):
        self.data.append(data)

    def add_inventory(self, item):
        self.inventory.append(item)

    def move(self, direction):
        if direction == 'right':
            places = getPlace('name')
            if player1.place == places[-1].replace(",",""):
                world.generatePlace()
            player1.place = chr(ord(player1.place) + 1)
            print ('You have successfully moved to the place right of you')
        elif direction == 'left':
            if player1.place != 'a':
                player1.place = chr(ord(player1.place) - 1)
                print 'You have successfully moved to the place left of you'
            elif player1.place == 'a':
                print 'There is no place to move to, sorry'

    def look(self):
        self.data = []
        print('You are in place ' + str(player1.place))
        print('The place right of you is ' + (chr(ord(player1.place) + 1)))
        if player1.place == 'a':
            print ('There is no place left of you')
        else:
            print('The place left of you is ' + (chr(ord(player1.place) - 1)))
        player1.add_data(getPlace('enviroment'))
        player1.add_data(getPlace('weather'))
        player1.add_data(getPlace('object'))
        print(str(player1.data[0]).replace(",","")+" "+str(player1.data[1]).replace(",","")+" "+str(player1.data[2]))

    def pick_up(self):
        if getPlace('object') == ['Coin']:
            player1.add_inventory(getPlace('object'))
            print ('You have picked up a coin')
        else:
            print 'You can not pick up that object'

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

