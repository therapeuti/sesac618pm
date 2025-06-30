file_path = 'text.txt'

# 파일 읽을때 모드
# r = 읽기, w = 새로쓰기, a(append) = 이어서 쓰기
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("Hello!\n") # \n 뉴라인 줄바꿈 캐릭터
    file.write("안녕!")
    file.write("\n바이")