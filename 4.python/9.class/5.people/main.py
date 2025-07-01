# import person
from person import Person
from student import Student
from employee import Employee

alice = Person('Alice',23)
alice.greet()

bob = Person('Bob',21)
bob.greet()
bob.name = 'BOB'
bob.greet()

tom = Student('Tom', 33, 12345)
tom.greet()
tom.study()

charlie = Employee('Charlie', 35, 'Sesac')
charlie.greet()
charlie.work()