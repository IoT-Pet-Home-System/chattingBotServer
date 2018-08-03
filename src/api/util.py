'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from api.config import url

PUSH_URL = "https://gw.talk.naver.com/chatbot/v1/event"
UPDATE_URL = "https://gw.talk.naver.com/chatbot/v1/imageUpload HTTP/1.1"

IMAGE_URL = url.SERVER_URL + 'download/'
REGIST_URL = url.SERVER_URL + 'signup/'

OEPN_EVENT = "open"
LEAVE_EVENT = "leave"
FRIEND_EVENT = "friend"
ECHO_EVENT = "echo"
SEND_EVENT = "send"
TYPING_TYPE = "typing"

def getSerial(str):
    return str.split(':')[1].replace(' ', '')