try:
    with open('hello.txt','r') as file:
        contents = file.read()
        print("파일 내용 : ", contents)
except FileNotFoundError as e:
    print(e, "파일이 존재하지 않음")
except IOError as e:
    print(e, '파일을 읽을 수 없음')
except:

    print('알 수 없는 오류')
