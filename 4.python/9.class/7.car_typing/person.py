class Person:
    def __init__(self, name: str, age: str) -> None:
        self._name: str = name
        self._age: int = age

    @property #getter
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


    @name.setter
    def age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print('나이는 0보다 커야합니다!')

    @property
    def age(self) -> int:
        return self._age
    
    def greet(self)-> None:
        print(f'나의 이름은 {self._name}이고, 나이는 {self._age}입니다.')
