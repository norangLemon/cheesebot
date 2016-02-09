#-*- coding: utf-8 -*-
import socket, ssl, re
import Value
from setting import *
from Message import *

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

def quit(channel, txt):
    send_msg(channel, txt)
    irc.send(bytes("QUIT\r\n", UTF8))


def react_invite(msg):
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
    send_msg(msg.channel, Value.randOKMsg(msg))

def react_tuna(msg):
    send_msg(msg.channel, Value.randTunaMsg(msg))

def react_goAaway(msg):
    part(msg.channel, Value.randPartMsg(msg))

def react_loveU(msg):
    send_msg(msg.channel, Value.randSatisfyMsg(msg))
    
def react_dog(msg):
    send_msg(msg.channel, Value.randHateMsg(msg))

def react_sleep(msg):
    if msg.ID == ID_NORANG:
        quit(msg.channel, Value.randQuitMsg(msg))
    else:
        send_msg(msg.channel, Value.randNoQuitMsg(msg))

def run():
    while 1:
        ircmsg_raw = irc.recv(8192).decode(UTF8)
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
            elif msg.msg.find("참치") != -1:
                react_tuna(msg)

            elif msg.msg == "쓰담쓰담":
                react_loveU(msg)

            elif msg.msg == "멍멍":
                react_dog(msg)

            elif msg.msg == NICK + ", 자러 갈 시간이야":
                react_sleep(msg)

        else:
            print(msg)
                



irc_raw = socket.socket()
irc_raw.connect((HOST, PORT))
irc = ssl.wrap_socket(irc_raw)
irc.send(bytes("NICK " + NICK + "\r\n", UTF8))
irc.send(bytes("USER %s %s %s : %s\r\n" %(ID, ID, HOST, ID), UTF8))
print("연결되었습니다.")
join(CHANNEL, "일어났다!")

run()
