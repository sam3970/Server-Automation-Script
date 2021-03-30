#!/usr/bin/python3

import os
from Inputtask import Keyboard
from Inputtask import Voice

#입력 후 해당하는 메뉴를 표시.
def menu(intype):

    print("\nInput Type:"+intype);
    menu_loop = True;

    while menu_loop:
        print(20*"-"+"메인 메뉴 화면"+"-"*20);
	print("실행할 명령어 입력                      |\tCommand");
		
	print("""------------------------------------------
Linux(리눅스)               |\tLinux	
Hadoop(하듑)                |\thdfs
AWS                         |\taws
Networking                  |\tnet 
Docker(도커)	            |\tdocker
Remote Login(원격 로그인)   |\tremote
clear screen                |\tclear
Back to Input Selection     |\tback
	""");

        if intype == 'keyboard':
	    keyin = Keyboard();

	elif intype == 'voice':
	    keyin = voice();

        
        #메인메뉴 'Linux' 입력 시    
        if keyin == 'Linux':
            Linux_loop = True;

            while Linux_loop:
                os.system("clear"); #리눅스 명령어 clear

                print("\n"+20*"-"+"리눅스 항목의 메뉴"+"-"*20);
                print("실행할 명령어 입력                      |\tCommand");

                print("""----------------------------------------------
    Calender(달력)                      |\tcal
    Date(날짜)                          |\tdate
    Hard disk Details(디스크 정보)      |\tHDD
    Yum Configuration(yum server 설정)  |\tyumC
    Install Softwares(소프트웨어 설치)  |\tinstall
    WebServer Configuration(웹서버 설정)|\twebC
    Partition                           |\tdiskP
    Back to previous menu               |\tback
		    """);

                if intype == 'keyboard':
                    lchoose = Keyboard();
                elif intype == 'voice':
		    lchoose = voice();    

                
                #lchoose 변수에 임포트한 함수 값을 입력받음.
                if lchoose == 'cal':
		    return("Linux-cal",intype); 

		elif lchoose == 'date':
		    return("Linux-date",intype);

		elif lchoose == 'HDD':
		    return("Linux-HDD",intype);

		elif lchoose == 'yumC':
		    return("Linux-yumC",intype);

		elif lchoose == 'install':
		    return("Linux-install",intype);

		elif lchoose == 'webC':
		    return("Linux-webC",intype);

    		elif lchoose == 'diskP':
                    return("Linux-diskP",intype);

    		elif lchoose == 'back':
		    Linux_loop = False;

		else:
		    print("Invalid Input");







            elif keyin == 'docker':
		docker_loop = True;
		while docker_loop:
		    os.system("clear");

                    print("\n"+20*"-"+"도커 항목의 메뉴"+"-"*20);
                    print("실행할 명령어 입력                      |\tCommand");
                   
                    print("""--------------------------------------------------
	이미지 다운로드	            |\tpullI
	컨테이너 시작(launch)       |\trunC
	컨테이너 중지	            |\tstopC
	컨테이너 시작	            |\tstartC
        컨테이너 이름변경           |\trenameC
	컨테이너 삭제               |\trmC
	이미지 삭제	            |\trmI
	이전메뉴로 돌아가기         |\tback
				""");

		    if intype == 'keyboard':
			docker_choose = Keyboard();

		    elif intype == 'voice':
			docker_choose = voice();


        	    if docker_choose == 'pullI':
			return("docker-pull",intype);

		    elif docker_choose == 'runC':
			return("docker-run",intype);

		    elif docker_choose == 'stopC':
			return("docker-stop",intype);

		    elif docker_choose == 'startC':
			return("docker-start",intype);

	    	    elif docker_choose == 'renameC':
			return("docker-rename",intype);

		    elif docker_choose == 'rmC':
			return("docker-rm",intype);

		    elif docker_choose == 'rmI':
			return("docker-rm",intype);

		    elif docker_choose == 'back':
			docker_loop = False;

		    else:
			print("Invalid Input");


	    elif keyin == 'remote':
		return("remote",intype);

	    elif keyin == 'clear':
		return("clear",intype);

	    elif keyin == 'back':
		return ('0',intype);

	    else:
		print("Invalid Input");
