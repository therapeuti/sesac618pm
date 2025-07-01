from animal import Animal

class Panda(Animal):
    _sound = '대나무 냠냠'

    def move(self):
        if self._hp == 0:
            print(f'{self._name}의 에너지가 다 떨어져서 움직일 수 없습니다. HP: {self._hp}')
        else:
            self._hp -= 20
            if self._hp < 0:
                self._hp = 0
                print(f'{self._name}이 움직여서 HP가 {self._hp}이 되었습니다.')
            else:
                print(f'{self._name}이 움직여서 HP가 {self._hp}이 되었습니다.')




      