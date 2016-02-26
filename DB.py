import sqlite3
import sys
from Log import *
from setting import *
from Person import *

connection = sqlite3.connect(DB_PEOPLE)
cursor = connection.cursor()
def insertData(person):
    cursor.execute("INSERT INTO People VALUES('%s', '%s', '%s',  %d, '%s')"\
                    %(person.ID, person.nick, person.name, person.affection, person.lastPat))
    connection.commit()

def updateData(person):
    if person.ID != ID_BYB_BOT:
        cursor.execute("UPDATE People SET name = '%s', affection=%d, lastPat='%s' WHERE ID='%s'"\
                % (person.name, person.affection, person.lastPat, person.ID))
    else:
        cursor.execute("UPDATE People SET name = '%s', affection=%d, lastPat='%s' WHERE nick='%s'"\
            %(person.name, person.affection, person.lastPat, person.nick))
    connection.commit()

def search(msg):
    if msg.ID != ID_BYB_BOT:
        cursor.execute("SELECT * FROM People WHERE ID='%s'" %msg.ID)
    else: 
        cursor.execute("SELECT * FROM People WHERE nick='%s'" %msg.nick)
    result = cursor.fetchall()
    if len(result) == 1:
        return Person(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4])
    elif len(result) == 0:
        prtLog("There's no nick %s's DB" %msg.nick)
    else:
        prtErr("nick %s:\n %s" %str(result))
    return None

def createDB(cursor):
    cursor.execute("CREATE TABLE People(ID text, nick text, name text, affection int, lastPat text)")
    connection.commit()
    prtInfo("DB is created!")

def printDB(cursor):
    num = 0
    print("ID\t\t\t\t\tnick\t\tname\t\taffection\tlast pat")
    print("--------------------------------------------")
    for row in cursor.execute("SELECT * FROM People ORDER BY affection"):
        print("%s\t\t\t\t\t%s\t\t%s\t\t%d\t%s"
                % (row[0], row[1], row[2], row[3], row[4]))
        num += 1
    print("--------------------------------------------")
    print("total: %d" %num)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "create":
            createDB(cursor)
        elif sys.argv[1] == "print":
            printDB(cursor)
    else:
        print("create or print")

