numbers = [1,2,3,4,5]

first_value = None
last_value = None

try:
    first_value = numbers[0]
    print(f'첫번째 숫자는 {first_value}')

    # last_value = numbers[5]  # crash 발생
    last_value = numbers[4]  
    print({f'마지막 숫자는 {last_value}'})


except IndexError as e:
    print(e)
    print('마지막 인덱스 잘못됨')


if first_value and last_value:
    diff = last_value - first_value
    print('두 수의 차이는 ', diff)
else:
    print('오류...............이런 식으로 짜면 안 됨.')