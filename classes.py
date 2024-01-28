# Dr. McCartin-Lim's Adventure Game Engine 0.75

import textwrap
from helperfunctions import *

# Global list of every "Thing" in the game
everyThingInGame = []

# Base class Thing (all objects in the game inherit this)
class Thing:
            
    def __init__(self, name, article="a"):
        global everyThingInGame
        self.name = name
        self.article = article
        self.aliases = []
        self.description = ""
        self.interactable = True #if this were set to False, then the player can't interact with it
        self.explicitMention = True #if this were set to False, then it won't be explicitly mentioned
        everyThingInGame.append(self)
    
    def __str__(self):
        if self.article != "":
            return self.article + " " + self.name
        else:
            # Proper noun
            return self.name
    
    def examine(self):
        if self.description != "":
            print(self.description)
        else:
            if self.article != "":
                print("There is nothing notable about the "+self.name+".")
            else:
                # Proper nouns don't have an article
                print("There is nothing notable about "+self.name+".")

    
# Class for a Thing that can contain other Things        
class Container(Thing):
    
    def __init__(self, name, article="a"):
        super().__init__(name,article)
        self.contents = []
    
    # Returns a list of objects in contents that match both stringToMatch and typeToMatch and are interactible
    # When stringToMatch is the empty string, we return all objects that match the typeToMatch
    def checkFor(self,stringToMatch,typeToMatch):
        
        #Strip out article from stringToMatch if it begins with an article
        if stringToMatch.startswith("the "):
            stringToMatch = stringToMatch.split("the ")[1]
        elif stringToMatch.startswith("a "):
            stringToMatch = stringToMatch.split("a ")[1]
        elif stringToMatch.startswith("an "):
            stringToMatch = stringToMatch.split("an ")[1]
            
        #Now, search contents for matches and add to listToReturn
        listToReturn = []
        for obj in self.contents:
            if isinstance(obj, typeToMatch) and obj.interactable:
                if stringToMatch == obj.name.lower() or stringToMatch in obj.aliases or stringToMatch=="":
                    listToReturn.append(obj)
                    
        #Return the list (if nothing found, empty list is returned)
        return listToReturn



# Class for Locations in the game        
class Location(Container):
    # These instance variables define locations you can move to from this location
    north = None
    south = None
    east = None
    west = None

    # We change this instance variable to True after the location has been visited at least once
    visitedOnce = False

    # Display description of room
    def displayDescription(self,verbose=False):
        print(self.name.upper())

        # If this is the first time visiting this location or verbose is True, print the full description
        if self.visitedOnce == False or verbose==True:
            print(self.description)

        # Print the list of everything in this location that should be explicitly mentioned
        explicitList = []
        for item in self.contents:
            if item.explicitMention:
                explicitList.append(item)
        if len(explicitList) > 0:
            print("")
            print("You see " + stringFromList(explicitList) + " here.")

        # Print the directions you can travel from here
        print("")
        dirList = []
        if self.north!=None: dirList.append("North")
        if self.south!=None: dirList.append("South")
        if self.east!=None: dirList.append("East")
        if self.west!=None: dirList.append("West")
        if (len(dirList) > 0):
            print("DIRECTIONS AVAILABLE: ",stringFromList(dirList))
        else:
            print("DIRECTIONS AVAILABLE: ","None")

    # Return True if we successfully enter the location
    def enter(self):
        self.displayDescription()
        self.visitedOnce = True
        return True

    def setNorth(self,location):
        self.north = location
        location.south = self

    def setSouth(self,location):
        self.south = location
        location.north = self

    def setEast(self,location):
        self.east = location
        location.west = self

    def setWest(self,location):
        self.west = location
        location.east = self
        
    def movePlayerTo(self,newlocation):
        global player
        if(newlocation != None):
            #We only update the player's current location if we
            #successfully entered newlocation. If not the enter()
            #method will give the player some kind of error message.
            if(newlocation.enter()):
                player.currentLocation = newlocation
        else:
            print("Sorry, you can't go that way.")        
        

