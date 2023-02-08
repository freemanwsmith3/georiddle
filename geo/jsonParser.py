import json

file_path = '/home/fsmith/geoRiddle/countries.json'

with open(file_path, 'r') as f:
    data = json.load(f)
    print(data)

