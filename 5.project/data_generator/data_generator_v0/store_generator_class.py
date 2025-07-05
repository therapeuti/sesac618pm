import random
import uuid
import csv

class Store_generator:
    def __init__(self):
        pass

    def generate_uuid(self):
        s_id = uuid.uuid4()
        return s_id

    def generate_store_name(self):
        # store type
        store_type = ['폴바셋','투썸플레이스','블루보틀','컴포즈커피','매머드커피','이디야커피','커피빈','할리스커피','스타벅스','메가커피']
        store = random.choice(store_type)
        
        # store address
        address_list=[]
        with open('address_sample.csv','r',encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader) # header 건너뜀
            for row in csv_reader:
                address_list.append(row) # csv_reader 사용하는 경우, 리스트 안에 리스트로 담김.
        address_pick = random.choice(address_list)
        road_name = address_pick[2]
        address = ' '.join(address_pick)
        s_address = address + str(random.randint(1,50)) + '길 ' + str(random.randint(1,100))

        # store name
        road_name = road_name.replace('대로','')
        road_name = road_name.replace('로','')
        store_name = store + ' ' + road_name + '점'

        return store, store_name, s_address
    
    def generate_store(self):
        s_id = self.generate_uuid()
        store_type, store_name, s_address = self.generate_store_name()
        return (str(s_id),store_type, store_name, s_address)
    
    def generate_store_dataset(self, n:int):
        # 데이터셋 처음 만들 때, 헤더 생성
        with open('store_dataset.csv','w',encoding='utf-8',newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['store_id','store_type','store_name','store_address'])        
        for _ in range(n):
            store_info = self.generate_store()
            with open('store_dataset.csv','a',encoding='utf-8',newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(store_info)


if __name__=='__main__':
    store_dataset = Store_generator()
    store_dataset.generate_store_dataset(100)





# store name