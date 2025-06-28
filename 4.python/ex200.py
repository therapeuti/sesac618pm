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