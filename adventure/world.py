import random

class Places:
    enviroment = ['Desert', 'Jungle', 'Mountain', 'Urban']
    weather = ['Raining', 'Snowing', 'Sunny']
    object = ['Buildings', 'People', 'River', 'Tree']

    def __init__(self, name):
        self.name = name
        self.attributes = []

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

def generatePlace():
    name = 'a'
    file = open('places.txt', 'r')
    for line in file:
        if line[0] == name:
            name = chr(ord(name)+1)
    name = Places(name)
    name.add_attribute(Places.enviroment[random.randint(0,len(Places.enviroment) - 1)])
    name.add_attribute(Places.weather[random.randint(0,len(Places.weather) - 1)])
    name.add_attribute(Places.object[random.randint(0,len(Places.object) - 1)])
    writePlace(name.name, name.attributes[0], name.attributes[1], name.attributes[2])

def writePlace(name, enviroment, weather, object):
    file_object = open('places.txt', 'a')
    file_object.write(str(name) +", " + str(enviroment) +", " + str(weather) +", " + str(object) + '\n')

