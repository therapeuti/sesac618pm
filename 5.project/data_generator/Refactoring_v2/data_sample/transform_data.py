import logging
import json
import csv
import pandas as pd
from collections import defaultdict

#로깅 설정
logging.basicConfig(level=logging.DEBUG,  # 로깅 레벨 설정. DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL 순으로 레벨이 높음. 설정된 레벨 이상의 로그만 출력됨.im
                    format="%(asctime)s [%(levelname)s] %(message)s", # 로그 출력 형식을 정의(포맷팅). 로그 발생 시각, 로그 레벨 이름, 출력 메시지(사용자가 정의..?) 
                    datefmt='%Y-%m-%d %H-%M-%S') # 로그 발생 시각의 출력 형식을 정의
def transform_name_sample():
    firstname = 'firstname_sample.csv'
    lastname = 'lastname_sample.csv'

    name_sample = {'firstname':[],
                'lastname': []}

    with open(firstname, 'r', encoding='utf-8') as f:
        row = f.read().splitlines()
        logging.debug(f'splitline()으로 이름 데이터 가져옴: {row}')
        name_sample['firstname'] = row[1:]
        logging.debug(f'splitline()으로 데이터 가져옴: {name_sample}')

    with open(lastname, 'r', encoding='utf-8') as f:
        row = f.read().splitlines()
        logging.debug(f'splitline()으로 성씨 데이터 가져옴: {row}')
        name_sample['lastname'] = row[1:]
        logging.debug(f'최종적으로 name_sample 확인: {name_sample}')


    with open('name_sample.json', 'w', encoding='utf-8') as f:
        json.dump(name_sample, f, ensure_ascii=False, indent=4)   # 한글 그대로 저장하기 위해서 ensure_ascii=False 필요
        logging.debug('json파일로 저장됨. 확인해봐!')

def item_transform_to_json():
    item_data = defaultdict(list)
    item_df = pd.read_csv('item_sample.csv', encoding='utf-8')
    logging.debug(item_df.head())
    logging.debug(item_df.info())
    
    item_type = item_df['type'].unique()
    logging.debug(item_type)

    for type in item_type:
        item_data[type] = item_df[item_df['type']==type][['item','price']].to_dict(orient='records')
        logging.debug(item_data)

    with open('item_sample.json', 'w', encoding='utf-8') as file:
        json.dump(item_data, file, ensure_ascii=False, indent=4)


# item_transform_to_json()


# item_df = pd.read_csv('item_sample.csv', encoding='utf-8')
# item_df.to_json('to_json.json', orient='records', force_ascii=False, indent=4)

def address_transform_to_json():
    address_df = pd.read_csv('address_sample.csv', encoding='utf-8')
    logging.debug(address_df.info())
    logging.debug(address_df.head())
    # address = address_df.groupby(by='시도').apply(lambda x: x.to_dict(orient='records')).to_dict()
    # address = address_df.groupby(by='시도').apply(lambda x: x.groupby(by='시군구').apply(lambda y: y.to_dict()).to_dict()).to_dict()
    cities = address_df['시도'].unique()
    districts = address_df['시군구'].unique()
    city_to_dict = defaultdict(list)
    for city in cities:
        logging.debug(city)
        address_in_city = address_df[address_df['시도'] == city][['시군구','도로명']]
        logging.debug(address_in_city.head())
        districts_to_dict = defaultdict(list)
        city_to_dict[city] = districts_to_dict
        for district in districts:
            districts_to_dict[district] = address_in_city[address_in_city['시군구'] == district]['도로명'].to_list()
        logging.debug(districts_to_dict)
        logging.debug(city_to_dict)

    with open('address_to_json.json', 'w', encoding='utf-8') as file:
        json.dump(city_to_dict, file, ensure_ascii=False, indent=4)




address_transform_to_json()