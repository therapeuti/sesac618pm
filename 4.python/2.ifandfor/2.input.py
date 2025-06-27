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


name = input('입력을 입력하시오: ')
score = int(input('점수를 입력하시오: '))
grade = getGrade(score)

print(f'학생 {name}의 성적은 {grade}입니다')