def remove_duplication(numbers):
    result = []
    for num in numbers:
        # if num in result: # result 리스트에 없으면을 어떻게 표현하지ㅣㅣ?? not in
        # 파이썬스러운 코드
        # if num not in result:   
        #     result.append(num)




        # 레거시한 C언어스러운 코드
        yes = True
        for i in result:
            if i != num: # 리스트 내 숫자가 결과 리스트 안에 없으면 결과 리스트에 넣기
                yes = True ## False
        if yes == True:        
            result.append(num) ## 애초에 리스트 안에 데이터가 없어서 비교가 안 되나?
            


    return result


numbers = [3,2,7,9,8,6,5,3,6,7,9,0,2,2,1,3,6,8]

print(remove_duplication(numbers))