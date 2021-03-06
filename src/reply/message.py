'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
OPEN_MSG = """
        안녕하세요!!! IoT-Pet-Home-System 시스템입니다.
        무엇을 도와드릴까요?
        """
LEAVE_MSG = "나중에 또봐요~ :)"
SUCESS_RECEVIED_MSG = " 기능이 접수완료 되었습니다."

# for friend EV
ON_FRIEND_MSG = "안녕하세요! IoT-Pet-Home-System이에요! 친구가 되서 반가워요"
OFF_FRIEND_MSG = "더는 친구가 아니게 되었네요... 즐거웠어요"

# for regist EV
SUCESS_IST_USER = "등록 완료"
SUCESS_DEL_NO_REGISTERD_USER = "미등록 유저입니다. 모든 정보들이 삭제되었습니다"
SUCESS_DEL_REGISTERD_USER = "등록 시 넣은 정보들이 정상 삭제 되었습니다."
SUCCESS_TO_REGIST = "사용자 등록이 완료되었습니다! 환영합니다!"

# for help EV
HOW_TO_USE = '''info [주어]: 온도,습도,먼지,공기,방,상황 [동사]알려[가중치] 모두다
feed [주어]: 먹이,사료,먹을것,밥 [동사]줘,급여,배식,먹 [가중치] 모두다
water [주어]: 마실,음료,물 [동사]배식,급여,주다,먹 [가중치] 모두다
door [주어]: 문,입구 [동사]열,오픈,개방 [가중치] 모두다
camera [주어]: 사진,상황,모습,얼굴,현황 [동사]보여주,찍,알려 [가중치] 모두다
howToUse 도움말
regist 등록 : serial (ex) 등록:SR_1452
'''

def feedOperationMsg(name, time):
    return name + "에게 밥을 안준지 "+ str(time)+ "시간이 지났어요. 배고프지 않을까요?"

def doorOperationMsg(name, time):
    return name+"의 집을 안 열어준지 "+str(time)+"시간이 지났어요. 답답해 할 것 같아요."

def operationPushMSG(name, request):
    msg = ""
    list = request["push_list"]

    for item in list:
        if item["operation"] == "door":
            msg = doorOperationMsg(name, item["time"])

        elif item["operation"] == "feed":
            if msg != "": msg = msg + "\n"
            msg = msg + feedOperationMsg(name, item["time"])

    return msg
