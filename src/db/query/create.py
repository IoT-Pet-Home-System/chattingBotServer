'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from . import util

DB_QUERY = '''
create database %s
	DEFAULT CHARACTER
	SET utf8 collate utf8_general_ci;
    ''' % (util.DB_NAME)

USER_TABLE_QUERY = '''
create table %s (
	user_key varchar(50),
	serial varchar(50),
	Email varchar(100),
	petName varchar(50),
	primary key (user_key, serial)
		) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
		    ''' % (util.USER_TABLE_NAME)

TEMPID_TABLE_QUERY = '''
create table %s (
	user_key varchar(50),
	ID varchar(50),
	primary key (user_key, ID)
		) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
		''' %(util.TEMPID_TABLE_NAME)

SAVED_IMAGE_TABLE_QUERY = '''
create table %s (
	addr varchar(100),
	serial VARCHAR(50),
	primary key (addr)
		) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
''' %(util.SAVED_IMAGE_TABLE_NAME)


SERIAL_TABLE_QUERY = '''
create table %s(
	serial varchar(50),
	petCount int default 1, 
	primary key (serial)
	) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
			    ''' % (util.SERIAL_TABLE_NAME)

REQUEST_TABLE_QUERY = '''
create table %s(
	serial varchar(50),
	requestor varchar(50),
	request varchar(50),
	FOREIGN KEY (serial) REFERENCES %s (serial)
	) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
			    ''' % (util.REQUEST_NAME, util.SERIAL_TABLE_NAME)