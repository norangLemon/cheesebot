from DB import *
from Message import *
from datetime import datetime

class Person():
    ID = None
    nick = None
    name = None
    affection = 0
    lastPat = None
    def __init__(self, msg):
        self.ID = msg.ID
        self.nick = msg.nick
        self.name = msg.nick
        self.lastPat = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    
    def __init__(self, ID, nick, name, affection, lastPat):
        self.ID = ID
        self.nick = nick
        self.name = name
        self.affection = affection
        self.lastPat = lastPat

    def plus(self, amount):
        self.affection += amount
        self.lastPat = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        updateData(self)
        return self

    def minus(self, amount):
        self.affection -= amount
        updateData(self)
        return self

    def rename(self, newName):
        self.name = newName
        self.lastPat = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        updateData(self)

    def getAffection(self):
        return self.affection
    
def getPerson(msg):
    person = search(msg)
    if person == None:
        person = Person(msg)
        insertData(person)
    return person
# db update module is needed



# main: poll module
# random picking module is needed
# randomly talking module is needed

# reaction based on affection is needed
# HowMuchLove module is needed
