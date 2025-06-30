# try 안에 오는 범위를 최소화 시킬수록 좋은 것.
# except도 구체적으로 잡아서 핸들링 할수록 좋은 것.
try:
    result = 10/0 #crash 발생.. 실행 중단되고, 프로그램이 종료. 더 이상 다음 줄 실행이 안 됨.
    print(result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")


def convert_to_int(num_str):
    """글자를 숫자로 바꾸는 함수.  <---- docstring이라고 부름

    Arg: 문자열 타입의 숫자

    Returns: 숫자 타입으로 변환된 숫자. 실패 시 None  
    
    """
    try:
        result = int(num_str)
    except ValueError as e: # except 안에서는 오류가 나지않는 최소한의 코드로 구성.
        # print('숫자 변환에 실패함. 입력값: ', num_str)
        print(e, ' 입력값이 숫자가 아닙니다.')
        result = None
    return result

def double_number(num):
    return num * 2

input = 'a'
result = convert_to_int(input)
if result:
    result = double_number(result)
print(f'입력한 숫자 {input}의 두 배 값은 {result}')