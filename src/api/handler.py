'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from db import Register
from nl import usecase_finder
from reply import message, exception

from auth import IDissuance
from . import util, payload

class Handler:
    def __init__(self):
        self.regist = Register.Register()
        self.IDI = IDissuance.IDIssuance()

    def eventHandler(self, infomationFromNaverTalk):
        sendMSG = "None"
        user = infomationFromNaverTalk["user"]
        if infomationFromNaverTalk["event"] == util.OEPN_EVENT:
            sendMSG = message.OPEN_MSG

        elif infomationFromNaverTalk["event"] == util.LEAVE_EVENT:
            sendMSG = message.LEAVE_MSG

        elif infomationFromNaverTalk["event"] == util.FRIEND_EVENT:
            if infomationFromNaverTalk["state"] == "on":
                sendMSG = message.ON_FRIEND_MSG
            else:
                self.regist.insertUserRequest(user, "UPDATE")
                sendMSG = message.OFF_FRIEND_MSG + "\n" + self.regist.deleteUserData(user)

        elif infomationFromNaverTalk["event"] == util.ECHO_EVENT:
            return "Echo"

        elif infomationFromNaverTalk["event"] == util.SEND_EVENT \
                and infomationFromNaverTalk["typing"] == util.TYPING_TYPE:
            sendMSG = self.handlerForSendEvent(user, infomationFromNaverTalk["message"])
        else:
            sendMSG = exception.UNSUPPORTED_TYPE_COMMAND

        postBodyMessage = payload.getPostBodyMessage(user, sendMSG)
        return postBodyMessage

    def handlerForSendEvent(self,user,msg):
            #finder setting
        usecaseFinder = usecase_finder.UsecaseFinder()
        usecaseFinder.setUserSetting()
        requestlist=usecaseFinder.analyzeSentence(msg)

        if "howToUse" in requestlist:
            print("도움 ")
            smsg = message.HOW_TO_USE
            return smsg

        elif "regist" in requestlist:
            id = self.IDI.getTempID(user)
            if self.regist.insertTempID(user, id) == False:
                return exception.REGISTERD_USER
            return "아래의 사용자 등록 폼에 따라 등록을 해주세요.\n"+util.REGIST_URL+id

        else :
            res=self.regist.insertUserRequest(user," ".join(requestlist))
            if len(requestlist) == 0:
                return exception.UNKNOWN_COMMAND

            #2 리퀘스트에 해당 시리얼 넣음
            return " ".join(requestlist)+res

    def getDataFromNaverTalk(self, dataFromMessenger):
        user = dataFromMessenger["user"]
        event = dataFromMessenger["event"]
        dicForSaveUserData = {"user": user, "event": event}

        if event != util.FRIEND_EVENT:
            dicForSaveUserData["typing"] = dataFromMessenger["textContent"]["inputType"]
            if dicForSaveUserData["typing"] == "typing":
                dicForSaveUserData["message"] = dataFromMessenger["textContent"]["text"]

        if "options" in dataFromMessenger and "set" in dataFromMessenger["options"]:
            dicForSaveUserData["state"] = dataFromMessenger["options"]["set"]

        return dicForSaveUserData

if __name__ == "__main__":
    h = Handler()
    h.eventHandler({'user':'test','event':'send',"typing":"typing","message": {"text": "안냥"
        }})

