#  Adventure Game Engine 0.75

from classes import *
from helperfunctions import *

# Here's the data for our game
from gamedata import *

dogThere = 1

def parseCommand(command):
    global player
    # Convert command to lowercase
    command = command.lower()
    
    # Check each verb
    if command == "look":
        # Print a verbose description of the player's current location
        player.currentLocation.displayDescription(True)
    
    elif command == "help": 
        help()
    
    elif command == "quit":
        #Exit the game
        exit()
    
    elif command.startswith("run "): 
        objToUse = command.split("run ")
        if player.currentLocation == allencenter: 
            import random
            answer = random.randint(1,5)
            NumAnswer = input("Which treadmill do you want to run on? 1,2,3,4, or 5?") 
            if NumAnswer == answer: 
                print("Noise, Spinning what is going on? You are time traveling back to the past. You found Professor Kruase's secret time machine. No wonder he runs all the time. Congrats you have beat Trapped!") 
                quit() 
            else:
                print("You went for a nice jog.") 
        else: 
            print("You are not near treadmills.")              
        
    
    
    
    elif command == "score":
        #Print the player's current score
        print("Your current score is now "+str(player.score)+ " points.")
    
    elif command == "inventory" or command == "inv" or command == "i":
        if len(player.contents) == 0:
            print("You are not carrying anything!")
        else:
            print("You have "+stringFromList(player.contents)+".")
        
    elif command == "north" or command == "n":
        player.currentLocation.movePlayerTo(player.currentLocation.north)
            
    elif command == "south" or command == "s":
        player.currentLocation.movePlayerTo(player.currentLocation.south)
            
    elif command == "east" or command == "e":
        player.currentLocation.movePlayerTo(player.currentLocation.east)
            
    elif command == "west" or command == "w":
        player.currentLocation.movePlayerTo(player.currentLocation.west) 
    
    elif command == "read book": 
        print("It appears this book tells how to bulid a time machine, cardboard, gravity amplifer, radio antenna, control panel, and a key.") 
        
      
    elif command.startswith("examine "):
        objToLookat = command.split("examine ")[1]
        # Search both the current location and the player's inventory
        matches = player.currentLocation.checkFor(objToLookat,Thing) + player.checkFor(objToLookat,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].examine()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # We found no matches
        else:
            print("I do not know what you are referring to.")     
    
    elif command.startswith("read "):
        objToLookat = command.split("read ")[1]
        
        # Search both the current location and the player's inventory
        matches = player.currentLocation.checkFor(objToLookat,Readable) + player.checkFor(objToLookat,Readable)
        badmatches = player.currentLocation.checkFor(objToLookat,Thing) + player.checkFor(objToLookat,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].read()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # Player may be referring to a Thing that is not Readable
        elif len(badmatches) >= 1:
            print("There doesn't seem to be anything interesting to read on the " + badmatches[0].name + ".")
        # We found no matches
        else:
            print("I do not know what you are referring to.")

    elif command.startswith("use "):
        objToUse = command.split("use ")[1]
        # Search both the current location and the player's inventory
        matches = player.currentLocation.checkFor(objToUse,Usable) + player.checkFor(objToUse,Usable)
        badmatches = player.currentLocation.checkFor(objToUse,Thing) + player.checkFor(objToUse,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].use()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        elif len(badmatches) >= 1:
            print("How would you use "+str(badmatches[0])+"?")
        # We found no matches
        else:
            print("I do not know what you are referring to.")

    elif command.startswith("get "):
        objToGet = command.split("get ")[1]
        matches = player.currentLocation.checkFor(objToGet,Portable)
        badmatches1 = player.checkFor(objToGet,Portable)
        badmatches2 = player.currentLocation.checkFor(objToGet,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].get()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # The player may be referring to an item they already have
        elif len(badmatches1) >= 1:
            print("You already have " + str(badmatches1[0]) + ".")
        # The player may be referring to something that is not obtainable
        elif len(badmatches2) >= 1:
            unobtainable = badmatches2[0].name
            # If it's not a proper noun, we will use the article "the"
            if badmatches2[0].article != "":
                unobtainable = "the " + unobtainable
            print("You are cannot remove "+unobtainable+".")
        # We found no matches
        else:
            print("I do not know what you are referring to.")

    # The "buy" verb is specific to the Flyaway game
    elif command.startswith("buy "):
        objToGet = command.split("buy ")[1]
        if player.currentLocation == sparks and money in player.contents: 
            
            
            print("You have brought a cheeseburger from Sparks.") 
            player.contents.append(cheeseBurger) 
            player.contents.remove(money)
        else: 
            print("You can not buy anything from this location.")
    
    elif command.startswith("eat "): 
        objToGet = command.split("eat ")[1] 
        if cheeseBurger in player.contents: 
            print("You are full after that cheeseburger.") 
            player.contents.remove(cheeseBurger)
            cheeseBurger.interactable = False 
            cheeseBurger.explicitMention = False 
            
    elif command.startswith("break "): 
        objToGet = command.split("break ")[1] 
        if hammer in player.contents and player.currentLocation == finearts: 
            print("BOOM! The cermanic piece breaks and a key drops. You pick up the key.") 
            key.explicitMention = True
            key.interactable = True
            player.contents.append(key) 
            cermanic.explicitMention = False
            cermanic.interactable =False
        else: 
            print("You can not break anything.")
    
    elif command.startswith("drink "): 
        objToGet = command.split("drink ")[1] 
        if drink in player.contents: 
            print("You take the drink and end up dying of alcohol posioning. The drinks are no lie in the future.") 
            quit()            
    
    elif command.startswith("give "):
        objToGet = command.split("give ")[1] 
        if bone in player.contents and player.currentLocation == collegehall: 
            global dogThere
            print("The dog left the buliding.")
            collegehall.contents.remove(dog) 
            radioantenna.explicitMention = True 
            radioantenna.interactable = True
            print("The dog was guarding a radio antenna.") 
            print("You probably need that.")
    
    elif player.currentLocation == collegehall: 
        dogThere = dogThere + 1 
    
    elif dog in collegehall.contents and dogThere == 2: 
        print("You have been attacked by the dog and you have died from blood lost.") 
        quit()
        
    
        
            
            
        
            
        
    
    elif player.currentLocation == beta: 
        print("The beta guys asked if you wanted to ride in there flying vechile to Purdue?") 
        usertypes = input("Do you want to go? yes or no?")
        if usertypes == ("yes"):  
            print("You end up dying from motion sickness the car had to much power for you to deal with. The future is something unreal.") 
            quit()
        
        
        
    
    elif command.startswith("open "): 
        objToGet = command.split("open ")[1] 
        if key in player.contents and player.currentLocation == chapel: 
            print("Door is open yayy! There is a complex control panel in the room. It looks important.") 
            controlpanel.explicitMention = True
            controlpanel.interactable = True
            
    elif command.startswith("play "):
        objToGet = command.split("play ")[1] 
        if currentLocation == martindale: 
            print("You play pool for hours and have a great time with the Martindale Marshions.") 
        else: 
            print("There is nothing to play.")
    
    elif command.startswith("assemble "): 
        objToGet = command.split("assemble ")[1] 
        if cardboard in player.contents and gravityAmplifer in player.contents and ductTape in player.contents and radioantenna in player.contents and controlpanel in player.contents and key in player.contents: 
            print("You have assembled your time machine! Now you can go back to the future. You turn the key and disappear into the past to Wabash in 2022. You have beat the game congrats!")
            quit()
        else: 
            print("You do not have enough materials to assemble anything.") 
            
    elif command.startswith("drop "):
        objToGet = command.split("drop ")[1]
        matches = player.checkFor(objToGet,Portable)
        badmatches = player.currentLocation.checkFor(objToGet,Thing)
        # We found an exact match
        if len(matches) == 1:
            matches[0].drop()
        # There are multiple matches, so it's ambiguous what the player is referencing
        elif len(matches) > 1:
            print("Are you talking about " + stringFromList(matches,"or") + "?")
        # The player may be referring to something else in their current location
        elif len(badmatches) >= 1:
            unobtainable = badmatches[0].name
            # If it's not a proper noun, we will use the article "the"
            if badmatches[0].article != "":
                unobtainable = "the " + unobtainable
            print("But you are not carrying "+unobtainable+".")
        # We found no matches
        else:
            print("I do not know what you are referring to.")

    # Implements GIVE X TO Y
    elif command.startswith("give "):
        giveString = command.split("give ")[1]
        givePart = giveString.rpartition(" to ")
        thingToGive = givePart[0]
        npcToGiveTo = givePart[2]
        if(thingToGive == ""):
            print("I do not know what you mean.")
        else:
            thingMatches = player.checkFor(thingToGive,Thing)
            npcMatches = player.currentLocation.checkFor(npcToGiveTo,NPC)
            # We found an exact match for both NPC and the item
            if len(npcMatches) == 1 and len(thingMatches) == 1:
                npcMatches[0].give(thingMatches[0])
            # Possible error messages
            elif len(npcMatches) > 1:
                print("Are you talking about " + stringFromList(npcMatches,"or") + "?")
            elif len(thingMatches) > 1:
                print("Are you talking about " + stringFromList(thingMatches,"or") + "?")
            elif len(npcMatches) == 0:
                print("No idea who you are referring to.")
            elif len(thingMatches) == 0:
                print("You cannot give what you do not have.")

    # "look at" is a synonym for "examine"
    elif command.startswith("look at "):
        objToLookat = command.split("look at ")[1]
        parseCommand("examine "+objToLookat)

    # "take" is a synonym for "get"
    elif command.startswith("take "):
        objToGet = command.split("take ")[1]
        parseCommand("get "+objToGet)

    # permit "go" prefix in game, for instance "go north" should be synonym for "north"
    elif command.startswith("go "):
        gosuffix = command.split("go ")[1]
        parseCommand(gosuffix)
            
    else:
        print("I do not understand what you want to do.")
