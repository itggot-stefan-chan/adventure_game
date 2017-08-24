import world
import player

def init():
    world.generatePlace()
    print('Welcome to an adventure game!')
    print('Type "move(left or right)" to move to an another place, "look" to look at the place you are in')
    print('To quit, type "quit"')
    adventure()

def adventure():
    while True:
        read = raw_input()
        if read == 'move(left)':
            player.player1.move('left')
            print ('You have successfully moved to the place left of you')
        elif read == 'move(right)':
            player.player1.move('right')
        elif read == 'look':
            player.player1.look()
        elif read == 'quit':
            quit()

init()
