'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
DB_NAME = "SystemData"
USER_TABLE_NAME = "naverUser"
SERIAL_TABLE_NAME = "homeSystem"
REQUEST_NAME = "request"
TEMPID_TABLE_NAME = "TempID"
SAVED_IMAGE_TABLE_NAME = "OldImageList"

USE_DB_QUERY = "use %s;" % (DB_NAME)

SUCESS_TO_REGIST = "등록 완료"
SUCESS_DEL_NO_REGISTERD_USER = "미등록 유저입니다. 모든 정보들이 삭제되었습니다"
SUCESS_DEL_REGISTERD_USER = "등록 시 넣은 정보들이 정상 삭제 되었습니다."

FAIL_TO_REGIST_USER = "사용자 등록에 실패하셨습니다. 이미 등록된 유저이거나 잘못된 시리얼 넘버입니다."