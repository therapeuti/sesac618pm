from abc import ABC, abstractmethod
# 추상클래스 - 필수로 구현해야하는 함수를 지정

class Displayable(ABC):
    @abstractmethod
    def display():
        pass

class User:
    def display(self):
        print('사용자 객체 처리')

class Store:
    def display(self):
        print('상점 객체 처리')

class Item:
    def display(self):
        print('아이템 객체 처리')

class Order:
    # def display_order(self):
    def display(self): # 이걸 강제로 만들도록 함.
        print('주문 객체 처리')

# 걍 출력해주는.. 역할... 디테일은 모름.....
# order의 경우.. 런타임 오류... display()가 강제되어 있찌 않음 => 추상클래스
class DisplayData:
    def __init__(self, data):
        data.display()

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(Order())

# 아래와 같이 개별적으로 호출하지 않고 , 위와 같이 중간 중계자를 통해서 처리하는 구조가 OOP적인 설계
User().display()
Store().display()
Item().display()

