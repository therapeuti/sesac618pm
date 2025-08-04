import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import os
IMAP_SERVER = 'imap.naver.com'
IMAP_PORT = 993

NAVER_EMAIL = os.getenv('NAVER_EMAIL')

NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(NAVER_EMAIL, NAVER_PASSWORD)

mail.select('INBOX')
status, messages =mail.search(None, "ALL")

print(status, messages)


mail_ids = messages[0].split()
latest_mail_id = mail_ids[-1] # 가장 최신 메일 아이디 가져오기

status, msg_data = mail.fetch(latest_mail_id, "(RFC822)")
print(status, msg_data)

# 본문 데이터 파싱하기
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
        print(f'제목: {subject}')

        # 발신자 정보
        from_ = msg.get('From')
        print(f'발신자 : {from_}')


        # 메일 본문 추출
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get('Content-Disposition'))
                body = part.get_payload(decode=True).decode('utf-8')
                print(f'본문: {body}')
        else: # 단일 파트 메일
            body = msg.get_payload(decode=True).decode('utf-8')
            print(f'본문: {body}')

    mail.logout()