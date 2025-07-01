class Person(): # 클래스명은 대문자로 시작하는게 관행. 객체 안에 있는 함수를 메서드Method라고 부름. 
    _count = 0 # 클래스 변수( 공통, 공용 영역에 해당함)
    
    # protected
    #_count =0  
    
    # private  외부에서 접근해서 변경하려는 것을 방지하기 위함. 자바에 public, private, protected 있는 것처럼...?
    #__count = 0 


    def __init__(self, name, age): # 초기화....
        self.name = name # 속성(attribute) - 개별 데이터를 저장하는 공간
        self.age = age # 속성

        # self.count +=1 은 틀린 것...인스턴스의 변수가 됨. 로컬 변수. 클래스 변수가 아님. 

        Person._count += 1 # 인스턴스가 만들어질 때 클래스 변수에 접근해서 1 증가
   
    def greet(self):  # 메서드(객체 함수)
        print(f'안녕하세요, 저는 {self.name}입니다.')

    def ride_car(self): # 메서드
        print('자동차를 탑니다')

    @classmethod # 데코레이터. 함수에 기능을 더해줌. 클래스 메서드임을...
    def get_count(cls): # 클래스 변수에 대한거라 self가 아니라 cls. 클래스 자체에 접근하기 위해 cls라는 클래스 자신을 칭하는 변수를 받아옴
        return cls._count


    # getter, setter 
    # 내부 변수에 저장해서 값을 읽어올 때는 get_name() -> getter
    # 내부변수에 셋팅을 할 때는 set_name() -> setter


person1 = Person('김태민', 35) # 객체를 찍어내는 과정. 실체화 instantiation
print(f'만들어진 사람수 {Person.count}')
print(f'만들어진 사람수 {person1.count}')
person2 = Person('김태영', 33)
person2.count = 5
print(f'만들어진 사람수 {Person.count}')
print(f'만들어진 사람수 {person1.count}')
print(f'만들어진 사람수 {person2.count}')

# person2.get_count() = 5  라고 사용할 수 없음.

person3 = Person('김하린', 3)
print(person3.get_count())

# person3 = {
# 'name':'김하린'
# 'age':3,
# __class__:
# }

print(person3.name)
print(person3.age)
print(person3.__class__)

