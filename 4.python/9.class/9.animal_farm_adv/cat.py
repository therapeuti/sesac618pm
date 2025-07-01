from animal import Animal

class Cat(Animal):
    # sound = 'Meow' # 모든 고양이의 소리가 같은 경우
    _sound = 'Meow'
    
    # def __init__(self, name: str) -> None: # 상속받은거 그대로 사용하는 경우엔 안 해도 됨...
    #     super().__init__(name)
    #     self._name: str = name 
    #     self._hp: int = 100
    #     self._sound: str = 'Meow'  # 고양이마다 사운드 다르게 할거면 이렇게 하고 모두 똑같게 할 거면 클래스 변수로 넣는게 나음.

    # def speak(self) -> None:
    #     print(f'{self._name}은 {_sound}라고 합니다.')

    def move(self) -> None:
        if self._hp == 0:
            print(f'{self._name}의 에너지가 다 떨어져서 움직일 수 없습니다. HP: {self._hp}')
        elif self._hp < 5:
            self._hp = 0
            print(f'{self._name}이 움직여서 HP가 {self._hp}이 되었습니다.')
        else:
            self._hp -= 5
            print(f'{self._name}이 움직여서 HP가 {self._hp}이 되었습니다.')

        