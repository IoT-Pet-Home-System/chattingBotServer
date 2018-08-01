import requests, unittest
from flask import Flask
from flask_testing import LiveServerTestCase

class ServerTest(LiveServerTestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING']=True
        app.config['LIVESERVER_PORT']=8080
        app.config['LIVESERVER_TIMEOUT']=5
        return app

    def test_404_error(self):
        # Forbidden URL
        response = requests.get(url="http://localhost:8000/random")
        self.assertEqual(response.status_code, 404)

    def test_500_error(self):
        # Send body that it is empty.
        response = requests.post(url="http://localhost:8000/")
        self.assertEqual(response.status_code, 500)

if __name__ == "__main__":
    unittest.main()