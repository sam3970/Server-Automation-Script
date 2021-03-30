#!/usr/bin/python3

import os

os.system("tput setaf 5");
print("설치하려고 하는 패키지 이름을 입력 : \n\n\n");
 
os.system("read package");

os.system("yum install ${package}");
os.system("tput setaf 7");
