from person import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # 부모 객체를 불러서 그것을 통해 초기화
        self._student_id = student_id

    def study(self):
        print(f'{self.name}은 공부하고 있습니다. 학번은 {self._student_id}') # getter로 이름 가져옴.
        # print(f'{self._name}은 공부하고 있습니다. 학번은 {self._student_id}) 셀프변수로 가져옴
