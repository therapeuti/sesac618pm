from abc import ABC, abstractmethod # 추상 클래스로 만들어서 상속 클래스에서 꼭 만들어야할 메서드를 잊지않고 만들도록 강제할 수 있음
# 또는 공통적으로 다 들어가 있는 것들은 공통 변수로 빼거나,,, 공통으로 만들어서 적용할 수도 있음.


class Animal:
    
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._hp: int = 100
        # self._sound = '나랑 놀아줘'

    def speak(self) -> None:
        print(f'{self._name}은 {self._sound}라고 합니다.')

    @abstractmethod
    def move(self) -> None:
        pass

    def feed(self) -> None:
        if self._hp > 50:
            self._hp = 100
            print(f'{self._name}의 에너지가 꽉 찼습니다. {self._hp}')

        else:
            self._hp += 50
            print(f'{self._name}의 에너지가 50 증가 했습니다. {self._hp}')
