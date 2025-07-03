from generator import *
import pandas as pd

class Order_generator(Generator):
    
    def generate_ordertime(self): # 주문시간ordertime 생성
        year = random.randint(2020, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(8,21)
        min = random.randint(0,59)
        second = random.randint(0,59)
        ordertime = f'{year}-{month:02d}-{day:02d} {hour:02d}:{min:02d}:{second:02d}'
        return ordertime

    def reference_store_id(self): # store id 가져오기
        store_list = self.read_csv(Generator.dataset_file_path_store)
        store = random.choice(store_list)
        # print(store)
        store_id = store[0] # store 정보에서 uuid만 가져오기
        return store_id

    def reference_user_id(self): # user id 가져오기
        user_list = self.read_csv(Generator.dataset_file_path_user)
        user = random.choice(user_list)
        # print(user)
        user_id = user[0] # user 정보에서 uuid만 가져오기
        # print(user[0])
        return user_id
    
    def generate_orderitem(self): # 하나의 주문order에 포함된 메뉴아이템orderitem 생성
        items_in_order = []
        count = random.randint(1, 6) # 주문한 아이템 개수 설정
        item_list = self.read_csv(Generator.dataset_file_path_item)
        items = random.sample(item_list, count) # 중복없이 고르기. 리스트 안에 리스트 구조
        # items = random.choices(item_list, k=count) # 중복해서 고르기 -> 중복되는 아이템이 서로 다른 orderitem id를 갖게 되므로.. 수량 항목을 추가하는식으로 진행...?
        # print(items)
        for item in items:
            orderitem_id = self.generate_uuid()
            items_in_order.append((orderitem_id, item[0]))
        # print(items_in_order)
        return items_in_order

    def generate_data(self):
        order = []
        order_id = self.generate_uuid()
        ordertime = self.generate_ordertime()
        store_id = self.reference_store_id()
        user_id = self.reference_user_id()
        items_in_order = self.generate_orderitem() # 주문한 여러개의 아이템이 튜플형태로 리스트에 담김

        for order_item_id, item_id in items_in_order:
            order.append((order_id, ordertime, store_id, user_id, order_item_id, item_id))
        # print(order)
        return order
    
    def generate_dataset(self, n:int): 
        field = ['order_id','ordertime','store_id','user_id','order_item_id','item_id']
        self.write_csv(Generator.dataset_file_path_order_item, field)   

        for order in range(n):
            order = self.generate_data()
            for i in order:
                self.attend_csv(Generator.dataset_file_path_order_item, i)
        print(f'주문 데이터 {n}개를 생성했습니다!')
        
    
    # 컬럼 분리하여 order.csv와 orderitem.csv 생성
    def split_order(self):
        df = pd.read_csv(Generator.dataset_file_path_order_item, encoding='utf-8')
        order = df[['order_id','ordertime','store_id','user_id']].drop_duplicates()
        orderitem = df[['order_item_id','order_id','item_id']].drop_duplicates()
        order.to_csv(Generator.dataset_file_path_order,index=False)
        orderitem.to_csv(Generator.dataset_file_path_orderitem,index=False)
        print('데이터 컬럼을 분리하여 저장했습니다!')
  

   
if __name__=='__main__':
    if len(sys.argv) > 1:
        data_num = int(sys.argv[1])
    else:
        data_num = int(input('생성할 데이터 개수를 입력하세요: '))

    order = Order_generator()
    order.generate_dataset(data_num)
    order.split_order()