numbers = [3,5,7,8,9,5,3,1,3,6,3]

def find_me(numbers):
    # 위 목록에서 가장 큰 수를 반환하시오
    numbers.sort()
    return numbers[-1]

print(find_me(numbers))



def find_max2(numbers):
    max_num = 0 # 초기값을 걍 리스트의 첫번째 값으로 정하면 더 간단.... 리스트에 인덱스로 접근할 필요없이 그냥 리스트 값으로 바로 비교 가능.
    for i in range(len(numbers)):
        if i+1 < len(numbers):

            if max_num < numbers[i+1]:
                max_num = numbers[i+1]
    return max_num

print(find_max2(numbers))
print(max(numbers))

