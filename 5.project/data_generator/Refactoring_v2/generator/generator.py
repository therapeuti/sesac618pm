from abc import ABC, abstractmethod
from datetime import datetime
from common_module import *
import random
import csv
import uuid
import sys
import json
import logging

#로깅 설정
logging.basicConfig(level=logging.DEBUG,  # 로깅 레벨 설정. DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL 순으로 레벨이 높음. 설정된 레벨 이상의 로그만 출력됨.im
                    format="%(asctime)s [%(levelname)s] %(message)s", # 로그 출력 형식을 정의(포맷팅). 로그 발생 시각, 로그 레벨 이름, 출력 메시지(사용자가 정의..?) 
                    datefmt='%Y-%m-%d %H-%M-%S') # 로그 발생 시각의 출력 형식을 정의


class Generator(ABC):

    def generate_uuid(self):
        id = uuid.uuid4()
        return id
    
    
    @abstractmethod
    def generate_data(self):
        pass
    
    @abstractmethod
    def generate_dataset(self):
        pass

