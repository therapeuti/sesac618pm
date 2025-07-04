from abc import ABC, abstractmethod
# 추상클래스 - 필수로 구현해야하는 함수를 지정

class Displayable(ABC):
    registry = {}

    def __init_subclass__(cls, **kwargs): # 상속클래스가 있으면 자동으로 실행되는 함수
        super().__init_subclass__(**kwargs)
        Displayable.registry[cls] = cls # 상속해간 애들을 registry에 기록

    @abstractmethod
    def display():
        pass

# @register 데코레이터 사용을 더 많이 하는 추세....? 파이써닉한...?
class User(ABC):
    def display(self):
        print('사용자 객체 처리')


class Store(ABC):
    def display(self):
        print('상점 객체 처리')

class Item(ABC):
    def display(self):
        print('아이템 객체 처리')

class Order(ABC):
    # def display_order(self):
    def display(self): # 이걸 강제로 만들도록 함.
        print('주문 객체 처리')

class OrderItem:
    def display(self): 
        print('주문아이템 객체 처리')

# 걍 출력해주는.. 역할... 디테일은 모름.....
# order의 경우.. 런타임 오류... display()가 강제되어 있찌 않음 => 추상클래스
class DisplayData:
    def __init__(self, data):  # 이 클래스를 누가 사용할 수 있는지 알 수 있게..
        handler = Displayable.registry.get(type(data))
        if handler:
            data.display()
        else:
            print('지원하지 않는 타입입니다.')

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(Order())
DisplayData(OrderItem())



