'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import threading

class Cache:
    def __init__(self):
        self.memory = {}
        self.sem_using = threading.Semaphore(1)  # 1명만 쓸것

    def memorization (self,key,val):
        self.sem_using.acquire()
        self.memory[key]= val
        self.sem_using.release()

    def dememorization (self,key):
        self.sem_using.acquire()
        if key in self.memory:
            item = self.memory[key]
            del(self.memory[key])
        else:
            item = False
        
        self.sem_using.release()
        return item
