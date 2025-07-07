# item : id, type, name, price
import csv
import uuid

class Item_generator:

    def generate_uuid(self):
        item_id = uuid.uuid4()
        return item_id

    def generate_item_dataset(self):
        item_list = []
        with open('item_data.csv','r',encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                item_id = self.generate_uuid()
                row.insert(0,item_id)
                item_list.append(row)

        with open('item_dataset.csv','w',encoding='utf-8',newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['item_id','item_name','item_type','item_price'])
            csv_writer.writerows(item_list)


# store type 상관없이 모든 store의 아이템과 아이템id가 같은 건지
# store type별로 각 아이템의 id가 서로 다른건지
# store마다 아이템id가 전부 다른건지...
# 일단 지금 한 건. 모든 store에 모두 같은 아이템id 사용. 모든 스토어 통합하여 각 아이템별 매출현황 확인 가능.....


if __name__=='__main__':
    item_data = Item_generator()
    item_data.generate_item_dataset()
    