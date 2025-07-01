import random
class AddressGenerator:
    def __init__(self, file_path):
        self.city = self.load_from_data(file_path)

    def load_from_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            city = f.read().splitlines()
        return city
    
    def generate_address(self):
        city = random.choice(self.city)
        street_num = random.randint(1,100)
        return f'{street_num} {city}'