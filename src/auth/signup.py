'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from db.Register import Register
from reply import exception

def sigup(temp_user_key, form):
    register = Register()

    user_key = register.getUserKeyByTempID(tempID=temp_user_key)
    if user_key == None:
        return user_key, False

    if register.insertUserData(
            user_key=user_key, email=form['email'],
            serial=form['serial'], petname=form['petname']) \
            == exception.DONT_REGIST:
        return user_key, False

    if register.updatePetCount(user_key=user_key, petCount=form['pet_num']) == False:
        return user_key, False

    if register.deleteTempID(tempID=temp_user_key) == False:
        return user_key, False

    return user_key, True