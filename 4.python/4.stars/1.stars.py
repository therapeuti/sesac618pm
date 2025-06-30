# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')

def draw_triangle(lines):
    for i in range(1,lines+1):
        print('*' * i)

def draw_rtriangle(lines):
    for i in range(1,lines+1):
        print(' ' * (lines+1-i) + '*' * i)

def draw_iltriangle(lines):
    for i in range(1, lines+1):
        print('*' * (lines+1-i))

def draw_irtriangle(lines):
    for i in range(1, lines+1):
        print(' '*(i-1), end='')
        print('*'*(lines+1-i))


draw_triangle(5)
print('-'*10)
draw_rtriangle(5)
print('-'*10)
draw_iltriangle(5)
print('-'*10)
draw_irtriangle(5)
print('-'*10)

for i in range(5,0,-1):
    print('*'*i)

for i in range(5,0,-1):
    print(' '*(5-i), end='')
    print('*'*i)