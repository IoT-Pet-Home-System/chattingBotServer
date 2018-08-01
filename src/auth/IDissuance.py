'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import time

class IDIssuance:
    def getTempID(self, userKey):
        if len(userKey) <= 6 or userKey == None:
            raise Exception('Too Short String, Please enter at least 6 digits of text.')

        Tid = ""
        Charlist = list(userKey)
        alph = 0
        limit = len(Charlist)
        for cnt in range(limit):
            item = Charlist.pop(0)
            alph += ord(item)
            if (cnt != 0 and cnt % 2 == 0) or range(len(Charlist)) == 0:
                Tid += chr(alph % 26 + 65)
                alph = 0
        sec = time.localtime().tm_sec
        return Tid + str(sec)


if __name__ == "__main__":
    TID = IDIssuance()
    UK = "a4ffge51ff6g756e"
    print("input = " + UK)
    tid = TID.getTempID(UK)
    print("output = " + tid)

    UK = "a231"
    print("input = " + UK)
    tid = TID.getTempID(UK)
    print("output = " + tid)