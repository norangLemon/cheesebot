#-*- coding: utf-8 -*-
import socket, ssl, re
import Value
from setting import *
from Message import *
from Log import *

def send_msg(channel, txt):
    irc.send(bytes('PRIVMSG ' + channel + ' :' + txt + '\n', UTF8))

def pong():
    irc.send(bytes("PONG :pingpong\n", UTF8))

def join(channel, txt):
    irc.send(bytes("JOIN %s\r\n" %channel, UTF8))
    send_msg(channel, txt)

def part(channel, txt):
    send_msg(channel, txt)
    irc.send(bytes("PART %s\r\n" %channel, UTF8))

def quit(txt):
    irc.send(bytes("QUIT\r\n", UTF8))

def react_part(msg):
    prtLog("part: "+msg.nick)
    part(msg.channel, Value.randPartMsg(msg))

def react_invite(msg):
    prtLog(msg)
    prtLog("invite"+msg.nick)
    if msg.channel == "#norang":
        irc.send(bytes("JOIN %s\r\n" %msg.channel, UTF8))
    send_msg(msg.channel, Value.randJoinMsg(msg))

def react_mode(msg):
    if msg.msg == "+o " + NICK:
        send_msg(msg.channel, Value.randOPMsg(msg))
    elif msg.msg == "-o " + NICK:
        send_msg(msg.channel, Value.randDEOPMsg(msg))
    elif msg.msg.find(NICK) != -1:
        send_msg(msg.channel, Value.randCuriousMsg(msg))

def react_RUOK(msg):
    prtLog("RUOK: "+msg.nick)
    send_msg(msg.channel, Value.randOKMsg(msg))

def react_tuna(msg):
    send_msg(msg.channel, Value.randTunaMsg(msg))

def react_goAway(msg):
    prtLog("goAway: "+msg.nick)
    part(msg.channel, Value.randPartMsg(msg))

def react_loveU(msg):
    prtLog("pat: "+msg.nick)
    send_msg(msg.channel, Value.randSatisfyMsg(msg))
    
def react_dog(msg):
    prtLog("dog: "+msg.nick)
    send_msg(msg.channel, Value.randHateMsg(msg))

def react_sleep(msg):
    prtLog("sleep: "+msg.nick)
    if msg.ID == ID_NORANG:
        quit(msg.channel, Value.randQuitMsg(msg))
        return True
    else:
        send_msg(msg.channel, Value.randNoQuitMsg(msg))
        return False

def react_giveOp(msg):
    irc.send(bytes('MODE ' + msg.channel + ' +o ' + msg.nick + '\n', UTF8))
    send_msg(msg.channel, Value.randGiveOpMsg(msg))

def react_eating(msg):
    send_msg(msg.channel, Value.randEatingMsg(msg))
    
def run():
    while 1:
        try:
            ircmsg_raw = irc.recv(8192).decode(UTF8)
        except KeyboardInterrupt:
            quit("난 자러 간다냥!")
            prtLog("ctrl+c")
            return

        except UnicodeDecodeError as err:
            prtErr("Unicode Error!")
            prtLog(ircmsg_raw)
            prtErr(err)
            continue

        except:
            prtLog(ircmsg_raw)
            prtLog("?")
            continue

        ircmsg_raw = ircmsg_raw.strip("\n\r")
        
        if ircmsg_raw.find("PING :") != -1:
            pong()
            continue
        
        if ircmsg_raw[0] != ':':
            continue

        msg = Message(ircmsg_raw)
        
        if msg.msgType == "INVITE":
            react_invite(msg)
        elif msg.msgType == "MODE":
            react_mode(msg)
        elif msg.msgType == "PRIVMSG":
            if msg.msg == NICK + " 살아있니?":
                react_RUOK(msg)
            elif msg.msg == "돌아가!" or msg.msg == "사라져버려!":
                react_goAway(msg)
            elif msg.msg == NICK +"야 참치 먹자" or msg.msg == "참치 먹자" or msg.msg == NICK + ", 참치 먹자":
                react_eating(msg)
            elif msg.msg.find("참치") != -1:
                react_tuna(msg)

            elif msg.msg == "쓰담쓰담":
                react_loveU(msg)

            elif msg.msg == "멍멍":
                react_dog(msg)

            elif msg.msg == NICK + ", 자러 갈 시간이야":
                if react_sleep(msg):
                    return
            elif msg.msg == NICK + ", 옵줘" or msg.msg == NICK + "야 옵줘":
                react_giveOp(msg)

        else:
            prtLog(str(msg))
                
if __name__ == "__main__":
    irc_raw = socket.socket()
    irc_raw.connect((HOST, PORT))
    irc = ssl.wrap_socket(irc_raw)
    irc.send(bytes("NICK " + NICK + "\r\n", UTF8))
    irc.send(bytes("USER %s %s %s : %s\r\n" %(ID, ID, HOST, ID), UTF8))
    print("연결되었습니다.")
    join(CHAN, "일어났다!")
    run()
