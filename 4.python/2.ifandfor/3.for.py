for i in range(10):
    print(i)

for i in range(1, 10): # 끝값은 포함하지 않음
    print(i)

for i in range(1, 10, 2): # 1부터 10까지 2개씩 건너뜀. 10은 포함하지 않음
    print(i)


fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)

str = "Hello, World!"
for char in str:
    print(char)


count_o = 0
for char in str:
    if char == 'o' :
        count_o += 1
print(f'{str} 문장 내의 o의 개수는 {count_o}개 입니다.')