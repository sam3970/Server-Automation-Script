#!/usr/bin/python3

import os

def Local(comin):
	if comin == 'Linux-cal':
		os.system("python3 calendar.py");

	elif comin == 'Linux-date':
		os.system("python3 Ldate.py");

	elif comin == 'Linux-HDD':
		os.system("python3 HDDDetails.py");

	elif comin == 'Linux-yumC':
		os.system("python3 yumConf.py");

	elif comin == 'Linux-install':
		os.system("python3 InsSW.py");

	elif comin == 'Linux-webC':
		os.system("python3 webSerConf.py");

	elif comin == 'Linux-diskP':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-pullI':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-runC':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-stopC':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-startC':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-renameC':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-rmC':
		os.system("echo 작업 진행중..");

	elif comin == 'docker-rmI':
		os.system("echo 작업 진행중..");

	elif comin == 'clear':
                os.system("clear");
