# <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/docs/repo/chatbot_image/chatbot%20image.jpg?raw=true" width="70">IoT-Pet-Home-System : ChattingBot Server

 This server is main part of this system. For example, it not only recieve and send payload related to Naver-talktalk 
messenger API from client, but also analyze nature language(Korean), receive pet-home's requests and send the pet-home's works.

## Full System Reference
- [Go To Main-Repository](https://github.com/kuj0210/IoT-Pet-Home-System)

## Requirement

### 1. Modules

- **openjdk-7-jdk** : KoNLPy package request JVM.
- **g++** : KoNLPy package request this.
- **Python3** : It is required to solve utf-8 issues and packages.
- **MySQL** : This system use this database.

### 2. Environment

- **Public IP** : This server must have public IP(to handle API server & support cloud).
- **HTTPS** : This server only support on HTTPS protocol environment.

## Dependency

- flask
- KoNLPy
- requests
- PyMySQL

## Installation

### 1. Requirement(modules)

```bash
$ sudo apt-get update
$ sudo apt-get install mysql-server
$ sudo apt-get install g++ openjdk-7-jdk
$ sudo apt-get install python3-dev
$ sudo apt-get install git # If you don't install it...
```

### 2. Dependency

- Case::**Python3**
```bash
$ pip3 install flask
$ pip3 install konlpy
$ pip3 install requests
$ pip3 install pymysql
```

### 3. Clone this repository

```bash
$ git clone https://github.com/IoT-Pet-Home-System/chattingBotServer
```

## Usage

- Setting Configuration

```bash
$ sudo chmod +0777 setting.sh
$ ./setting.sh
```

- Run

```bash
$ cd src  #In this repository's root directory
$ sudo python3 server.py
```

## Introduce Internal Modules

- **api** : This module handle NaverTalkTalk(Web application messenger used by this system) API payload.
- **auth** : This module manage authentication related to sign up and issue temporary ID for registration step. 
- **db** : This module handle database and data related to this system.
- **memo** : This module memorize cache related a images recieving from pet-homes and if this cache isn't unecessary, this module delete it.
- **nl** : This module analyze Nature Language(Korean) and pick main keyword for operating each pet-homes or replying to user.
- **reply** : This module manage of reply messages to send user.
- **static & template** : This module manage html template, script source codes(Javascript), css and favicon. Specially, this system refer about user registration form.
- **test** : You can test this system, to use this module.
- **server.py** : Main part of this system. It recieve and send payloads with HTTPS to client.

## DB Explanation and Membership Management

### DB Explanation

This system include 1 database and 5 tables. Below tables is them. <br/>
Main database is ```SystemData``` and this database include below 5 tables.

- **naverUser**

```sql
user_key varchar(50) primary key,
serial varchar(50) primary key,
Email varchar(100),
petName varchar(50)
```

 This table is used to manage user data related to regist this system. UserKey and Serial is used to search another keys or tuples.
 
 - **TempID**
 
 ```sql
user_key varchar(50) primary key,
ID varchar(50) primary key
 ```
 
  This table is used to temporarily manage user_key. But user related on this table isn't this system's user, accordingly this user's 
  information isn't registed in naverUser table. If you regist in this system, this table's tuple will be deleted.
  
  - **OldImageList**
  
  ```sql
addr varchar(100) primary key,
serial VARCHAR(50)
  ```
  
This table stores the image received from "Pet Home System" and saves the path. When a new image comes in, it looks for the old image, deletes the file, and saves the path to the new image file.
 
 - **homeSystem**
 
 ```sql
serial varchar(50) primary key,
petCount int default 1
 ```

 This table is used to manage pet-home's information. Specially serial is very important to use or search other data.
 
 - **request**
 
 ```sql
serial varchar(50),
requestor varchar(50),
request varchar(50),
FOREIGN KEY (serial) REFERENCES homeSystem (serial)
 ```
 
 This table is used to manage pet-home's request list. If a user(registed user) request any operation(s), this server will save it.
After a pet-home request to its works in database, server will send this list and delete this tuple. This tuple is pet-home's works.


## Membership Management

The step of user registration is below steps.

1. User must write a keyword;```등록``` in messager app(NaverTalkTalk).
2. A user-Key of user writting keyword ```등록``` and temporary ID that created by IDissuance module is registed in TempID table.
3. This server send a link ```https://url/signup/<temporary-ID>```that created by auth module and reply module.
4. If the user click this link, user registration form will be shown. User will fill this form.
5. If the user send form, this server check this user's temporary ID and start the step of registration.
6. In step of registration, this server delete ```TempID``` tuple that exist the temporary ID.
7. In next step, this server add the data of registration form in ```naverUser``` table and ```homeSystem``` table.


## Note

 - Apply from public IP to HTTPS
   1. [AWS EC2 setting guide](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/AWS_EC2_setting.md)
   2. [Domain setting description](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/Domain_setting.md)
   3. [How to use SSL Certificates and apply HTTPS](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/.README/Notes/How_to_use_SSL_Certificates_and_apply_HTTPS.md)


## CONTRIBUTING

Contributing on our repository is very thanks, and welcome!<br>
If you want to contact us, please send below mail.<br>

- KeonHeeLee ([chattingBotServer](https://github.com/IoT-Pet-Home-System/chattingBotServer))
  - beta1360@naver.com
  - beta1360sh@gmail.com
  
- kuj0210 ([All management](https://github.com/kuj0210/IoT-Pet-Home-System))
  - on_11@naver.com
  
- seok8418 ([petHomeSystem](https://github.com/IoT-Pet-Home-System/petHomeSystem))
  - seok8418@nate.com


## LICENSE

IoT-Pet-Home-System's main-server is licensed under [the GNU GENERAL PUBLIC LICENSE v3](./LICENSE).
 
 ```
 Copyright (C) 2017-present, kuj0210, KeonHeeLee, seok8418

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
