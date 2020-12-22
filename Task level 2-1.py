import json

file = open("car_model_list_full.json")

car_list = json.load(file)
""" Команда виводить список моделей
for car in car_list:
    print(car["Model"])

"""

# Команда для вивeденння списку моделей вказаного бренду користувачем
# (Зробити  програму для виведення моделей вказаного бренду 
# (наприклад ввів користувач Chevrolet i показало всі авто цього бренду))
"""
enter_brand_by_user = input("Веедіть бренд авто: ")
print("Всі моделі авто: ")
for car in car_list:
    if car["Make"] == enter_brand_by_user:
        print(car["Model"]) 

"""
"""
# Пошук моделі по імені
enter_name_of_car = input("Введіть модель машини: ")
print("Повна інформація про авто")
for car in car_list:
    if car["Model"] == enter_name_of_car:
        print("Рік машини: ", car["Year"])
        print("Марка машини: ", car["Make"])
        print("Модель: ", car["Model"])
        print("Категорія: ", car["Category"])

"""