class Portable(Thing):
    # Return True if successful
    def get(self):
        global player
        if self in player.currentLocation.contents:
            player.currentLocation.contents.remove(self)
            player.contents.append(self)
            print("You pick up "+str(self)+".")
            #Once a Portable is picked up it becomes explicitly mentioned, if it wasn't earlier
            self.explicitMention = True
            return True
        else:
            # This else condition should never happen
            # since the parser looks for the object
            # before its get method is called
            print("But it is not here.")
            return False
        
    # Return True if successful
    def drop(self):
        global player
        if self in player.contents:
            player.contents.remove(self)
            player.currentLocation.contents.append(self)
            print("You drop "+str(self)+".")
            return True
        else:
            # This else condition should never happen
            # since the parser looks for the object
            # before its drop method is called            
            print("But you do not have it.")
            return False

# This class represents things that can be read
class Readable(Thing):
    def read(self):
        self.examine()

# This class represents things that can be used
class Usable(Thing):
    # Default message when attempting to use it. Override this in the game
    def use(self):
        
        print("But there does not seem to be any particularly good reason to use the "+self.name+" at the moment.")
        return False

# This class inherits from both Portable and Usable
class UsablePortable(Portable,Usable):
    pass

# This class represents Non-Player Characters
class NPC(Thing):
    # We can try to give items to the NPC, but by default they are rejected
    def give(self,item):
        print(str(self) + " does not want the " + item.name+".")

# Class to represent the player
class Player(Container):
    
    def __init__(self):
        self.name = "player"
        self.article = "the"
        self.aliases = ["me","myself","self"]
        self.description = "You are but one of many brave players to try to beat this game."
        self.explicitMention = False
        self.score = 0
        self.currentLocation = None
    
    def __str__(self):
        return "yourself"

    def increaseScore(self, amount):
        print("")
        print("YOUR SCORE HAS GONE UP BY "+str(amount)+" POINTS!")
        self.score += amount    

class TrappedWatch(Portable):
    minuteselapsed = 0
    def updateEveryTurn(self):
        global money
        if money in player.contents: 
            self.minuteselapsed = self.minuteselapsed + 1
            if self.minuteselapsed == 15: 
                print("Ahhh you have died of a starvation because you did not eat in time. Try to play again.") 
                exit()
        else: 
            pass
    def examine(self):
        super().examine()
        print("")
        print("Your watch reads that "+str(self.minuteselapsed)+" minutes have passed.") 


    
class CermanicBreak(Location):
    def movePlayerTo(Location):
        global key, hammer
        if Location(finearts): 
            print("BOOM! The cermanic piece breaks and a key drops. You pick up the key.") 
            key.explicitMention = True
            key.interactable = True
            player.contents.append(key)
        else: 
            print("You can't use the hammer right now.")





class DoorChapel(Location): 
    def openDoor(Location): 
        global key, player
        if key in player.contents: 
            print("Door is open yayy! There is a complex control panel in the room. You grab it, it looks important.") 
            player.contents.append(controlpanel)
        else: 
            print("You don't have anything to open the door.") 
            
class TreadMill(Location): 
  
    def treadmillPick(self): 
        if player.currentLocation == allencenter: 
            import random 
           
            answer = random.randrange(1, 5)
            NumAnswer = input("Which treadmill do you want to run on? 1,2,3,4, or 5?") 
            if NumAnswer == answer: 
                print("Noise, Spinning what is going on? You are time traveling back to the past. You found Professor Kruase's secret time machine. No wonder he runs all the time. Congrats you have beat Trapped!") 
                quit() 
            else:
                print("You went for a nice jog.") 
        else: 
            print("You are not near treadmills.")

class fijiPlace(Location):
    def FijiDeath(Location): 
        print("You take the drink and end up dying of alcohol posioning. The drinks are no lie in the future.") 
        quit()
            

            
