import random
from setting import *

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

def howMuchLoveMsg(msg, affection):
    if affection > MAX_AFFECTION * 4/5:
        list = [msg.nick+"님 엄청 좋아한다냥!", "당연히 최고 좋아한다냥!", "냐앙..(부끄)//ㅅ//"]
    elif affection > MAX_AFFECTION *1/3:
        list = ["헤헤.. "+msg.nick+"님이랑 나랑은 꽤 친하지요냥?", "우웅.. 참치 다음으로 좋아한다냥!>ㅅ<"]
    elif affection > MAX_AFFECTION * 1/4:
        list = ["비밀이다냥!>ㅅ<", msg.name+"님은 좋은 사람이다냥! 그치만 좀 더 놀아주면 좋겠다냥!"]
    elif affection > MAX_AFFECTION* 1/5:
        list = ["좀 더 친해졌으면 좋겠다냥!", "냐아웅!ㅇㅅㅇ","헤에?ㅇㅅㅇ?"]
    elif affection >MIN_AFFECTION * 1/5:
        list = ["오늘 처음 본 거 같은데냥...?", msg.nick+"님이랑 나랑 아는 사이었냥..?", "좀 더 쓰다듬고 나서 물어봐달라냥!"]
    elif affection > MIN_AFFECTION *1/4:
        list = ["후웅..?", "히잉.. 솔직히 잘 모르겠다냥..."]
    elif affection > MIN_AFFECTION * 4/5:
        list = ["흥!",  msg.nick +"님한테는 지금 삐져있다냥!", "ㅡㅅㅡ..."]
    else:
        list = ["캬아아옹!", "우왜야아옹.. 또 괴롭히려고 그러냥!!", "히이잉..ㅠㅅㅠ", "와아앙! "+msg.nick+"님이 또 괴롭힌다냥!ㅠㅅㅠ"]
    return random.choice(list)
def randAnnoyedMsg(msg):
    list = ["자꾸 그러면 삐진다냥!", "귀찮게 하지 말라냐앙!", "히잉.. "+msg.nick+"님은 할 일도 없냥?!"]
    return random.choice(list)
