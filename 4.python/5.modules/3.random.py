import random
# 무작위 숫자 만들기

print('랜덤 숫자: ', random.randint(1,100)) # 1부터 100까지의 양수를 다 포함하느 ㄴ랜덤 숫자를 생성

# 주사위 던지기 구현

def roll_dice():
    number = random.randint(1,6)
    return number

print(f'주사위 던진 결과: {roll_dice()}')

# 주사위를 100번 던져보고, 1000번, 10000번 던져서 각 숫자가 나올 확률 출력
# 1이 나온 횟수: 000번, 확률: 000 %

def dice_num_percentage(n):
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []

    for i in range(n):
        num = roll_dice()
        if num == 1:
            one.append(num)
        elif num == 2:
            two.append(num)
        elif num == 3:
            three.append(num)
        elif num == 4:
            four.append(num)
        elif num == 5:
            five.append(num)
        else:
            six.append(num)
    one1 = len(one)/n
    two2 = len(two)/n
    three3 = len(three)/n
    four4 = len(four)/n
    five5 = len(five)/n
    six6 = len(six)/n

    print(f'1이 나올 확률은 {one1}입니다.')
    print(f'2가 나올 확률은 {two2}입니다.')
    print(f'3이 나올 확률은 {three3}입니다.')
    print(f'4가 나올 확률은 {four4}입니다.')
    print(f'5가 나올 확률은 {five5}입니다.')
    print(f'6이 나올 확률은 {six6}입니다.')


# dice_num_percentage(100)



def dice_num_percentage2(n):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0

    for i in range(n):
        num = roll_dice()
        if num == 1:
            one += 1
        elif num == 2:
            two += 1
        elif num == 3:
            three += 1
        elif num == 4:
            four += 1
        elif num == 5:
            five += 1
        else:
            six += 1

    one1 = one/n
    two2 = two/n
    three3 = three/n
    four4 = four/n
    five5 = five/n
    six6 = six/n

    for i in range(1,7):
        print(f'{i}이 나올 확률은 {one1}입니다.')
    


# dice_num_percentage2(1000)


def roll_dices(n):
    counts = [0,0,0,0,0,0]
    for i in range(n):
        num = roll_dice()
        counts[num-1] += 1
        
    for i in range(1,7):
        print(f'{i}이 나온 횟수는 {counts[i-1]}, 확률은 {counts[i-1]/n}입니다.')

print('-'*10)
# roll_dices(10000)


def roll_dices2(n):
    counts = {i:0 for i in range(1,7)}
    for i in range(n):
        num = roll_dice()
        counts[num] += 1
        
    for num, count in counts.items():
        print(f'{num}이 나온 횟수는 {count}, 확률은 {count/n}입니다.')



print('-'*10)
roll_dices2(100000)