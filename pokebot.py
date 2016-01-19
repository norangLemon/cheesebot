#-*- coding: utf-8 -*-
import socket, ssl, re
from setting import *

irc_raw = socket.socket()
irc_raw.connect((HOST, PORT))
irc = ssl.wrap_socket(irc_raw)
irc.send(bytes("NICK " + NICK + "\r\n", UTF8))
irc.send(bytes("USER %s %s %s : %s\r\n" %(ID, ID, HOST, ID), UTF8))

def send_msg(channel, msg):
    ircsock.send('PRIVMSG ' + chan + ' :' + msg + '\n')

