class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property #getter
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    @name.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            print('나이는 0보다 커야합니다!')

    @property
    def age(self):
        return self._age
    
    def greet(self):
        print(f'나의 이름은 {self._name}이고, 나이는 {self._age}입니다.')
