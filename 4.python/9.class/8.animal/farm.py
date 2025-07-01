from animal import Animal
from cat import Cat
from dog import Dog
from panda import Panda
from typing import List

# 농장 클래스 Farm
# 농장에 동물을 추가
# add_animal() 함수로 동물을 농장에 추가
# 밥주기 feed_all()  모든 동물 밥주기 -> 에너지 올리기
# 놀기 play_all  모든 동물 놀아주기 -> 에너지 감소
# 보기 show_all 동물의 현재 상태 보기.( 이름, 소리, 에너지)

class Farm:
    def __init__(self, farm_name: str) -> None:
        self._farm_name: str = farm_name
        self._animal_number: int = 0
        self._animal: List[Animal] = []

    def add_animal(self, animal: [Animal]) -> None:
        self._animal.append(animal)
        self._animal_number += 1
        animals = []
        for i in self._animal:
            animals.append(i._name)
        print(f'현재 농장 {self._farm_name}있는 동물들은 {animals}입니다.')


# 밥주기 feed_all()  모든 동물 밥주기 -> 에너지 올리기
# 놀기 play_all  모든 동물 놀아주기 -> 에너지 감소
# 보기 show_all 동물의 현재 상태 보기.( 이름, 소리, 에너지)        
    def feed_all(self) -> None:
        print('-------동물들에게 밥주는 중---------')
        for i in self._animal:
            i._hp += 50
            if i._hp > 100:
                i._hp = 100
                print(f'{i._name}의 에너지가 꽉 찼습니다. HP: {i._hp}')
            else:
                print(f'{i._name}의 에너지가 50 증가 했습니다. {i._hp}')
        
    def play_all(self):
        print('---------- 동물들과 노는 중 ----------')
        for i in self._animal:
            i._hp -= 10
            print(f'{i._name}과 놀아줬습니다. HP: {i._hp}')
        
    def show_all(self):
        print(f'------{self._name}에 있는 동물들의 정보는 다음과 같습니다.------')
        for i in self._animal:
            print(f'{i._name}의 소리는 {i._sound}이고, 현재 HP는 {i._hp}입니다.')