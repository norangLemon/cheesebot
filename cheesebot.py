#-*- coding: utf-8 -*-
import socket, ssl, re
from setting import *
from IRCMessage import *

def send_msg(channel, msg):
    irc.send(bytes('PRIVMSG ' + channel + ' :' + msg + '\n', UTF8))

def pong():
    irc.send(bytes("PONG :pingpong\n"))

def join(channel, msg):
    irc.send(bytes("JOIN %s\r\n" %channel, UTF8))
    send_msg(channel, msg)

def run():
    while 1:
        ircmsg_raw = irc.recv(8192).decode(UTF8)
        ircmsg_raw = ircmsg_raw.strip("\n\r")
        print (ircmsg_raw)

        if ircmsg_raw.find("PING :") != -1:
            pong()
            continue
        
        if ircmsg_raw[0] != ':':
            continue
        msg = IRCMessage(ircmsg_raw)
        print(msg)
        
        if msg.msgType == "INVITE":
            join(msg.channel)
            send_msg(msg.channel, MSG_ENTER)
        
        elif msg.msgType == "MODE":
            if msg.msg == "+o " + NICK:
                send_msg(msg.channel, MSG_OP)
            elif msg.msg == "-o " + NICK:
                send_msg(msg.channel, MSG_DEOP)
        elif msg.msgType == "PRIVMSG":
            if msg.msg == NICK + " 살아있니?":
                send_msg(msg.channel, MSG_YES)

            elif msg.msg.find("참치") != -1:
                send_msg(msg.channel, MSG_INTEREST)

            elif msg.msg == "쓰담쓰담":
                send_msg(msg.channel, MSG_SATISFYING)

            elif msg.msg == "멍멍":
                send_msg(msg.channel, MSG_HATE)



irc_raw = socket.socket()
irc_raw.connect((HOST, PORT))
irc = ssl.wrap_socket(irc_raw)
irc.send(bytes("NICK " + NICK + "\r\n", UTF8))
irc.send(bytes("USER %s %s %s : %s\r\n" %(ID, ID, HOST, ID), UTF8))

join(CHANNEL, MSG_ENTER)
run()
