#-*- coding: utf-8 -*-
import socket, ssl, re
from setting import *

def send_msg(channel, msg):
    irc.send('PRIVMSG ' + chan + ' :' + msg + '\n')

def pong():
    irc.send("PONG :pingpong\n")

def join(channel, msg):
    irc.send(bytes("JOIN %s\r\n" %channel, UTF8))
    send_msg(jannel, msg)

def run():
    while 1:
        ircmsg_raw = irc.recv(8192).strip("\n\r")decode(UTF8)
        print (ircmsg_raw)

        if ircmsg.find("PING :") != -1:
            pong()
            continue
        
        if ircmsg_raw[0] != ':':
            continue
        msg = IRCMessage(ircmsg_raw)
        print(msg)

        if msg.msgType == "PRIVMSG":
            if msg.msg == NICK + " 살아있니?":
                send_msg(msg.channel, MSG_YES)

irc_raw = socket.socket()
irc_raw.connect((HOST, PORT))
irc = ssl.wrap_socket(irc_raw)
irc.send(bytes("NICK " + NICK + "\r\n", UTF8))
irc.send(bytes("USER %s %s %s : %s\r\n" %(ID, ID, HOST, ID), UTF8))

join(CHANNEL, MSG_ENTER)
run()
