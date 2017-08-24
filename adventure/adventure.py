import world
import player

def init():
    #world.wipe_places()
    world.generatePlace()
    print('Welcome to an adventure game!')
    print('Type "move(left or right)" to move to an another place, "look" to look at the place you are in')
    print ('Type "pick up" to see if you can pick up an object and "inventory" to see what objects you have')
    print('To quit, type "quit"')
    adventure()

def adventure():
    while True:
        read = raw_input()
        if read == 'move(left)':
            player.player1.move('left')
        elif read == 'move(right)':
            player.player1.move('right')
        elif read == 'look':
            player.player1.look()
        elif read == 'pick up':
            player.player1.pick_up()
        elif read == 'inventory':
            print player.player1.inventory
        elif read == 'quit':
            quit()

init()
