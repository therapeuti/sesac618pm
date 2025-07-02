import random
import csv
import uuid
import pandas as pd
# order id 생성, ordertime 생성
# store id, user id 하나씩 랜덤으로 참조하여 가져옴.
# 하나의 order 안에 개수 랜덤으로 하여 item id 참조하여 가져욤.
# 하나의 order 내에서 각 item 별로 order-item-id 부여.
# order-id 10000개, order-item-id 30000개
class Order_generator:
    #order id 생성
    def generate_uuid(self):
        order_id = uuid.uuid4()
        return order_id
    
    def generate_ordertime(self):
        # ordertime생성
        year = random.randint(2020, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(8,21)
        min = random.randint(0,59)
        second = random.randint(0,59)
        ordertime = f'{year}-{month:02d}-{day:02d} {hour:02d}:{min:02d}:{second:02d}'
        return ordertime

    def reference_store_id(self):
        # store id 가져오기
        with open('dataset/store_dataset.csv','r',encoding='utf-8') as f:
            csv_Dictreader = csv.DictReader(f) # csv_Dictreader는 iterator.. 반복자..라서 바로 random.choice 사용 못 함.
            store = random.choice(list(csv_Dictreader)) # 시퀀스 타입(리스트, 튜플 등)으로 변환 필요.
            store_id = store['store_id']
            return store_id

    def reference_user_id(self):
        # user id 가져오기
        with open('dataset/user_dataset.csv','r',encoding='utf-8') as f:
            csv_Dictreader = csv.DictReader(f) # csv_Dictreader는 iterator.. 반복자..라서 바로 random.choice 사용 못 함.
            user = random.choice(list(csv_Dictreader)) # 시퀀스 타입(리스트, 튜플 등)으로 변환 필요.
        user_id = user['user_id']
        return user_id
    
    def generate_orderitem(self): # 하나의 order내 orderitem 생성
        count = random.randint(1, 10) # 주문한 아이템 개수 설정
        items_in_order = []
        # 아이템 중 count많큼 고르기. 중복 상관없음.
        with open('dataset/item_dataset.csv','r',encoding='utf-8') as f:
            csv_Dictreader = csv.DictReader(f)
            item_list = list(csv_Dictreader)
            for _ in range(count):
                order_item_id = uuid.uuid4()
                item = random.choice(item_list)
                item_id = item['item_id']
                items_in_order.append((str(order_item_id), item_id))
        return items_in_order

    def generate_order(self):
        order = []
        order_id = self.generate_uuid()
        ordertime = self.generate_ordertime()
        store_id = self.reference_store_id()
        user_id = self.reference_user_id()
        items_in_order = self.generate_orderitem() # 주문한 여러개의 아이템이 튜플형태로 리스트에 담김

        for order_item_id, item_id in items_in_order:
            order.append((str(order_id), ordertime, store_id, user_id, order_item_id, item_id))
        return order
    
    def generate_order_item_dataset(self, n:int): 
        with open('dataset/orderitem_dataset.csv','w',encoding='utf-8',newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['order_id','ordertime','store_id','user_id','order_item_id','item_id'])

        for order in range(n):
            order = self.generate_order()
            with open('dataset/orderitem_dataset.csv','a',encoding='utf-8',newline='') as f:
                csv_writer = csv.writer(f)
                for i in order:
                    csv_writer.writerow(i)

    def split_order(self):
        df = pd.read_csv('dataset/orderitem_dataset.csv', encoding='utf-8')
        order = df[['order_id','ordertime','store_id','user_id']].drop_duplicates()
        orderitem = df[['order_item_id','order_id','item_id']].drop_duplicates()
        order.to_csv('dataset/order.csv',index=False)
        orderitem.to_csv('dataset/orderitem.csv',index=False)
  

   
if __name__=='__main__':
    order = Order_generator()
    # order.generate_order_item_dataset(10000)
    order.split_order()