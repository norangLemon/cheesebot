import re
from setting import *

class Message:
    ID = None
    nick = None
    channel = None
    msg = None
    msgType = None
    target = None

    def __init__(self, origMsg):
        parse = re.search('^(?:[:](\S+)!~?(\S+) )?(\S+)(?: (?!:)(.+?))?(?: [:](.+))?$', origMsg)
        if parse:
            self.msgType = parse.group(3)
            if self.msgType == 'PING':
                self.ID = parse.group(5)
            elif self.msgType == 'JOIN':
                self.ID = parse.group(2)
                self.channel = parse.group(5)
            elif self.msgType == 'MODE':
                self.nick = parse.group(1)
                self.ID = parse.group(2)
                self.channel = parse.group(4).split(' ', maxsplit = 1)[0]
                self.msg = parse.group(4).split(' ', maxsplit = 1)[1]
            elif self.msgType == 'INVITE':
                self.nick = parse.group(1)
                self.ID = parse.group(2)
                self.target = parse.group(4)
                self.channel = parse.group(5)
            elif self.msgType == 'PRIVMSG':
                self.nick = parse.group(1)
                self.ID = parse.group(2)
                self.channel = parse.group(4)
                self.msg = parse.group(5)
                if self.ID == ID_BYB_BOT:
                    byb_parse = re.match('< (.+)> (.+)', self.msg)
                    if byb_parse:
                        self.nick = byb_parse.group(1)
                        self.msg = byb_parse.group(2)
            else:
                pass

    def __repr__(self):
        return ('Message<type: %s chan: %s ID: %s nick: %s target: %s>'
                    %(self.msgType, self.channel, self.ID, self.nick, self.target))

    def __str__(self):
        return ('Message<type: %s chan: %s ID: %s nick: %s target: %s>'
                    %(self.msgType, self.channel, self.ID, self.nick, self.target))

