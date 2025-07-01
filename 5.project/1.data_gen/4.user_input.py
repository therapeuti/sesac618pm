from generators.user import *
import sys

class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, bday, gender, address in data:
            print(f'Name: {name}\nBrithdate: {bday}\nGender: {gender}\nAddress: {address}\n')

# 최종 실행
# print(sys.argv) # argv -> 입력인자
# sys.argv[0] # 무조건 실행 파일명
# sys.argv[1] # 첫번째 인자


if len(sys.argv) > 1:
    num_data = int(sys.argv[1])
else:
    num_data = int(input('원하는 데이터 개수를 입력하시오: '))


my_data = DisplayData()
my_data.print_data(num_data)