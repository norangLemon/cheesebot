import logging
import logging.handlers
import datetime

logger = logging.getLogger('CheeseLoger')
fileHandler = logging.FileHandler('logs/%s.log' 
        %datetime.datetime.today().strftime("%y-%m-%d"))
streamHandler = logging.StreamHandler()

formatter = logging.Formatter('[%(filename)s: %(lineno)s]<%(levelname)s> %(asctime)s\n\t%(message)s')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.setLevel(logging.DEBUG)
def prtInfo(text):
    logger.info(text)

def prtErr(text):
    logger.error(text)

def prtLog(text):
    logger.debug(text)

