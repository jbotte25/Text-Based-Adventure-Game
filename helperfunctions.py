#  Adventure Game Engine 0.75

import sys
import textwrap
import builtins

#Overriding the built-in print function to word wrap what's printed
def print(*strings,sep=" ",end="\n",file=sys.stdout, flush=False):
    
    #Concatenate all the strings together into catstring
    catstring = ""
    count = 0
    for string in strings:
        catstring += string
        if count < len(strings)-1:
            catstring += sep
        count += 1
    
    #Create a wrapped string from catstring
    wrappedstring = ""
    count = 0
    wrapper = textwrap.TextWrapper()
    wrapper.replace_whitespace = False
    for string in catstring.splitlines():
        wrappedstring += wrapper.fill(string)
        if count < len(catstring.splitlines())-1:
            wrappedstring += "\n"
        count += 1
    
    #Call built-in print function with wrappedstring and pass-in other parameters
    builtins.print(wrappedstring,end=end,file=file,flush=flush)
    
#General function to create a string from a list of objects
def stringFromList(itemList, andWord="and"):
    #If the list only has one item in it, return string representing that item
    if len(itemList)==1:
        return str(itemList[0])
    else:
        strToReturn = ""
        for i in range(0,len(itemList)):
            if i == len(itemList) - 1:
                strToReturn = strToReturn + andWord + " " + str(itemList[i])
            elif i == len(itemList) - 2:
                strToReturn = strToReturn + str(itemList[i]) + " "
            else:
                strToReturn = strToReturn + str(itemList[i]) + ", "
        return strToReturn 
    
def help(): 
    print(" Your verbs are get, break, assemble, drink, buy, eat, use, read, examine, north, south, west, east, open, drop, give, and inventory.") 
