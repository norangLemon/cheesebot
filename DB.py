import sqlite3
import sys
from Log import *
from setting import *

connection = sqlite3.connect(DB_PEOPLE)
cursor = connection.cursor()
def insertData(person):
    cursor.execute("INSERT INTO People VALUES(%s, %s, %d, %s)"
                    %(person.ID, person.nick, person.affection, person.lastPat))
    connection.commit()

def searchByNick(nick):
    cursor.execute("SELECT * FROM People WHERE nick='%s'" %nick)
    result = cursor.fetchall()
    if len(result) == 1:
        return Person(result[0][0], result[0][1], result[0][2], result[0][3])
    else:
        prtErr("nick %s:\n %s" %str(result))
        return None

def createDB(cursor):
    cursor.execute("CREATE TABLE People(ID text, nick text, affection int, lastPat text)")
    connection.commit()
    prtInfo("DB is created!")

def printDB(cursor):
    num = 0
    print("ID\t\t\t\t\tnick\t\taffection\tlast pat")
    print("--------------------------------------------")
    for row in cursor.execute("SELECT * FROM People ORDER BY affection"):
        print("%s\t\t\t\t\t%s\t\t%d\t%s"
                % (row[0], row[1], row[2], row[3]))
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

