from dotenv import load_dotenv
import os

# 디버깅 추가
print("현재 작업 디렉토리:", os.getcwd())
print(".env 파일 존재 여부:", os.path.exists('.env'))

# load_dotenv 결과 확인
result = load_dotenv()
print("load_dotenv 결과:", result)

# 모든 환경변수 출력해보기
print("SESSION_SECRET_KEY:", repr(os.getenv('SESSION_SECRET_KEY')))
print("KAKAO_CLIENT_ID:", repr(os.getenv('KAKAO_CLIENT_ID')))

# app = Flask(__name__)