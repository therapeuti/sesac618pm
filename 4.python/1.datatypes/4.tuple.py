# 튜플은 리스트와 동일하나 데이터 변경을 할 수 없음
# 데이터 변경에 따른 버그가 많이 발생하기 때문에 데이터 변경이 안 되는 자료구조인 튜플이 만들어짐

my_tuple = (1,2,3,4,5)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

# my_tuple[2] = 5  이런 식으로 기존 데이터 변경이 안 됨. 실행시 오류 발생

my_list  = list(my_tuple) # 튜플을 리스트로 변환. 복제본 생성
my_list[2] = 5
print(my_list)
print(my_tuple)

my_tuple2 = tuple(my_list) # 리스트를 튜플로 변환
# my_tuple[4] = 10

# 튜플 안의 데이터를 여러개의 변수로 나누어 담을 수 있음

a, b,_ = ( 1, 2, 3) # 안 쓸 변수를 _로 치환할 수 있음
print(a) 
print(b)
# print(c)
