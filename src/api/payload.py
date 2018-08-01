'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
def getImageBox(user, url):
    return {
        "event": "send",
        "user": user,

        "compositeContent": {
            "compositeList": [{
                "title": "펫홈사진",
                "description": "요청하신 사진입니다",
                "image": {
                    "imageUrl": url
                }
            }]
        }
    }

def getUpdateBox(url):
    return {"imageUrl": url}

def getPostBodyMessage(user, text):
    return {
        "event": "send",
        "user": user,
        "textContent": {
            "text": text
        },
        "options": {
            "notification": "true"
        }
    }

def getPostPushMessage(user, text):
    return {
        "event": "send",
        "user": user,
        "textContent": {
            "text": text
        }
    }

def ImageJson(user, URL):
    return {
        "event": "send",
        "user": user,
        "imageUrl": URL
    }
