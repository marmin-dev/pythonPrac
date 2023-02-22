import smtplib
# 도메인과 포트넘버 설정
# 587 465 사용가능 그 번호또한 작동하지 않는 경우 임의의 번호를 전달하더라도
# 파이썬 스크립트를 막는 방화벽이나 바이러스 백신이 설치되어 있다면
# 작동 되지 않는다
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
# ehlo 를 실행하여 서버에 접속한다
# 587번 포트를 사용할 경우 TLS 암호화를 사용한다
# 발송하는 모든 이메일은 암호화된다 수신자가 아닌 이상 해당 이메일을 읽을 수 없다
# 이와 같은 종류의 암호화를 적용하려면 smtp_object.starttls를 실행한다
smtp_object.ehlo()
smtp_object.starttls()
# 이메일과 비밀번호 설정하기
# 암호나 이메일의 원래의 문자열을 스크립트에 절대 저장해서는 안된다
# password = input('What is your password?')
import getpass
# 보안 비밀번호 입력
# password = getpass.getpass("Password please")
# password = 'password123'
# 이 단계는 일반적인 이메일 비밀번호 대신 앱 비밀번호를 생성해야 하는 지메일 사용자들을 위한 것이다
# 2차 검증 필요

email = getpass.getpass("Email: ")
password = getpass.getpass("Password: ")
smtp_object.login(email,password)
from_address = email
to_address = email
subject = input("enter the subjectline")
message = input("enter the body message")
msg = "Subject: "+subject+'\n'+message
smtp_object.sendmail(from_address,to_address,msg)