import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

# SMTP 서버 설정
SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 587

# 환경변수에서 이메일 정보 가져오기
NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

print("=== 환경변수 확인 ===")
print(f"NAVER_EMAIL: {NAVER_EMAIL}")
print(f"NAVER_PASSWORD: {'*' * len(NAVER_PASSWORD) if NAVER_PASSWORD else 'None'}")

# 환경변수 검증
if not NAVER_EMAIL or not NAVER_PASSWORD:
    print("❌ 오류: .env 파일에 NAVER_EMAIL 또는 NAVER_PASSWORD가 제대로 설정되지 않았습니다.")
    print("✅ .env 파일 형식 예시:")
    print("NAVER_EMAIL=your_email@naver.com")
    print("NAVER_PASSWORD=your_app_password")
    exit(1)

RECIPIENT_EMAIL = NAVER_EMAIL

# 이메일 내용
subject = '네이버 이메일 테스트'
body = '이 메일은 파이썬을 통해 생성됨'

print("\n=== 이메일 발송 시작 ===")

try:
    # MIMEMultipart 사용 (더 안정적)
    message = MIMEMultipart()
    message['From'] = NAVER_EMAIL
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = subject
    
    # 본문 추가
    message.attach(MIMEText(body, 'plain', 'utf-8'))
    
    print(f"📧 발신자: {NAVER_EMAIL}")
    print(f"📧 수신자: {RECIPIENT_EMAIL}")
    print(f"📧 제목: {subject}")
    
    # SMTP 서버 연결
    print(f"🔗 SMTP 서버 연결 중... ({SMTP_SERVER}:{SMTP_PORT})")
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    
    print("🔒 TLS 보안 연결 시작...")
    smtp.starttls()
    
    print("🔑 로그인 시도...")
    smtp.login(NAVER_EMAIL, NAVER_PASSWORD)
    print("✅ 로그인 성공!")
    
    print("📤 이메일 발송 중...")
    smtp.sendmail(NAVER_EMAIL, RECIPIENT_EMAIL, message.as_string())
    print("✅ 이메일 발송 완료!")
    
except smtplib.SMTPAuthenticationError as e:
    print(f"❌ 인증 오류: {e}")
    print("🔧 해결 방법:")
    print("   1. 네이버 이메일과 앱 비밀번호가 정확한지 확인")
    print("   2. 네이버 메일 > 환경설정 > POP3/IMAP 설정에서 IMAP/SMTP 사용 허용")
    print("   3. 2단계 인증 설정 후 앱 비밀번호 생성 (일반 비밀번호 사용 불가)")
    print("   4. 앱 비밀번호 생성: 네이버 메일 > 환경설정 > 2단계 인증 > 앱 비밀번호 생성")
    
except smtplib.SMTPRecipientsRefused as e:
    print(f"❌ 수신자 거부: {e}")
    
except smtplib.SMTPServerDisconnected as e:
    print(f"❌ 서버 연결 끊김: {e}")
    
except smtplib.SMTPException as e:
    print(f"❌ SMTP 오류: {e}")
    
except Exception as e:
    print(f"❌ 예상치 못한 오류: {e}")
    print(f"❌ 오류 타입: {type(e).__name__}")
    
finally:
    try:
        smtp.quit()
        print("🔌 SMTP 연결 종료")
    except:
        pass

print("\n=== 추가 확인사항 ===")
print("1. .env 파일이 Python 스크립트와 같은 폴더에 있는지 확인")
print("2. .env 파일 내용:")
print("   NAVER_EMAIL=your_email@naver.com")
print("   NAVER_PASSWORD=your_16digit_app_password")
print("3. 네이버 메일 IMAP/SMTP 설정 확인")
print("4. 앱 비밀번호는 16자리 숫자여야 함")