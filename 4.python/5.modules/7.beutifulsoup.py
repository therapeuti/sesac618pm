import requests
from bs4 import BeautifulSoup # 라이브러리 안에 있는 특정 객체만 가져오기

response = requests.get('https://blog.naver.com/kimsue0')
print(response)
print(response.status_code)
print(response.text) # 그냥 문자열


# HTML 파싱해주는 라이브러리
soup = BeautifulSoup(response.text, "html.parser") # HTML을 파싱해서 DOm형태 자료 구조를 갖추고 있음.
print(soup)
head = soup.find('head')
print(head)
body = soup.find('body')
print('바디 DOM은', body)

bodytext = body.text.strip()
print(bodytext)

