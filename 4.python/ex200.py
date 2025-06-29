def print_coin():
    return "비트코인"


# for i in range(100):
#     print(print_coin())


def print_coins():
    for i in range(5):
        print(i)
        print('비트코인')
        


# print(print_coins())  -> 마지막에 None은 왜 나오는거야? return값이 없어서?
print_coins()


def print_with_smile(sentence):
    print(sentence+':D')

print_with_smile('안녕하세요')


def print_upper_price(price):
    print(price + price*3/10)

def print_sum(a,b):
    print(a+b)

def print_arithmetic_operation(a,b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b}')

print_arithmetic_operation(3,4)


def print_max(a,b,c):
    if a < b : #b가 a보다 큰 경우
        if b < c: # b가 a보다 큰 경우, c가 가장 큼. b가 a와 같은 경우도 c가 가장 큼
            return c
        else: #b가 보다 작거나 a,c 비교. 같은 경우
            return b #b가 c와 같을 수도 있고b와 a가 같은 경우, 셋이 모두 같고, b가 a보다 큰 경우에도 b,c가 가장 큼. b가 c보다 더 클 수도 있음.
    elif a < c:  # a가 b보다 큰 경우 c가 가장 큼., a가 c랑 같은 경우에도 a,c가 가장 크니까
        return c
    

def print_maz(a,b,c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    # print(max_val)
    return max_val

def print_reverse(sentence):
    print(sentence[::-1])

# def print_score([1,2,3]):
#     sum = 0
#     for i in [1,2,3]:
#         sum += i
#     avg = sum / len([1,2,3])
#     print(avg)

def print_score2(score_list):
    print(sum(score_list)/len(score_list))


def print_even(number_list):
    even_num = []
    for num in number_list:
        if num % 2 == 0:
            print(num)
    #         even_num.append(num)
    #         prin
    # print(even_num)

def print_keys(dict):
    # print(dict.keys())
    for key in dict.keys():
        print(key)

def print_value_by_keys(my_dict, date):
    print(my_dict[date])

# def print_5xn(string):
#     n = len(string)//5
#     i = len(string)%5
#     for i in range(n):
#         print(string[5*i:5*i + 5])
#     print(string[-i:])
   


def print_mxn(string,n):
    for i in range(len(string)+1):
        print(string[n*i:n*i+n])

def calc_monthly_salary(annual_salary): #연봉을 12개월 나눔.1미만은 버림. 걍 int로 바꿔도 버림됨.
    monthly_salary = int(annual_salary/12,0) # floor는 math라이브러리 함수.. import 필요
    print(monthly_salary)  
    return monthly_salary

### 파이썬 예제 230까지 완료

def make_url(string):
    url = "www."+string+".com"
    return url

print(make_url("naver"))

def make_list(string):
    made_list = []
    for i in string:
        made_list.append(i)
    return made_list

print(make_list("made_list"))

def pickup_even(num_list):
    even = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
    return even

print(pickup_even([1,2,3,4,5,6,7,8,9]))

def convert_int(string):
    string_list = string.split(',')
    result = int(''.join(string_list))
    return result

print(convert_int("123,456,34,6,7"))

# 240까지 완료
from datetime import datetime,timedelta

print(datetime.now())

now = datetime.now()

print(type(now))


days5_ = timedelta(days=5)
print(now - days5_)

for i in range(5,0,-1):
    day = timedelta(days=i)
    print(now - day)

print(datetime.now().strftime("%H:%M:%S"))

date = ("2020-05-04")
print(datetime.strptime(date,"%Y-%m-%d"))

import time
i = 0
# while i < 10:
#
#     print(datetime.now())
#     i += 1
#     time.sleep(1)


import os
print(os.getcwd())

# os.rename('practice.txt','practice2.txt')

import numpy as np

np_array = np.arange(0, 5.1, 0.1, dtype='float64')
# print(np_array)

for i in np.arange(0, 5.1, 0.1):
    print(i)

# 파이썬 예제 250까지 완료 -> 이후부터 코랩으로 진행
# 예외처리


# os.rename('종목코드.txt', '매수종목1.txt')
# print('메모장 이름 바뀌었나?')

memo = open('매수종목1.txt', "w", encoding='utf-8')
# w면 기존 파일 지우고 새로 씀
# a는 기존 파일 뒤에 추가
memo.write('005930\n005380\n035420')
memo.close()

memo2 = open('매수종목2.txt', 'w', encoding='utf-8')
memo2.write('005930 삼성전자\n')
memo2.write('005380 현대차\n')
memo2.write('035420 NAVER\n')
memo2.close()


memo3 = open('매수종목.csv', 'w', encoding='utf-8')
memo3.write('종목명,종목코드,PER\n')
memo3.write('삼성전자,005930,15.79\n')
memo3.write('NAVER,035420,55.82\n')
memo3.close()

code_list = []
with open('매수종목1.txt','r',encoding='utf-8') as f:
    # code_list = f.readlines()
    for line in f: #파일을 한 줄 씩 읽음
        line = line.strip() # 줄바꿈 \n . 변수에 할당해야함.
        code_list.append(line)

print(code_list)
f.close()


dict = {}
with open('매수종목2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        i = line.strip().split(' ')
        print(i)
        dict[i[0]] = i[1]
        print(dict)


per = ["10.31", "", "8.00"]
per_float = []
for i in per:
    try:
        per_float.append(float(i))
        print(per_float) 
    except ValueError as e:
        print(0)
        per_float.append(0)


num = 10
num_list = [1,4,8,0,6,5]

for i in num_list:
    try:
        print(num / i)
    except ZeroDivisionError as e:
        print(e)


data = [1,2,3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)


for i in per:
    try:
        print(float(i))
    except ValueError as e:
        print(e)
    else:
        print('else 예외가 발생하지 않았을 때 수행할 코드')
    finally:
        print('예외 발생 여부와 상관없이 항상 수행할 코드')
