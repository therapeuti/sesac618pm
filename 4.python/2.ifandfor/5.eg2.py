users = [
    {'name':"Alice", 'age':25, 'location':'Seoul','car':'BMW'},
    {'name':"Bob", 'age':30, 'location':'Busan','car':'Mercedes'},
    {'name':"Charlie", 'age':35, 'location':'Daegu','car':'Audi'},
    {'name':"Charlie", 'age':40, 'location':'Suwon','car':'Audi'},
    {'name':"Bob", 'age':40, 'location':'Jeju','car':'Audi'}
]


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
print('-'*30)


def find_user3_simple(name=None, age=None):
    result = []
    for u in users:
        if name is not None and age is not None:
            if u['name'] == name and u['age' == age]:
                result.append(u)
        elif name is not None:
            if u['name'] == name:
                result.append(u)
        elif age is not None:
            if u['age'] == age:
                result.append(u)
    return result

print('-'*30)
print(find_user3('Bob',30))
print(find_user3(name='Charlie', age=40))
print(find_user3(name='Charlie'))
print(find_user3(age=25))
print('-'*30)

