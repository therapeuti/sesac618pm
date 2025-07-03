from generator import *

class Store_generator(Generator):
    file_path_store = 'store_type.csv'

    def generate_store_name(self):
        # store type
        store_type = self.read_csv(self.file_path_store)
        store = random.choice(store_type)[0]
        # print(store)
        
        # store address
        address_list = self.read_csv(Generator.file_path_address)
        address_pick = random.choice(address_list)
        road_name = address_pick[2]
        address = ' '.join(address_pick)
        s_address = address + str(random.randint(1,50)) + '길 ' + str(random.randint(1,100))

        # store name
        road_name = road_name.replace('대로','')
        road_name = road_name.replace('로','')
        store_name = store + ' ' + road_name + '점'

        return store, store_name, s_address
    
    def generate_data(self):
        s_id = self.generate_uuid()
        store_type, store_name, s_address = self.generate_store_name()
        return (s_id,store_type, store_name, s_address)
    
    def generate_dataset(self, n:int):
        # 데이터셋 처음 만들 때, 헤더 생성
        field = ['store_id','store_type','store_name','store_address']
        self.write_csv(Generator.dataset_file_path_store, field)
        for _ in range(n):
            store_info = self.generate_data()
            self.attend_csv(Generator.dataset_file_path_store, store_info)
        print(f'스토어 데이터 {n}개가 생성되었습니다.')


if __name__=='__main__':
    if len(sys.argv) > 1:
        data_num = int(sys.argv[1])
    else:
        data_num = int(input('생성할 데이터 개수를 입력하세요: '))

    store_dataset = Store_generator()
    store_dataset.generate_dataset(data_num)