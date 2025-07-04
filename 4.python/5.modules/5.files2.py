import os
import zipfile  #빌트인 모듈. zip으로 압축해줌

my_dir = 'sesac1234'


# 디렉토리 안의 파일'만' 읽어보기
for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    if (os.path.isfile(file_path)):
        # print(filename)
        # 해당파일 압축하기
        zip_filename = f'{file_path}.zip'   # 확장명 zip이 붙은 확장파일명을 생성

        with zipfile.ZipFile(zip_filename, 'w') as zipf: # zip_filename의 이름을 가진 압축파일을 생성
            zipf.write(file_path, arcname=filename) # zip_filename의 압축파일에 file_path의 파일을 추가하고, 파일 이름은 filename으로 함.
            print('f{filename}을 {zip_filename}으로 압축 완료')

        # 원본 파일 삭제
        os.remove(file_path)
        print(f'원본 파일 삭제')
#######################################################################
# import os
# import zipfile
# # 빌트인 모듈중에 zip으로 압축해주는 기능이 있음

# my_dir = 'sesac1234'

# # 디렉토리 안에 파일"만" 읽어오기
# for filename in os.listdir(my_dir):
#     file_path = os.path.join(my_dir, filename)
#     if (os.path.isfile(file_path)):
#         # print(filename)
#         # 해당 파일을 압축하기
#         zip_filename = f"{file_path}.zip"
        
#         # zip으로 압축하기
#         with zipfile.ZipFile(zip_filename, 'w') as zipf:
#             zipf.write(file_path, arcname=filename)
#             print(f"{filename} 을 {zip_filename} 으로 압축 완료함")
#             # 암호화 기능을 추가한다

#         # 원본 파일 삭제
#         os.remove(file_path)
#         print(f"원본 파일 삭제")

#     # 이메일 발송하는 모듈을 가져온다
#     # README.txt 만들고.. 나에게 비트코인을 보내도록 한다.