#Global player object
player = Player() 

key = UsablePortable("key")
key.aliases = ["key"]
key.description = "An unusal pattern on a key"
key.explicitMention = False
key.interactable = False

book = Thing("Buliding A Time Machine Book") 
book.aliases = ["Buliding A Time Machine","book","time book"] 
book.description = "It appears this book tells how to bulid a time machine, cardboard, gravity amplifer, radio antenna, control panel, and a key" 

basketball = Thing("basketball") 
basketball.aliases = ["basketball"] 
basketball.description = "Oh you could play a basketball game."

cardboard = Portable("Card Board") 
cardboard.aliases = ["card board","cardboard","Card Board"]
cardboard.description = "A big brown card board box!"

cheeseBurger = Portable("cheeseburger") 
cheeseBurger.aliases = ["burger","cheeseburger","cheese burger"]
cheeseBurger.description = "That looks delicious!"

controlpanel = Portable("Control Panel") 
controlpanel.aliases = ["control panel","panel","Control Panel"]
controlpanel.description = "This looks crazy it looks like it will control something."

cermanic = Portable("Cermanic Piece") 
cermanic.aliases = ["cermanic","cermanics","cermanic piece" ]
cermanic.description = "A cermanic pieces. It would be fun to break them haha!" 
 



drink = Portable("Drink") 
drink.aliases = ["drink","alcoholic beverage"] 
drink.description = "Nice drink for a party if you are 21." 

ductTape = Portable("duct tape")
ductTape.aliases = ["duct tape","tape"] 
ductTape.description = "This tape seems like it will hold many things together."

flashlight = Portable("Flashlight") 
flashlight.aliases = ["Flashlight","light","flashlight"] 
flashlight.description = "You can see in the dark with this!"

gravityAmplifer = Portable("Gravity Amplifer") 
gravityAmplifer.aliases = ["gravity amplifer","gravity amp","Gravity Amplifer"] 
gravityAmplifer.description = "This has a lot of potential." 

hammer = UsablePortable("Hammer") 
hammer.aliases = ["hammer","Hammer"]
hammer.description = "It is just a hammer."

money = Portable("Money") 
money.aliases = ["money","Money"] 
money.descripition = "You have a couple dollar you can buy some lunch."

pooltable = Thing("Pool Table") 
pooltable.aliases = ["Pool Table","pool table"] 
pooltable.description = "Stay and play a game of pool on the new table."

radioantenna = Portable("Radio Antenna") 
radioantenna.alaises=["radio antenna","antenna","Radio Antenna"] 
radioantenna.description = "Gray and big but will get some good connection."

watch = TrappedWatch("watch")
watch.aliases = ["watch"]
watch.description = "You tell time with that Rolex. The watch reads 4:45."


# LOCATIONS
allencenter = Location("Allen Center")
beta = Location("Beta")
baxter = Location("Baxter Hall")
chapel = Location("Chapel") 
collegehall = Location("College Hall") 
detchon = Location("Decthon Hall") 
fiji = Location("Fiji") 
finearts = Location("Fine arts center") 
footballfield = Location("Football Field")
goodrich = Location("Goodrich") 
hays = Location("Hays Hall")
Lambda = Location("Lambda Chi Alpha")
library = Location("The Lily Library") 
mall = Location("Center of the Mall") 
martindale = Location("Martindale") 
sidewalkA2 = Location("side walk") 
sidewalkC4 = Location("side walk") 
sidewalkC1 = Location("side walk") 
sidewalkE1 = Location("side walk") 
sparks = Location("Sparks") 

allencenter.description = "You find yourself in a the weight room and appears that their are 5 treadmills."
allencenter.contents = [basketball]
allencenter.setNorth(sidewalkA2) 
allencenter.setEast(goodrich) 
allencenter.setSouth(Lambda) 
      
beta.description = "You are at the faternity Beta Theta Pi. A small party seems to be going on"
beta.setEast(library) 
beta.setSouth(sidewalkA2) 


