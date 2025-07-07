import csv
import json

   
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

    
def read_csv(file_path):
    csv_contents = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # 필드 제목 건너뜀
        for row in csv_reader:
            csv_contents.append(row)
    return csv_contents # 리스트 안에 리스트 구조로 한 줄 씩 담김

def write_csv(self, file_path, file_name, contents):
    with open(f'{file_path}/{file_name}', 'w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(contents)        

def append_csv(self, file_path, file_name, contents):
    with open(f'{file_path}/{file_name}', 'a', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(contents)


