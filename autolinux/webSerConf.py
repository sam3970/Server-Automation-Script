#!/usr/bin/python3

import os

os.system("tput setaf 6");
os.system("yum install -y httpd");

os.system("tput setaf 2");
print("기본 웹 페이지 파일을 생성할까요?[y(생성)/n(서비스 시작)]");

os.system("read request");

    if request=='y':
        cd /var/www/html
        touch webpage.html
    else:
	print("웹서버 서비스가 시작되었습니다..");


os.system("tput setaf 6");
os.system("systemctl start httpd");

os.system("tput setaf 2");
print("웹서버 서비스가 시작되었지만 enable 상태가 아닙니다..");

os.system("tput setaf 7");
