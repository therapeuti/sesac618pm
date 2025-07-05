import random
import csv
import uuid
from datetime import datetime

# order id 생성, ordertime 생성
# store id, user id 하나씩 랜덤으로 참조하여 가져옴.
# 하나의 order 안에 개수 랜덤으로 하여 item id 참조하여 가져욤.
# 하나의 order 내에서 각 item 별로 order-item-id 부여.
# order-id 10000개, order-item-id 30000개

#order id 생성
order_id = uuid.uuid4()
print(order_id)
print(type(order_id))

# ordertime생성
year = random.randint(2020, 2025)
month = random.randint(1, 12)
day = random.randint(1, 28)
hour = random.randint(8,21)
min = random.randint(0,59)
second = random.randint(0,59)
ordertime = f'{year}-{month:02d}-{day:02d} {hour:02d}:{min:02d}:{second:02d}'
print(ordertime)
print(type(ordertime))

# store id 가져오기
# store dataset에서 랜덤으로 하나의 행을 골라서 -> store id만 가져오기 : csv.Dictreader 사용
with open('dataset/store_dataset.csv','r',encoding='utf-8') as f:
    csv_Dictreader = csv.DictReader(f) # csv_Dictreader는 iterator.. 반복자..라서 바로 random.choice 사용 못 함.
    store = random.choice(list(csv_Dictreader)) # 시퀀스 타입(리스트, 튜플 등)으로 변환 필요.
print(store)
store_id = store['store_id']
print(store_id)


# user id 가져오기
with open('dataset/user_dataset.csv','r',encoding='utf-8') as f:
    csv_Dictreader = csv.DictReader(f) # csv_Dictreader는 iterator.. 반복자..라서 바로 random.choice 사용 못 함.
    user = random.choice(list(csv_Dictreader)) # 시퀀스 타입(리스트, 튜플 등)으로 변환 필요.
print(user)
user_id = user['user_id']
print(user_id)


# 하나의 order내 orderitem 생성
# 하나의 order에서 주문한 item 개수
count = random.randint(1, 10)
print(count)
item_in_order = []
# 아이템 중 count많큼 고르기. 중복 상관없음.
with open('dataset/item_dataset.csv','r',encoding='utf-8') as f:
    csv_Dictreader = csv.DictReader(f)
    item_list = list(csv_Dictreader)
    for _ in range(count):
        order_item_id = uuid.uuid4()
        print('uuid: ', order_item_id)
        item = random.choice(item_list)
        print('랜덤으로 고른 아이템: ', item)
        item_id = item['item_id']
        item_in_order.append((str(order_item_id), item_id))
    print(item_in_order)

