# 빌트인모듈. 내장모듈. 추가 설치하지 않아도 바로 쓸 수 있음.
import datetime as dt

# 모듈명.변수명
# 모듈명.클래스명.함수명()

print(dt.MINYEAR)
print(dt.MAXYEAR)

# YYYY-mm-dd HH:MM:SS.mmmmmmmm
print(dt.datetime.now())
print(dt.datetime.now().strftime('%Y-%m-%d'))
print(dt.datetime.now().strftime('%H:%M:%S'))

# 특정 날짜를 정해서 해당 시간값을 담아놓기
my_time = dt.datetime(2025, 6, 30, 10, 45, 00)
print(my_time)
print(type(my_time))