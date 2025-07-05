import csv

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.read(file)
    return csv_reader

def write_csv(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow()
    

# def generate_name(file_path1):

