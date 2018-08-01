'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from . import util

def petCountBySerial(petCount, serial):
    return "UPDATE %s SET %s.petCount=%d WHERE %s.serial = \'%s\';" %(
    util.SERIAL_TABLE_NAME, util.SERIAL_TABLE_NAME, petCount, util.SERIAL_TABLE_NAME, serial)