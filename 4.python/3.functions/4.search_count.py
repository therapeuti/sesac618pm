numbers = [1,3,5,7,9,11,13,15,17,19]

# 원하는 숫자를 찾으면 해당 인덱스를 반환, 없으면 -1 반환
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
        
    return -1


target = 3
print(linear_search(numbers, target))

def binary_search(numbers, target):
    # len(numbers)/2
    

