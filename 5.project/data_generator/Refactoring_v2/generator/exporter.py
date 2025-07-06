from abc import ABC, abstractmethod
from user_generator import *
import pandas as pd

class Exporter:
    @abstractmethod
    def exporter(self, data):
        pass


class Console_exporter(Exporter):
    def exporter(self, data):
        for i in data:
            print(i)

class Csv_exporter(Exporter):
    def exporter(self, data, file_path, file_name):
        fieldnames = data[0].keys()
        with open(f'{file_path}/{file_name}', 'w', encoding='utf-8') as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(data)
        print('csv파일이 저장되었습니다.')


class Excel_exporter(Exporter):
    def exporter(self, data, file_path, file_name):
        df = pd.DataFrame(data)
        df.to_excel(f'{file_path}/{file_name}', index=False, engine='openpyxl')
        print('엑셀 파일이 저장되었습니다.')




file_path = '../output'
file_name = 'user_dataset.xlsx'

user = User_generator()
export = Excel_exporter()
export.exporter(user.generate_dataset(5), file_path, file_name)


