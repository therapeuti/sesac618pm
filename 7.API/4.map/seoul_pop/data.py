# -*- coding: utf-8 -*-

seoul_population_data = {
    "Gangnam-gu": 555731,
    "Gangdong-gu": 472622,
    "Gangbuk-gu": 320773,
    "Gangseo-gu": 602235,
    "Gwanak-gu": 519584,
    "Gwangjin-gu": 373188,
    "Guro-gu": 438956,
    "Geumcheon-gu": 246481,
    "Nowon-gu": 552338,
    "Dobong-gu": 338677,
    "Dongdaemun-gu": 363994,
    "Dongjak-gu": 405006,
    "Mapo-gu": 389061,
    "Seodaemun-gu": 322975,
    "Seocho-gu": 438740,
    "Seongdong-gu": 300794,
    "Seongbuk-gu": 467108,
    "Songpa-gu": 671173,
    "Yangcheon-gu": 471545,
    "Yeongdeungpo-gu": 402024,
    "Yongsan-gu": 245502,
    "Eunpyeong-gu": 490875,
    "Jongno-gu": 157833,
    "Jung-gu": 131362,
    "Jungnang-gu": 419825
}

# District coordinates (latitude, longitude)
seoul_coordinates = {
    "Gangnam-gu": [37.5172, 127.0473],
    "Gangdong-gu": [37.5301, 127.1238],
    "Gangbuk-gu": [37.6396, 127.0257],
    "Gangseo-gu": [37.5509, 126.8495],
    "Gwanak-gu": [37.4784, 126.9516],
    "Gwangjin-gu": [37.5384, 127.0822],
    "Guro-gu": [37.4954, 126.8874],
    "Geumcheon-gu": [37.4569, 126.8956],
    "Nowon-gu": [37.6541, 127.0568],
    "Dobong-gu": [37.6688, 127.0471],
    "Dongdaemun-gu": [37.5744, 127.0398],
    "Dongjak-gu": [37.5124, 126.9393],
    "Mapo-gu": [37.5663, 126.9019],
    "Seodaemun-gu": [37.5794, 126.9368],
    "Seocho-gu": [37.4837, 127.0324],
    "Seongdong-gu": [37.5634, 127.0368],
    "Seongbuk-gu": [37.5894, 127.0167],
    "Songpa-gu": [37.5145, 127.1059],
    "Yangcheon-gu": [37.5170, 126.8664],
    "Yeongdeungpo-gu": [37.5264, 126.8962],
    "Yongsan-gu": [37.5384, 126.9654],
    "Eunpyeong-gu": [37.6176, 126.9227],
    "Jongno-gu": [37.5735, 126.9788],
    "Jung-gu": [37.5641, 126.9979],
    "Jungnang-gu": [37.6063, 127.0925]
}

def get_population_data():
    """Return Seoul population data"""
    return seoul_population_data

def get_coordinates_data():
    """Return Seoul district coordinates data"""
    return seoul_coordinates

def get_district_info(district_name):
    """Return specific district information"""
    if district_name in seoul_population_data:
        return {
            'name': district_name,
            'population': seoul_population_data[district_name],
            'coordinates': seoul_coordinates[district_name]
        }
    return None