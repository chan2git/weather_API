import json

def print_us_cities(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    us_cities = [city for city in data if city['country'] == 'US']

    for city in us_cities:
        print(f"City: {city['name']}, {city['state']}")



def print_international_cities(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    international_cities = [city for city in data if city['country'] != 'US']

    for city in international_cities:
        print(f"City: {city['name']}, {city['country']}")

