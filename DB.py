import sqlite3
import sys
from Log import *
from setting import *
from datetime import datetime

connection = sqlite3.connect(DB_PEOPLE)
cursor = connection.cursor()
def insertData(person):
    cursor.execute("INSERT INTO People VALUES('%s', '%s', '%s',  %d, '%s', '%s', '%s', '%s')"\
                    %(person.ID, person.nick, person.name, person.affection, person.lastPat, person.firstPat, person.secondPat, person.thirdPat))
    connection.commit()

def updateData(person):
    cursor.execute("UPDATE People SET name = '%s', affection=%d, lastPat='%s', firstPat = '%s', secondPat = '%s', thirdPat ='%s' WHERE ID='%s' AND nick ='%s'"\
                % (person.name, person.affection, person.lastPat, person.firstPat, person.secondPat, person.thirdPat, person.ID, person.nick))
    connection.commit()

def search(msg):
    cursor.execute("SELECT * FROM People WHERE ID='%s' AND nick='%s'" %(msg.ID, msg.nick))
    result = cursor.fetchall()
    if len(result) == 1:
        return (result[0])

    elif len(result) == 0:
        prtLog("There's no '%s' in DB" %msg.nick)
    else:
        prtErr("nick %s:\n %s" %str(result))
    return None

def createDB(cursor):
    cursor.execute("CREATE TABLE People(ID text, nick text, name text, affection int, lastPat text, firstPat text, secondPat text, thirdPat text)")
    cursor.execute("INSERT INTO People VALUES('%s', '%s', '%s',  %d, '%s')"\
            %(ID_NORANG, 'norang', '주인님', MAX_AFFECTION, datetime.now().strftime("%y-%m-%d %H:%M:%S")))
    connection.commit()
    prtInfo("DB is created!")

def printDB(cursor):
    num = 0
    print("%10s%20s%20s%40s%20s%20s" %("affection", "last pat", "first pat", "ID", "nick", "name"))
    print("-"*130)
    for row in cursor.execute("SELECT * FROM People ORDER BY affection"):
        print("%10s%20s%20s%40s%20s%20s"
                % (row[3], row[4], row[5], row[0], row[1], row[2]))
        num += 1
    print("-"*130)
    print("total: %d" %num)



if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "create":
            createDB(cursor)
        elif sys.argv[1] == "print":
            printDB(cursor)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "sql":
            cursor.execute(sys.argv[2])
            connection.commit()
    else:
        print("create or print or sql")

