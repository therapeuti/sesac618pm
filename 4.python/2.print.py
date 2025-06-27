name = 'Alice'
print(name)
print('Hello', name) # 인자(argument)로 받음
print('Hello' + name) # 덧셈연산이라... 띄어쓰기 되지 않음
print('Hello,' + name + '!!')
print('Hello, {}!!'.format(name))
print('Hello, {}!! {}??'.format(name, name))
# print('Hello, {}!! {}??'.format(name)) 에러..

name1 = 'Bob'
name2 = 'Charlie'
print('Hello, {}!! {}??'.format(name1, name2))
print('Hello, {1}!! {0}??'.format(name1, name2))
print('Hello, {0}!! {1}??'.format(name, name))

print('Hello, %s!!!1 %s???2' %(name1, name2))


print(f'Hello, {name1}!!!!!! {name2}??????') # 가장 많이 쓰이는 f-string 표기법. js 에서는 백틱` ${변수}`