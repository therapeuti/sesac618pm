# CSV 파일? comma seperated value 범용적이고. 전통적인...

import csv

file_path = 'test.csv'

data = [
    ['name', 'age', 'city'],
    ['John', 25 ,'Seoul'],
    ['Jane', 30 ,'Busan'],
    ['Bob', 35 ,'Jeju'],
]

print(data)

for i in range(len(data)):
    print(data[i])

with open(file_path,'w',newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    # csv_writer.writerows([['Alice',45,'Suwon']]) # writerows는 2차원 리스트로 작성.... data가 2차원 리스트였으니까....
    csv_writer.writerow(['Alice',45,'Suwon']) 

print('csv 쓰기 완료')

