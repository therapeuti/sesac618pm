numbers = [1,2,3,4,5,6,7,8,10]
for num in numbers:
    if num%2 == 0:
        print(f'숫자 {num}은 짝수입니다.')
    elif num%2 ==1:
        print(f'숫자 {num}은 홀수입니다.')


def getEvenNumbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

even = getEvenNumbers(numbers)
print(even)

def getGrade(score):
    if score >= 90:
        grade = 'A학점'
    elif score >= 80:
        grade = 'B학점'
    elif score >= 70:
        grade = 'C학점'
    else:
        grade = 'F학점'
    return grade

# 다음 목록에서 성적이 A인 학생만 반환하시오
student = [
    {"이름": "김태민", "점수": 87},
    {"이름": "이수정", "점수": 92},
    {"이름": "박지훈", "점수": 78},
    {"이름": "최민서", "점수": 85},
    {"이름": "정우진", "점수": 90},
    {"이름": "한예슬", "점수": 73},
    {"이름": "오세훈", "점수": 88},
    {"이름": "윤하늘", "점수": 95},
    {"이름": "강도현", "점수": 81},
    {"이름": "서지민", "점수": 76}
]


# def getScore(student):

def studentA(student):
    A_student = []
    for score in student:
        name = score['이름']
        grade = getGrade(score['점수'])
        if grade == 'A학점':
            # print(name)
            A_student.append(name)
    return A_student
    
print(studentA(student))
            
        