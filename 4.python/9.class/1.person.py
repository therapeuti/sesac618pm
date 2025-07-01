class Person(): # 클래스명은 대문자로 시작하는게 관행. 객체 안에 있는 함수를 메서드Method라고 부름. 
    def __init__(self, name, age): # 초기화....
        self.name = name # 속성(attribute) - 개별 데이터를 저장하는 공간
        self.age = age # 속성

    # 초중급까지는 잘 안 씀.
    def __str__(self): # 객체를 사람들이 보기 좋게 표현하는 함수
        return f'Person: {self.name}, {self.age}'
    
    # 초중급까지는 전혀 안 씀.
    def __eq__(self, other): # 객체끼리 비교할 때 조건 설정
        return self.name == other.name and self.age == other.age # 내 객체와 다른 객체의 이름과 나이가 같으면 같은 객체로 간주하겠다는 의미


    def greet(self):  # 메서드(객체 함수)
        print(f'안녕하세요, 저는 {self.name}입니다.')

    def ride_car(self): # 메서드
        print('자동차를 탑니다')


# Person 클래스에서 공통 내용이 만들어지고
# 인스턴스는 개별내용...
# 자바의 클래스랑 차이가 있음...

person1 = Person('김태민', 35) # Person 클래스의 객체(인스턴스)를 만듦.
person2 = Person('김태영', 33)
person3 = Person('김하린', 3)
person4 = Person('김태영', 33)

person1.greet()
person1.ride_car()

person2.greet()
person2.ride_car()

person3.greet()
person3.ride_car()

print(person1)


print(person1==person2)
print(person1==person3)
print(person1==person1)
print(person2==person4)
# greet()
# ride_car()