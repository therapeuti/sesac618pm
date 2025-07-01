from generators.user import *


class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, bday, gender, address in data:
            print(f'Name: {name}\nBrithdate: {bday}\nGender: {gender}\nAddress: {address}\n')

num_data = input('원하는 데이터 개수를 입력하세요')
# 최종 실행
my_data = DisplayData()
my_data.print_data(int(num_data))



