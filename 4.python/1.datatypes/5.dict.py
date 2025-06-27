my_dict = {"name":"Alice", "age":35, "location":"Seoul"}
print(my_dict)

print(my_dict['name'])

user1 = {"name":"Bob"}
print(user1['name'])

user1['name'] = 'Robert'

print(user1['name'])

print(user1)

user1['car'] = '기아 K5'

print(user1)

# 특정 키값을 지우는 키워드는 del 
# 키워드가 예약어 말하는 거??
# 주요 키워드 외우고... 이런 키워드로는 변수명, 클래스명, 함수명으로 사용할 수 없음
del user1['car']
print(user1)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

user_items = my_dict.items()
useritem_list = list(user_items)
print(useritem_list)