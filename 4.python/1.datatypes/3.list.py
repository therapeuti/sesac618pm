my_list = [1,2,3,4,5]

my_list.insert(2, 10)
print(my_list)


another_list = [7,8,9]
print(another_list)

my_list.extend(another_list)
print(my_list)

my_list.remove(10) # 리스트에 있는 10을 삭제
print(my_list)

my_list.pop(3) # 해당 인덱스 요소 삭제, 인자를 안 주면 마지막 요소 삭제
print(my_list)

my_list.clear() # 리스트 안에 저장된 내용 비우기

print('-'*10)

my_list=[1,2,3,4,9,2,5,2,4,5,6]

my_list[3]
index_of_3 = my_list.index(3)
print(index_of_3)

count_2 = my_list.count(2)
print(count_2)


sorted_list = sorted(my_list)
print(sorted_list)

print('----- sort 전 my list----------')
print(my_list)
print('------sort 후 my list--------')

my_list.sort() # 원본 데이터를 수정. 리턴 값이 없어서 변수에 할당해도 할당되는 게 없음. 디폴트는 오름차순.
print(my_list)

my_list.sort(reverse=True) # 내림차순
print(my_list)

my_list.reverse()
print(my_list)

my_list2 = my_list.copy()
print(my_list2)

# 리스트 컴프리헨션 #파이썬의 매우 큰 특징(장점)!!!!!!!
numbers = [ x for x in range(10)]
print(numbers)


num11 = [ num for num in range(1,11)]
print(num11)


num1111 = [ num**2  for num in range(1,11)]
print(num1111)

numbers = [   num            for num in range(1,11) if num%2 == 0]
print(numbers)