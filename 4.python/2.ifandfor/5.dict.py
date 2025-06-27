users = [
    {'name':"Alice", 'age':25, 'location':'Seoul','car':'BMW'},
    {'name':"Bob", 'age':30, 'location':'Busan','car':'Mercedes'},
    {'name':"Charlie", 'age':35, 'location':'Daegu','car':'Audi'},
    {'name':"Charlie", 'age':40, 'location':'Suwon','car':'Audi'},
    {'name':"Bob", 'age':40, 'location':'Jeju','car':'Audi'}
]

#사용자 이름 기반으로 해당 사용자 정보를 가져오는 코드 구현하기

for u in users:
    print(u)

print('-'*10)
def find_user(name):
    for u in users:
        if u['name'] == name:
            return u


print(find_user('Bob'))
print('-'*10)


def find_users(name):
    findedUsers = []
    for u in users:
        if u['name'] == name:
            findedUsers.append(u)
    return findedUsers

print(find_users('Bob'))
print('-'*10)

def find_users_caseinsensitive(name):
    findedUsers = []
    for u in users:
        if u['name'].lower() == name.lower():
            findedUsers.append(u)
    return findedUsers

print(find_users_caseinsensitive('bob'))
print('-'*10)

def find_user2(name,age):
    user_list = []
    for u in users:
        # if (u['name'] == name) & (u['age']== age): # 비트 연산자 &, ||가 논리연산자처럼 쓰이는 경우도 있으나 아닌 경우도 있고, 우선순위가 다름.
        if (u['name'] == name) and (u['age']== age): # 이게 가장 파이썬스러운 표현. 논리 연산자 and, or
            user_list.append(u)
    return user_list

print(find_user2('Alice', 25))


def find_user3(name=None, age=None):
    result = []
    for u in users:
        if name:
            if u['name'] == name:
                if age:
                    if u['age'] == age:
                        # 이름, 나이 둘 다 매치
                        result.append(u)
                else:
                    result.append(u)
        elif age:
            if u['age'] == age:
                result.append(u)
    return result

print('-'*30)
print(find_user3('Bob',30))
print(find_user3(name='Charlie', age=40))
print(find_user3(name='Charlie'))
print(find_user3(age=25))
