import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# IMAP 서버 설정
IMAP_SERVER = 'imap.naver.com'
IMAP_PORT = 993

# 환경변수에서 인증 정보 가져오기
NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

def decode_mime_words(s):
    """MIME 인코딩된 문자열을 디코딩"""
    if not s:
        return s
    
    decoded_words = decode_header(s)
    decoded_string = ""
    
    for word, encoding in decoded_words:
        if isinstance(word, bytes):
            try:
                decoded_string += word.decode(encoding if encoding else 'utf-8')
            except (UnicodeDecodeError, LookupError):
                # 디코딩 실패시 다른 인코딩 시도
                for fallback_encoding in ['utf-8', 'euc-kr', 'cp949']:
                    try:
                        decoded_string += word.decode(fallback_encoding)
                        break
                    except (UnicodeDecodeError, LookupError):
                        continue
                else:
                    # 모든 인코딩 실패시 에러 무시하고 디코딩
                    decoded_string += word.decode('utf-8', errors='ignore')
        else:
            decoded_string += word
    
    return decoded_string

def get_email_body(msg):
    """이메일 본문 추출"""
    body = ""
    
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get('Content-Disposition', ''))
            
            # 첨부파일이 아닌 텍스트 부분만 처리
            if 'attachment' not in content_disposition:
                if content_type == "text/plain":
                    try:
                        payload = part.get_payload(decode=True)
                        if payload:
                            # 다양한 인코딩 시도
                            for encoding in ['utf-8', 'euc-kr', 'cp949']:
                                try:
                                    body = payload.decode(encoding)
                                    break
                                except (UnicodeDecodeError, LookupError):
                                    continue
                            else:
                                body = payload.decode('utf-8', errors='ignore')
                            break
                    except Exception as e:
                        print(f"본문 디코딩 오류: {e}")
                        continue
    else:
        # 단일 파트 메일
        try:
            payload = msg.get_payload(decode=True)
            if payload:
                for encoding in ['utf-8', 'euc-kr', 'cp949']:
                    try:
                        body = payload.decode(encoding)
                        break
                    except (UnicodeDecodeError, LookupError):
                        continue
                else:
                    body = payload.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"본문 디코딩 오류: {e}")
            body = "본문을 읽을 수 없습니다."
    
    return body

def main():
    # 환경변수 검증
    if not NAVER_EMAIL or not NAVER_PASSWORD:
        print("❌ 오류: .env 파일에 NAVER_EMAIL 또는 NAVER_PASSWORD가 설정되지 않았습니다.")
        return
    
    print("=== 네이버 메일 읽기 시작 ===")
    print(f"📧 계정: {NAVER_EMAIL}")
    
    mail = None
    try:
        # IMAP 서버 연결
        print(f"🔗 IMAP 서버 연결 중... ({IMAP_SERVER}:{IMAP_PORT})")
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        
        # 로그인
        print("🔑 로그인 중...")
        mail.login(NAVER_EMAIL, NAVER_PASSWORD)
        print("✅ 로그인 성공!")
        
        # 받은편지함 선택
        print("📥 받은편지함 선택...")
        status, messages = mail.select('INBOX')
        print(f"📬 총 메일 수: {messages[0].decode()}")
        
        # 모든 메일 검색
        print("🔍 메일 검색 중...")
        status, messages = mail.search(None, "ALL")
        
        if status != 'OK':
            print("❌ 메일 검색 실패")
            return
            
        mail_ids = messages[0].split()
        
        if not mail_ids:
            print("📭 받은편지함이 비어있습니다.")
            return
            
        print(f"📊 검색된 메일 수: {len(mail_ids)}")
        
        # 가장 최신 메일 가져오기
        latest_mail_id = mail_ids[-1]
        print(f"📤 최신 메일 ID: {latest_mail_id.decode()}")
        
        # 메일 데이터 가져오기
        print("📖 메일 내용 가져오는 중...")
        status, msg_data = mail.fetch(latest_mail_id, "(RFC822)")
        
        if status != 'OK':
            print("❌ 메일 데이터 가져오기 실패")
            return
        
        # 메일 파싱
        print("\n=== 최신 메일 내용 ===")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # 메일 객체 생성
                msg = email.message_from_bytes(response_part[1])
                
                # 제목 디코딩
                subject = decode_mime_words(msg.get('Subject', '제목 없음'))
                print(f"📋 제목: {subject}")
                
                # 발신자 정보
                from_ = decode_mime_words(msg.get('From', '발신자 정보 없음'))
                print(f"👤 발신자: {from_}")
                
                # 수신자 정보
                to_ = decode_mime_words(msg.get('To', '수신자 정보 없음'))
                print(f"📧 수신자: {to_}")
                
                # 날짜 정보
                date_ = msg.get('Date', '날짜 정보 없음')
                print(f"📅 날짜: {date_}")
                
                # 메일 본문 추출
                body = get_email_body(msg)
                print(f"\n📄 본문:")
                print("-" * 50)
                print(body[:500] + ("..." if len(body) > 500 else ""))  # 처음 500자만 출력
                print("-" * 50)
                
                break  # 첫 번째 메일만 처리
        
        print("\n✅ 메일 읽기 완료!")
        
    except imaplib.IMAP4.error as e:
        print(f"❌ IMAP 오류: {e}")
        print("🔧 해결 방법:")
        print("   1. 네이버 메일 > 환경설정 > POP3/IMAP 설정에서 IMAP/SMTP 사용 허용")
        print("   2. 앱 비밀번호가 올바른지 확인 (16자리 숫자)")
        
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        print(f"❌ 오류 타입: {type(e).__name__}")
        
    finally:
        # 연결 종료
        if mail:
            try:
                mail.logout()
                print("🔌 IMAP 연결 종료")
            except:
                pass

if __name__ == "__main__":
    main()