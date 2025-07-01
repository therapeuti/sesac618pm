from animal import Animal

class Cat(Animal):
    def __init__(self, name: str) -> None: # 상속받은거 그대로 사용하는 경우엔 안 해도 됨...
        super().__init__(name)
        self._name: str = name 
        self._hp: int = 100
        self._sound: str = 'Meow'

    def speak(self) -> None:
        print(f'{self._name}은 {self._sound}라고 합니다.')

    def move(self) -> None:
        if self._hp == 0:
            print(f'{self._name}의 에너지가 다 떨어져서 움직일 수 없습니다. HP: {self._hp}')
        elif self._hp < 5:
            self._hp = 0
            print(f'{self._name}이 움직여서 HP가 {self._hp}이 되었습니다.')
        else:
            self._hp -= 5
            print(f'{self._name}이 움직여서 HP가 {self._hp}이 되었습니다.')