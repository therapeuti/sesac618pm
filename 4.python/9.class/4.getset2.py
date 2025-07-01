class Person(): # 클래스명은 대문자로 시작하는게 관행. 객체 안에 있는 함수를 메서드Method라고 부름. 
    def __init__(self, name, age): # 초기화....
        self.__name = name # __는 private 속성이라서 밖엥서 접근하지 못 함.
        self.__age = age # 속성


   
    def greet(self):  # 메서드(객체 함수)
        print(f'안녕하세요, 저는 {self.__name}입니다.')

    def ride_car(self): # 메서드
        print('자동차를 탑니다')

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def sname(self, name):
        self__name = name

    @property
    def get_age(self):
        return self.__age
    
    @name.setter
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print('나이는 0보다 커야합니다.')



person1 = Person('김태민', 35) 
person2 = Person('김태영', 33) 

print(person1.name) # setter/getter를 파이썬 신버전에서 데코레이터로 지정을 했으면, 함수가 아닌 변수철머 쉽게 접근할 수 있음
print(person1.get_age)

# 최신 파이썬 문법으로 짜면, 객체 안의 변수를 자유롭게 바꾸는 것처럼 보이지만. 실제로는 함수를 통해서 에러 처리 등등 통과해서 할당되는 구조임...

