import redis

r = redis.Redis('localhost', decode_responses=True)
dbKeyPrefix = "cheese-bot-"

def getChanList():
    return r.hgetall(dbKeyPrefix+"channel-list")

def addChanList(chan, key = ""):
    r.hset(dbKeyPrefix+"channel-list", chan, key)

def removeChanList(chan):
    r.hdel(dbKeyPrefix+"channel-list", chan)
