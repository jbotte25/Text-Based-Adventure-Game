#  Adventure Game Engine 0.5

from classes import *
from helperfunctions import *

# ITEMS

poolTable = Thing("Pool Table") 
poolTable.aliases = ["pool table", "Pool Table", "pool"] 
poolTable.description = "You can play with Martindale Marshions." 


dog = NPC("dog") 
dog.aliases = ["dog"]
dog.description = "It's loud and aggresive. He has a chrome futuristic suit on watch out!" 

bone = UsablePortable("bone") 
bone.aliases = ["bone"] 
bone.description = "It looks like an old bone something could eat it." 

key = UsablePortable("key")
key.aliases = ["key"]
key.description = "An unusal pattern on a key."
key.explicitMention = False
key.interactable = False

book = Portable("Buliding A Time Machine Book") 
book.aliases = ["Buliding A Time Machine","book","time book","book"] 
book.description = "It appears this book tells how to bulid a time machine, cardboard, gravity amplifer, radio antenna, control panel, and a key." 

basketball = Thing("basketball") 
basketball.aliases = ["basketball"] 
basketball.description = "Oh you could play a basketball game."

cardboard = Portable("Card Board") 
cardboard.aliases = ["card board","cardboard","Card Board"]
cardboard.description = "A big brown card board box!"

cheeseBurger = Portable("cheeseburger") 
cheeseBurger.aliases = ["burger","cheeseburger","cheese burger"]
cheeseBurger.description = "That looks delicious!"
cheeseBurger.interactable = True
cheeseBurger.explicitMention = True

controlpanel = Portable("Control Panel") 
controlpanel.aliases = ["control panel","panel","Control Panel"]
controlpanel.description = "This looks crazy it looks like it will control something."
controlpanel.explicitMention = False
controlpanel.interactable = False

cermanic = Portable("cermanic piece")
cermanic.aliases = ["cermanic","cermanics","cermanic piece" ]
cermanic.description = "A cermanic pieces. It would be fun to break them haha!" 
cermanic.interactable = True
cermanic.explicitMention = True


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

money = Portable("money") 
money.aliases = ["money","Money"] 
money.descripition = "You have a couple dollar you can buy some lunch."

pooltable = Thing("Pool Table") 
pooltable.aliases = ["Pool Table","pool table"] 
pooltable.description = "Stay and play a game of pool on the new table."

radioantenna = Portable("Radio Antenna") 
radioantenna.alaises=["radio antenna","antenna","Radio Antenna"] 
radioantenna.description = "Gray and big but will get some good connection."
radioantenna.explicitMention = False
radioantenna.interactable = False

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
      
beta.description = "You are at the faternity Beta Theta Pi. A small party seems to be going on."
beta.setEast(library) 
beta.setSouth(sidewalkA2) 


baxter.description = "Some much learning in this buliding."
baxter.contents = [ductTape]
baxter.setNorth(hays)  
baxter.setEast(finearts) 
baxter.setSouth(martindale) 
baxter.setWest(chapel)

chapel.description = "You are in the chapel and it appears there is a mysteriously locked door."
chapel.contents = [controlpanel] 
chapel.setNorth(mall) 
chapel.setEast(baxter)
chapel.setSouth(sidewalkC4)
chapel.setWest(goodrich) 

collegehall.description = "This place seems very dirty but nice inside. Bark! Bark! A dog is inside the buliding guarding some item?" 
collegehall.contents = [radioantenna,dog] 
collegehall.setNorth(finearts)
collegehall.setWest(martindale) 

detchon = Location("Detchon Hall") 
detchon.description ="There is tons of card board in this buliding right now."
detchon.contents = [cardboard] 
detchon.setEast(sidewalkE1)
detchon.setSouth(hays) 
detchon.setWest(sidewalkC1) 

fiji.description = "It's party time for fiji. Lights, music, and everything else that makes a party." 
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

goodrich.description = "It appears a robotic Profesor Krause working on very odd project." 
goodrich.contents = [gravityAmplifer] 
goodrich.setNorth(sparks) 
goodrich.setEast(chapel) 
goodrich.setSouth(sidewalkC4) 
goodrich.setWest(allencenter) 
 
hays.description = "Lots of experiments go on in this room. Interesting stuff." 
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

mall.description = ("This where everything is happening and it is the center." 
                    " of Wabash College campus.") 
mall.setNorth(sidewalkC1) 
mall.setEast(hays)
mall.setSouth(chapel) 
mall.setWest(sparks)
mall.contents =[money]

martindale.description = "Oh you can play come pool with in this buliding." 
martindale.contents = [bone]
martindale.setNorth(baxter) 
martindale.setEast(collegehall) 
martindale.setWest(sidewalkC4)


sidewalkA2.description = "There isn't much here other then a way to go to other places." 
sidewalkA2.setNorth(beta) 
sidewalkA2.setEast(sparks) 
sidewalkA2.setSouth(allencenter)

sidewalkC4.description = "Not much to see here." 
sidewalkC4.setNorth(chapel) 
sidewalkC4.setEast(martindale) 
sidewalkC4.setWest(footballfield) 


sidewalkC1.description = "You can walk to other places." 
sidewalkC1.setEast(detchon)
sidewalkC1.setSouth(mall) 
sidewalkC1.setWest(library) 


sidewalkE1.description = "People walk on side walks to get places." 
sidewalkE1.setSouth(fiji) 
sidewalkE1.setWest(detchon)


sparks.description = "This is where you can find all the food." 
sparks.contents = [cheeseBurger]
sparks.setNorth(library) 
sparks.setEast(mall) 
sparks.setSouth(goodrich) 
sparks.setWest(sidewalkA2)  


