#!/usr/bin/python3

import os
import time
from Menutask import menu
from Localtask import Local
from Remotetask import Remote

#로그인 관련 옵션
def login(option,intyper):
	if option == '0':
		input_type()
		
	os.system("clear")	
	logi = input("""\nSelect Login Type:
로컬 로그인 (press:'ll')
원격 로그인 (press:'rl')
'back'을 입력하시면 메인메뉴로 돌아갑니다.
:""")
		
	if option == 'remote': #원격 사용자 접속만 허용한다면
		Remote(option)
		
	else:
		if logi == 'll': #로컬 로그인
			os.system("clear")
			print("Login type: LOCAL")
			Local(option)
	
		elif logi == 'rl': #원격 로그인
			os.system("clear")
			print("Login type: LOCAL")
			Remote(option)
		
	option,intyper = menu(intyper)	#이전 메뉴로 돌아갈 시 사용할 인자
	login(option,intyper)
	
	
			
#메인 메뉴	
def input_type():
	os.system("clear")
	print(20*"-"+"Welcome to Menu Program"+"-"*20)
	intype = input("""\nChoose Input type:
1. Keyboard (Press 1 or Type 'keyboard')
2. Voice (Press 2 or Type 'voice')
Type 'exit' to exit
:""")


	if intype == '1' or intype == 'keyboard':
		option,intyper = menu('keyboard')#이전으로 돌아가고 싶다면..
		if option == '0':
			input_type()
		else:	
			login(option,intyper) #로그인 메서드로 넘어감
		
	elif intype == '2' or intype == 'voice':
		option,intyper = menu('voice')#메뉴를 불러오고 전 단계로 진입	
		if option == '0':
			input_type()
		else:
			login(option,intyper) #로그인 메서드로 넘어감.
	elif intype == 'exit' or intype == 'Exit' or intype == 'EXIT':
		print("BYE~")
		exit()
			
	else:
		print("Invalid input selection")	
		exit()
		
#main: 스크립트가 구동되는 첫 위치.
input_type() #input_type() 메서드 불러와 구동.
