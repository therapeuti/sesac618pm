from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._hp: int = 100
    
    @abstractmethod
    def speak(self):
        print('동물이 말을 하네')

    def move(self):
        print('동물이 움직이네')

    def feed(self, food: str) -> None:
        self._hp += 50
        print('동물이 먹이를 먹어 hp가 50 증가함.')