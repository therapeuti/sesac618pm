import os
import zipfile  #빌트인 모듈. zip으로 압축해줌

my_dir = 'sesac1234'

# my_dir 안에 있는 모든 폴더 및 파일을 리스트화


# for filename in os.listdir(my_dir):  
#     print(filename)  
    
# 디렉토리 안의 파일'만' 읽어보기
for filename in os.listdir(my_dir):
    # os.path 자체가 경로를 다루는 함수들의 모음. 
    file_path = os.path.join(my_dir, filename)  #경로를 os에 맞게 결합시킴. my_dir 폴더 이름과 그 안에있는 파일명(filename)을 결합하여 경로주소를 만듦
    # print(file_path)
    if os.path.isfile(file_path): # 해당 경로가 파일인지 확인
        print(filename)
        print(file_path)
