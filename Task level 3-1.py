import json
file = open("car_model_list_full.json")
car_list = json.load(file)


# Пошук по частковій назві
search_by_part = input(" Введите частичное название модели авто: ")
for car in car_list:
    if search_by_part == 
        print("Good")