import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv()  # .env 파일을 읽어서 내용을 메모리에 둠

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")
text = "python 개발"

encText = requests.utils.quote(text)
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

print(url)

header = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret}

response = requests.get(url, headers=header)
print(response.status_code)
if response.status_code == 200:
    response_body = response.text
    print(response_body)

    data = json.loads(response_body)
    print(data)

    selected_columns = [["title", "link", "description"]]
    for item in data['items']:
        print(item['title'], item['lin'])