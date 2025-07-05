import random
import csv
import uuid
from abc import ABC, abstractmethod
import sys
import json
import logging

#로깅 설정
logging.basicConfig(level=logging.DEBUG,  # 로깅 레벨 설정. DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL 순으로 레벨이 높음. 설정된 레벨 이상의 로그만 출력됨.im
                    format="%(asctime)s [%(levelname)s] %(message)s", # 로그 출력 형식을 정의(포맷팅). 로그 발생 시각, 로그 레벨 이름, 출력 메시지(사용자가 정의..?) 
                    datefmt='%Y-%m-%d %H-%M-%S') # 로그 발생 시각의 출력 형식을 정의


# 비슷한 부분은 상속클래스로 대체..
# 공통으로 사용할 변수는 클래스 변수로 사용.
# 각 제너레이터 파일 실행시 콘솔에 원하느 데이터 개수 입력하면 만들어지도록 수정.

class Generator(ABC):

    def generate_uuid(self):
        id = uuid.uuid4()
        return id
    
    def generate_person_name(self, file_path):
        name_sample = self.read_json(file_path)
        logging.debug(name_sample)
        last_name = random.choice(name_sample['lastname'])
        first_name = random.choice(name_sample['firstname'])
        user_name = last_name + first_name
        logging.debug(user_name)
        return user_name

    def read_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                logging.debug(data)
        return data

    
    def read_csv(self, file_path):
        csv_contents = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # 필드 제목 건너뜀
            for row in csv_reader:
                csv_contents.append(row)
        return csv_contents # 리스트 안에 리스트 구조로 한 줄 씩 담김
    
    def write_csv(self, file_path, contents):
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(contents)
        
    
    def append_csv(self, file_path, contents):
        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(contents)

    @abstractmethod
    def generate_data(self):
        pass
    
    @abstractmethod
    def generate_dataset(self):
        pass



if __name__=='__main__':
    generator = Generator()
    generator.generate_person_name()