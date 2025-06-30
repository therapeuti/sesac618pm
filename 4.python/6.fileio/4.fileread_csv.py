# CSV 파일? comma seperated value 범용적이고. 전통적인...

import csv

file_path = 'test.csv'

data = []
with open(file_path,'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # print(row)
        data.append(row)


print(data)



