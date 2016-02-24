from setting import *
from Message import *
import pickle
import datetime

class Person:
    ID = None
    nick = None
    affection = 0
    last_said = None
    def __init__(ID, nick, time):
        self.ID = ID
        self.nick = nick
        last_said = time

    def getdata(msg):
        filename = msg.ID == ID_BYB_BOT ? "BYB"+msg.nick : msg.ID
        try:
            rawfile = open(filename, rb)
            person = pickle.load(rawfile)
        except IOError:
            person = Person(msg.ID, msg.nick, datetime.datetime.now())
            rawfile = open(filename, wb)
            print("New person resisted: %s - %s" % msg.nick, msg.ID)
        finally:
            close(rawfile)
        return person

    def setdata(person):
        filename = person.ID == ID_BYB_BOT ? "BYB"+person.nick : person.ID
        try:
            rawfile = open(filename, wb)
            pickle.dump(person, rawfile)
        except as err:
            print("data setting err: %s" %s)
            print("ID: %s \nnick: %s\n affection: %s\n last_said: %s" %person.ID, person.nick, person.affection, person.last_said)

    def refreshTime(person):
        person.last_said = datetime.datetime.now()

    def plus(msg):
        person = getdata(msg)
        person.affection = person.affection == MAX_AFFECTION? person.affection : person.affection++
        refreshTime(person)
        setdata(person)

    def minus(msg):
        person = getdata(msg)
        person.affection = person.affection == MIN_AFFECTION? person.affection : person.affection--
        refreshTime(person)
        setdata(person)

