#Adventure Game Engine 0.5

from classes import *
from helperfunctions import *
from commandparser import *

# Here's the data for our game
from gamedata import *

print("               Welcome to Trapped.\n\n    "" You have woke up in the future on Wabash College campus!\n" 
      "As you wake up you can not recall how you got here\n" 
      "200 years in the future is a far into the future!\n" 
      "The bulidings are all chrome and float.\n"
      "Try to find your way out or live in the future your choice\n\n"  
      "Type help if you want a few word list or clues\n\n")
print(" You are staving make sure you eat dinner at Sparks before 5:00\n\n")
#Play game
player.contents = [watch]
player.currentLocation = mall
mall.enter()
while(True):
    # Check each thing in the game and call its updateEveryTurn method if it exists
    for thing in everyThingInGame:
        if hasattr(thing,"updateEveryTurn"):
            thing.updateEveryTurn()
            
    command = input("> ")
    print("")
    parseCommand(command) 
    
