#-*-coding: utf-8-*-
'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from flask import Flask,request,jsonify,send_from_directory, render_template
from flask_sslify import SSLify

from file.sr_image import imageIO, initDir
from file.cache import Cache
from nl import usecase_finder
from api.handler import Handler
from api import sender, util
from auth.signup import *
from ssl_config import config
from device.pethome import Pethome

from reply import message, exception

THusecaseFinder = usecase_finder.UsecaseFinder()
UPLOAD_FOLDER = 'uploaded'
initDir('uploaded')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sslfy =SSLify(app, permanent=True)
Memo = Cache()

@app.route("/",methods=["POST"])
def naver_Servermain():
    # make manager
    Manager = Handler()

    # get data from naver  talk talk
    dataFromMessenger =request.get_json()# get json data from naver talk talk
    infomationFromNaverTalk=Manager.getDataFromNaverTalk(dataFromMessenger) # it is process for data sorting
    postBodyMessage = Manager.eventHandler(infomationFromNaverTalk) # process event

    if postBodyMessage == "ECHO": return
    return jsonify(postBodyMessage), 200

@app.route("/bootUp",methods=["POST"])
def bootUpMobile():
    pethome = Pethome()
    return pethome.bootUp(request)

@app.route("/RQST",methods=["POST"])
def passRequest():
    pethome = Pethome()
    return pethome.sendRequest(request)
 
@app.route("/push",methods=["POST"])
def pushResult():
    pethome = Pethome()
    return pethome.push(request)

@app.route("/operation", methods=["POST"])
def operationPush():
    pethome = Pethome()
    return pethome.sendOperationPush(request), 200
 
@app.route("/<user>/image",methods=["POST",'GET'])
def image(user):
    path = app.config['UPLOAD_FOLDER']
    return imageIO(request, user, Memo, path)

#파일전송
@app.route('/download/<filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

#로그인
@app.route('/signup/<temp_user_key>', methods=['GET','POST'])
def sign_up(temp_user_key):
    regist = Register()
    if request.method == 'GET':
        return render_template('regist.html')

    else: # request.method == 'POST':
        user_key, is_registed = sigup(temp_user_key=temp_user_key, form=request.form)
        regist.insertUserRequest(user_key, "UPDATE")
        if is_registed:
            sender.sendPush(url=util.PUSH_URL, user=user_key, msg=message.SUCCESS_TO_REGIST)
            return render_template("regist_success.html"), 200
        else:
            sender.sendPush(url=util.PUSH_URL, user=user_key, msg=exception.FAIL_TO_REGIST_USER)
            return render_template("regist_fail.html"), 200

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template("error404.html"), 404

@app.errorhandler(405)
def not_allow_method(error):
    app.logger.error(error)
    return render_template("error405.html"), 405

if __name__ == "__main__":
    contextSSL = (config.cert, config.key)
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)
