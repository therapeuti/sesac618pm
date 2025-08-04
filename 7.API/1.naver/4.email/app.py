import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 587

NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

RECIPIENT_MAIL = NAVER_EMAIL

# 메일 내용
subject = '네이버 이메일 테스트'
body = '이 메일은 파이썬을 통해 생성됨'

# mime 타입으로 인코딩
message = MIMEText(body)
message['subject'] = subject
message['body'] = body
message['to'] = RECIPIENT_MAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER,SMTP_PORT )
    smtp.starttls() # TLS 보안 연결 시작
    smtp.login(NAVER_EMAIL, NAVER_PASSWORD)
    smtp.sendmail(NAVER_EMAIL, RECIPIENT_MAIL, message.as_string()) # 전송
except Exception as e:
    print(f'메일 전송 중 오류 발생: {e}')
finally:
    smtp.quit()  # 종료


