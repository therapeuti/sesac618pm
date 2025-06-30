# CSV 파일? comma seperated value 범용적이고. 전통적인...

import csv

file_path = 'test.csv'

data = [
  {'name':'John','age': 25,'city':'Seoul'},
  {'name':'Jane','age': 30,'city':'Busan'},
  {'name':'Bob','age': 35,'city':'Jeju'},
  {'name':'Taemin','age': 35,'city':'Suwon'},
]

# print(data)

for person in data:
    # print(person)
    for key, value in person.items():
        print(f'키는 {key}, 값은 {value}')
    # print(f'이름은 {person['name']}, 나이는 {person['age']}')

with open(file_path, 'w', newline='') as file:
    headers = ['name', 'age', 'city']
    # headers = data[0]
    csv_writers = csv.DictWriter(file, fieldnames=headers)
    csv_writers.writeheader()
    csv_writers.writerows(data)





# with open(file_path,'w',newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)

print('csv 쓰기 완료')

