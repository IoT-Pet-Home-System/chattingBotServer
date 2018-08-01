#-*-coding: utf-8-*-
import requests, unittest, json
from flask import Flask
from flask_testing import LiveServerTestCase

send_url= "http://localhost:8000/"
header = {"Content-Type": "application/json;charset=UTF-8"}

payload = {
    "event":"send",
    "user":"testcase-ChatbotServer",
    "textContent":{
        "text": "등록",
        "inputType":"typing"
    },
    "options":{
        "notification": True
    }
}



class ServerTest(LiveServerTestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING']=True
        app.config['LIVESERVER_PORT']=8080
        app.config['LIVESERVER_TIMEOUT']=5
        self.SIGNUP_URL = None
        return app

    def test_send_payload(self):
        res = requests.post(url=send_url, headers=header, data=json.dumps(payload))
        self.SIGNUP_URL = res.json()["textContent"]["text"]
        print(self.SIGNUP_URL)
        self.assertEqual(res.status_code, 200)

    def test_get_url(self):
        res = requests.get(url=self.SIGNUP_URL, headers={'Accept-Encoding': 'utf-8'})
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()