x = 5
y = "hello"
z = [1,2,3]

print(type(x))
print(type(y))
print(type(z))


print(y.upper())
# print(x.upper())
# 각 변수 타입은 클래스로 만들어져 있고, 그 안에 있는 함수를 통해서 세부 클래스의 함수들이 동작함.
# str 타입에 사용할 수 있는 함수들이 str클래스에 지정되어있어서 str변수에 str클래스의 함수들을 사용할 수 있음. 다르 ㄴ타입은 안 됨.


#클래스에 대한 인스턴스들 생성.... instantiation 객체 생성...? 객체의 인스턴스를 생성.. ㄱ

print(isinstance(x, int)) # x는 int로 만들어진거야?
print(isinstance(y, int))
print(isinstance(y, str))

print(isinstance(x, (str, int))) # x는 str이거나 int야?

