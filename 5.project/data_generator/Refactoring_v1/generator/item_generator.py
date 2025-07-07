from generator import *

class Item_generator(Generator):
    file_path_item = 'item_data.csv'

    def generate_data(self):
        item_list = self.read_csv(self.file_path_item)
        for item in item_list:
            item_id = self.generate_uuid()
            item.insert(0, item_id)

        print(item_list)
        return item_list

    def generate_dataset(self):
        item_list = self.generate_data()
        field = ['item_id','item_name','item_type','item_price']
        self.write_csv(Generator.dataset_file_path_item, field)
        for row in item_list:
            self.append_csv(Generator.dataset_file_path_item, row)
        print('메뉴 아이템 데이터셋을 생성했습니다.')


if __name__=='__main__':
    item_data = Item_generator()
    item_data.generate_dataset()

    