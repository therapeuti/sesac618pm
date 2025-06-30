import math
# 기본 수학 연산을 위한 빌트인 모듈
# https://docs.python.org/ko/3.10/library/datetime.html


print(math.pi)

# 원의 넓이
# pi * r^2

radius = 5
area = math.pi * radius**2

print(f'반지름이 {radius}인 원의 넒이는 {area}입니다.')

area2 = math.pi * math.pow(radius, 2)
print(f'반지름이 {radius}인 원의 넒이는 {area2:9.2f}입니다.') # :2f 소수 둘째자리까지 표시
print(f'반지름이 {radius}인 원의 넒이는 {area2:>9.2f}입니다.') # :2f 소수 둘째자리까지 표시
print(f'반지름이 {radius}인 원의 넒이는 {area2:<9.2f}입니다.') # :2f 소수 둘째자리까지 표시



text = "Hi"
print(f"[{text:<10}]")
print(f"[{text:>10}]")
print(f"[{text:^10}]") # 가운데에 쓰임.