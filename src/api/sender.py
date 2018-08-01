'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import requests, json
from src.api.config import Authorization
from . import util, payload

def sendPush(url, user, msg):
    header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": Authorization.key }
    requests.post(url=url, headers=header, data=json.dumps(payload.getPostPushMessage(user, msg)))

def upLoad(url):
    header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": Authorization.key }
    requests.post(url=util.UPDATE_URL, headers=header, data=json.dumps(payload.getUpdateBox(url)))

def sendIMAG(user, URL):
    header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": Authorization.key }
    requests.post(url=util.PUSH_URL, headers=header, data=json.dumps(payload.getImageBox(user, URL)))
