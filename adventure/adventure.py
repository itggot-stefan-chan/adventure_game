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
        read = input()
        if read == 'move(left)':
            player.player1.move('left')
        elif read == 'move(right)':
            player.player1.move('right')
        elif read == 'look':
            player.player1.look()
        elif read == 'quit':
            quit()

init()