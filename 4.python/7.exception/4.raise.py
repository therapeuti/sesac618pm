def square_root(num):
    if num < 0:
        raise ValueError('음수의 제곱근은 계산할 수 없습니다')
    return num ** 0.5


print(square_root(25))
print(square_root(10))
print(square_root(1))
print(square_root(0))


try:
    print(square_root(-4))
except ValueError as e:
    print(e)
