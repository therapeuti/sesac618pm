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



    # getter, setter 
    # 내부 변수에 저장해서 값을 읽어올 때는 get_name() -> getter
    # 내부변수에 셋팅을 할 때는 set_name() -> setter


person1 = Person('김태민', 35) # 객체를 찍어내는 과정. 실체화 instantiation
person2 = Person('김태영', 33) # 객체를 찍어내는 과정. 실체화 instantiation

print(person1.__name) 
person1.set_name('김하린')
print(person1.__name) 
print(f'나이는 {person1.get_age()}입니다.')
person1.set_age(3)
print(f'나이는 {person1.get_age()}입니다.')
