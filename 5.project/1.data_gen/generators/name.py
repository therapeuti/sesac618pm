import random

class NameGenerator:
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read().splitlines()
        return data

    
    def generate_name(self):
        return random.choice(self.names)
    