baxter.description = "Some much learning in this buliding."
baxter.contents = [ductTape]
baxter.setNorth(hays)  
baxter.setEast(finearts) 
baxter.setSouth(martindale) 
baxter.setWest(chapel)

chapel.description = "You are in the chapel and it appears there is a mysteriously locked door"
chapel.contents = [controlpanel] 
chapel.setNorth(mall) 
chapel.setEast(baxter)
chapel.setSouth(sidewalkC4)
chapel.setWest(goodrich) 

collegehall.description = "This place seems very dirty but nice to in" 
collegehall.contents = [radioantenna] 
collegehall.setNorth(finearts)
collegehall.setWest(martindale) 

detchon = Location("Detchon Hall") 
detchon.description ="There is tons of card board in this buliding right now"
detchon.contents = [cardboard] 
detchon.setEast(sidewalkE1)
detchon.setSouth(hays) 
detchon.setWest(sidewalkC1) 

fiji.description = "It's party time for fiji. Lights, music, and everything else that makes a party" 
fiji.contents = [drink]
fiji.setNorth(sidewalkE1) 
fiji.setSouth(finearts)
fiji.setWest(hays)

finearts.description = "All the creative minds are in this location, crafting away at their master pieces. You are surpised at how different art is in the new time period."
finearts.contents = [key,cermanic]
finearts.setNorth(fiji)
finearts.setSouth(collegehall) 
finearts.setWest(baxter) 

footballfield.description = "You could play a nice game of football but do not interfere with practice." 
footballfield.setNorth(goodrich) 
footballfield.setEast(sidewalkC4) 
footballfield.setWest(Lambda) 

goodrich.description = "It appears a robotic Profesor Krause working on very odd project" 
goodrich.contents = [gravityAmplifer] 
goodrich.setNorth(sparks) 
goodrich.setEast(chapel) 
goodrich.setSouth(sidewalkC4) 
goodrich.setWest(allencenter) 
 
hays.description = "Lots of experiments go on in this room. Interesting stuff" 
hays.contents = [hammer]
hays.setNorth(detchon)
hays.setEast(fiji)
hays.setSouth(baxter)
hays.setWest(mall)
 
Lambda.description = "Just another faternity." 
Lambda.contents = [flashlight] 
Lambda.setNorth(allencenter)
Lambda.setEast(footballfield)

library.description = "The library always has the information to your problems. There are books to fix all your problems."
library.contents = [book] 
library.setEast(sidewalkC1) 
library.setSouth(sparks) 
library.setWest(beta) 

mall.description = ("This where everything is happening and it is the center" 
                    " of Wabash College campus.") 
mall.setNorth(sidewalkC1) 
mall.setEast(hays)
mall.setSouth(chapel) 
mall.setWest(sparks)

martindale.description = "Oh you can play come pool with in this buliding" 
 
martindale.setNorth(baxter) 
martindale.setEast(collegehall) 
martindale.setWest(sidewalkC4)


sidewalkA2.description = "There isn't much here other then a way to go to other places." 
sidewalkA2.setNorth(beta) 
sidewalkA2.setEast(sparks) 
sidewalkA2.setSouth(allencenter)

sidewalkC4.description = "Not much to see here" 
sidewalkC4.setNorth(chapel) 
sidewalkC4.setEast(martindale) 
sidewalkC4.setWest(footballfield) 


sidewalkC1.description = "You can walk to other places." 
sidewalkC1.setWest(detchon)
sidewalkC1.setSouth(mall) 
sidewalkC1.setWest(library) 


sidewalkE1.description = "People walk on side walks to get places" 
sidewalkE1.setSouth(fiji) 
sidewalkE1.setWest(fiji)


sparks.description = "This is where you can find all the food." 
sparks.contents = [cheeseBurger]
sparks.setNorth(library) 
sparks.setEast(mall) 
sparks.setSouth(goodrich) 
sparks.setWest(sidewalkA2)  


