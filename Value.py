import random

def randJoinMsg(msg):
    list = ["안녕하세요냥!", "내가 왔다냥!", msg.nick+"님, 불러주셔서 고맙다냥!", ">ㅅ<냐옹!"]
    return random.choice(list)

def randPartMsg(msg):
    list = ["알았다냥..ㅠㅅㅠ", msg.nick+"님 나쁘다냥!ㅠㅠ", "냥무룩.. 잘있으라냥.."]
    return random.choice(list)

def randQuitMsg(msg):
    list = ["히잉.. 알았다냥..", "ㅜㅅㅠ다들 잘있으라냥!"]
    return random.choice(list)

def randNoQuitMsg(msg):
    list = ["난 주인님 말씀만 듣는다냥!", msg.nick+"님은 바보다냥!!"]
    return random.choice(list)

def randHateMsg(msg):
    list = ["캬옹!", "와아아옹!!!-ㅅ-", "냐아아!!=ㅅ="]
    return random.choice(list)

def randSatisfyMsg(msg):
    list = ["고릉고릉", "냐아.. 잠이 온다냥zZ", "냐아앙♡"]
    return random.choice(list)

def randTunaMsg(msg):
    list = ["!!", msg.nick+"님, 참치 주세요냥!!", "어디서 참치 소리를 들었다냥?!"]
    return random.choice(list)


def randOKMsg(msg):
    list = ["나 여기 있다요냥!", "그렇다냥!", msg.nick+", 나 찾았나요냥?"]
    return random.choice(list)

def randOPMsg(msg):
    list = [">ㅅ<", msg.nick+"님, 고맙다냥!", "부비적부비적♡"]
    return random.choice(list)

def randDEOPMsg(msg):
    list = [msg.nick+"님 미워! ㅠㅠ", "냥무룩...", "삐질꺼다냥ㅇㅅㅠ"]
    return random.choice(list)

def randCuriousMsg(msg):
    list = [msg.nick + "님, 뭐 한거냐요냥?", "냐아?", "내 이름을 본거 같은데냥?!"]
    return random.choice(list)


