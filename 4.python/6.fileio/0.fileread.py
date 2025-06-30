file_path = 'file.txt'

file = open(file_path, 'r') # file을 file descriptor라고 부름 FD

contents = file.read() # FD로 파일을 읽고 쓴다.

file.close() # 마지막에 파일을 닫아줘야함.