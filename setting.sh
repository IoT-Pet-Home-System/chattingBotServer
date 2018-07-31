#!/usr/bin/env bash

DIR_PATH=`dirname $0`
AUTH_PATH=$DIR_PATH"/src/api/config/Authorization.py"
URL_PATH=$DIR_PATH"/src/api/config/url.py"
SSL_PATH=$DIR_PATH"/src/ssl/config.py"
DBCON_PATH=$DIR_PATH"/src/db/dbcon.py"

echo -e "\033[0;34mMade by \033[1;36mkuj0210, KeonHeeLee, seok8418 \033[1;34m"
echo -e "\033[0;34m- Github : \033[1;36mhttps://github.com/IoT-Pet-Home-System/chattingBotServer"
echo -e "\033[0;34m- E-mail : \033[1;36mbeta1360@naver.com\033[0m"
echo " "

echo -e "\033[1;36m1. Server Setting\033[0m"

echo -e "- Domain: \c"
read url

payload="SERVER_URL = \""$url"\""
echo $payload

if [ -e `ls $URL_PATH` ]; then
    rm -rf "$URL_PATH"
    touch "$URL_PATH"
    echo $payload >> "$URL_PATH"
else
    touch "$URL_PATH"
    echo $payload >> "$URL_PATH"
fi

echo -e "- SSL Certificate path: \c"
read cert

echo -e "- SSL Certificate key path: \c"
read cert_key

payload="cert = \"$cert\"\nkey = \"$cert_key\""

if [[ -e `ls $cert`] && [ -e `ls $cert_key` ]]; then
    if [ -e `ls $SSL_PATH` ]; then
        rm -rf "$SSL_PATH"
        touch "$SSL_PATH"
        echo -e $payload >> "$SSL_PATH"
    else
        touch "$SSL_PATH"
        echo -e $payload >> "$SSL_PATH"
    fi
else
    echo -e "\033[0;31m[Setting Error] SSL certificate does not exist.\033[0m"
    exit
fi
echo -e "\033[0;34m[SUCCESS] \033[1;36mRenew(Create) /api/config/url.py\033[0m"
echo -e "\033[0;34m[SUCCESS] \033[1;36mRenew(Create) /ssl/config.py\033[0m"

echo -e "\033[1;36m2. API Authorization setting\033[0m"

echo -e "- Authorization key: \c"
read auth_key

payload="key = \"$auth_key\""

if [ -e `ls $AUTH_PATH` ]; then
    rm -rf "$AUTH_PATH"
    touch "$AUTH_PATH"
    echo $payload >> "$AUTH_PATH"
else
    touch "$AUTH_PATH"
    echo $payload >> "$AUTH_PATH"
fi
echo -e "\033[0;34m[SUCCESS] \033[1;36mRenew(Create) /api/config/Authorization.py\033[0m"

echo -e "\033[1;36m3. Database Setting\033[0m"

echo -e "- host: \c"
read db_host

echo -e "- user: \c"
read db_user

echo -e "- password: \c"
read -s db_pwd

payload="host = \"$db_host\"\nuser = \"$db_user\"\npassword = \"$db_pwd\"\ncharset = \"utf8\""

if [ -e `ls $DBCON_PATH` ]; then
    rm -rf "$DBCON_PATH"
    touch "$DBCON_PATH"
    echo -e $payload >> "$DBCON_PATH"
else
    touch "$DBCON_PATH"
    echo -e $payload >> "$DBCON_PATH"
fi

echo -e "\033[0;34m[SUCCESS] \033[1;36mRenew(Create) /db/dbcon.py\033[0m"
echo -e "\033[0;34mIoT-Pet-Home-System's Chatting Server Setting is complete!!\033[0m"
