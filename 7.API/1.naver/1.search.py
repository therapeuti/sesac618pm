import urllib.request
import json

client_id = '발급받은 어플리케이션 클라이언트 아이디'
client_secret = '발급받은 어플리케이션 클라이언트 시크릿'
text = "python 개발"

encText = urllib.parse.quote(text)
url = 'https://openapi.naver.com/v1/search/blog?query=' + encText

print(url)


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
print(request)

response = urllib.request.urlopen(request)
rescode = response.getcode()
print(rescode)
if rescode == 200:
    response_body = response.read()
    print(response_body.decode())

