import re
from setting import *


class IRCMessage():
    msgType = None
    sender = None
    channel = None
    msg = None
    target = None
    nick = None

    def __init__(self, origMessage):
        parse = re.search('^(?:[:](\S+)!~?(\S+) )?(\S+)(?: (?!:)(.+?))?(?: [:](.+))?$', origMessage)
        if parse:
            self.msgType = parse.group(3)
            
            if self.msgType == 'PING':
                self.sender = parse.group(5)
            elif self.msgType == 'INVITE':
                self.nick = parse.group(1)
                self.sender = parse.group(2)
                self.target = parse.group(4)
                self.channel = parse.group(5)
            elif self.msgType == 'PRIVMSG':
                self.sender = parse.group(2)
                self.channel = parse.group(4)
                self.msg = parse.group(5)
                self.nick = parse.group(1)
                if self.sender == SENDER_BYB_BOT:
                    byb_parse = re.match('< (.+)> (.+)', self.msg)
                    if byb_parse:
                        self.msg = byb_parse.group(2)
                        self.nick = byb_parse.group(1)
            elif self.msgType == 'MODE':
                self.nick = parse.group(1)
                self.sender = parse.group(2)
                self.channel = parse.group(4).split(' ', maxsplit=1)[0]
                self.msg = parse.group(4).split(' ', maxsplit=1)[1]
            elif self.msgType == 'JOIN':
                self.sender = parse.group(2)
                self.channel = parse.group(5)
        else:
            pass

    def __repr__(self):
        msg = self.msg
        return '<IRCMessage : %s %s %s %s %s %s>' \
               % (self.msgType, self.sender, self.nick, self.channel, msg, self.target)

    def isValid(self):
        if self.msgType == None:
            return False
        else:
            return True
