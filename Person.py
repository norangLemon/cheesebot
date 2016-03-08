from DB import *
from Message import *
from Log import *
from setting import *
from datetime import datetime

class Person():
    ID = None
    nick = None
    name = None
    affection = 0
    lastPat = None
    firstPat = None
    secondPat = None
    thirdPat = None
    def __init__(self, ary = None, msg=None):
        if ary!= None:
            self.ID = ary[0]
            self.nick = ary[1]
            self.name = ary[2]
            self.affection = ary[3]
            self.lastPat = ary[4]
            self.fisrtPat = ary[5]
            self.secondPat = ary[6]
            self.thirdPat = ary[7]
        if msg != None:
            self.ID = msg.ID
            self.nick = msg.nick
            self.name = msg.nick
            self.lastPat = datetime.now().strftime(TIME_FORMAT)

    
    def plus(self, amount):
    # return false when he/she is annoying Cheese
        self.updateTime()
        result = True
        if self.isAnnoying():
            amount = -10
            result = False
        self.affection += amount

        if self.affection > MAX_AFFECTION:
            self.affection = MAX_AFFECTION
        elif self.affection < MIN_AFFECTION:
            self.affection = MIN_AFFECTION
        updateData(self)
        return result

    def minus(self, amount):
    # return false when he/she is annoying Cheese
        self.updateTime()
        result = True
        if self.isAnnoying():
            amount = 10
            result = False
        self.affection -= amount
        if self.affection < MIN_AFFECTION:
            self.affection = MIN_AFFECTION
        updateData(self)
        return result

    def rename(self, newName):
        self.name = newName
        updateTime(self)
        updateData(self)

    def getAffection(self):
        return self.affection
    
    def updateTime(self):
        self.firstPat = self.secondPat
        self.secondPat = self.thirdPat
        self.thirdPat = self.lastPat
        self.lastPat = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    def isAnnoying(self):
        try:
            print("parse")
            first = datetime.strptime(self.firstPat, TIME_FORMAT)
            last = datetime.strptime(self.lastPat, TIME_FORMAT)
            result = last - first
            return (result.seconds <10)
        except Exception as err:
            prtErr(err)
            prtErr(self.firstPat)
        return False


def getPerson(msg):
    args = search(msg)
    if args == None:
        person = Person(msg=msg)
        insertData(person)
    else:
        person = Person(args)

    return person
# db update module is needed



# main: poll module
# random picking module is needed
# randomly talking module is needed

# reaction based on affection is needed
# HowMuchLove module is needed
