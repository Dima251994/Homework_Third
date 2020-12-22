""" Варіант без бібліотеки
file = open("car_model_list_full.json")

print(file.read())
"""

import json # Варіант з бібліотекою

file = open("car_model_list_full.json")

car_list = json.load(file)
print(car_list)