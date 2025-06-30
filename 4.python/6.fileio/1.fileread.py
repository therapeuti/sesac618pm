file_path = 'text.txt'

# 파일 읽을때 모드
# r = 읽기, w = 새로쓰기, a(append) = 이어서 쓰기
with open(file_path, 'r', encoding='utf-8') as file:
    contents = file.read()
print("파일내용 : ", contents)