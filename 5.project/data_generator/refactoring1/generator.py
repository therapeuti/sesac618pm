import random
import csv
import uuid
from abc import ABC, abstractmethod
import sys

# 비슷한 부분은 상속클래스로 대체..
# 공통으로 사용할 변수는 클래스 변수로 사용.
# 각 제너레이터 파일 실행시 콘솔에 원하느 데이터 개수 입력하면 만들어지도록 수정.

class Generator(ABC):
    
    file_path_address = 'address_sample.csv'
    file_path_item = 'item_data.csv'

    # 상속받은 클래스에서 사용하는거니까 상속받는 클래스에서 정의하는 것이 더 나음.
    dataset_file_path_user = 'dataset/user.csv' # 추상함수로 만들어서 강제로 변수 만들도록
    dataset_file_path_store = 'dataset/store.csv'
    dataset_file_path_item = 'dataset/item.csv'
    dataset_file_path_order_item = 'dataset/order_item_dataset.csv'
    dataset_file_path_order = 'dataset/order.csv'
    dataset_file_path_orderitem = 'dataset/orderitem.csv'

    # def __init__(self):
    #     # self.uuid = self.generate_uuid()

    def generate_uuid(self):
        id = uuid.uuid4()
        return id
    
    def read_csv(self, file_path):
        csv_contents = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # 필드 제목 건너뜀
            for row in csv_reader:
                csv_contents.append(row)
        return csv_contents # 리스트 안에 리스트 구조로 한 줄 씩 담김
    
    def write_csv(self, file_path, contents):
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(contents)
        
    
    def append_csv(self, file_path, contents):
        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(contents)

    @abstractmethod
    def generate_data(self):
        pass
    
    @abstractmethod
    def generate_dataset(self):
        pass
