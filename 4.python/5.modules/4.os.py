import os

print(os.getcwd()) # 현재 디렉토리를 가져옴. cwd = current working derectory

new_directory = 'sesac1234'
# os.makedirs(new_directory)
# os.mkdir('new directory')
# print('생성완료')

# 시스템 콜이라고 함...
os.chdir(new_directory) # 해당 디렉토리로 이동. 터미널에서 cd와 같은
print(os.getcwd()) # 현재 디렉토리를 가져옴. cwd = current working derectory


os.chdir("..") # 현재 디렉토리에서 상위 디렉토리로 이동.
print(os.getcwd()) # 현재 디렉토리를 가져옴. cwd = current working derectory


os.rmdir(new_directory)
# os.rmdir('new directory')
print('삭제완료')