import json

file = open("prices.json")
price_list = json.load(file)

for price in price_list:
    print(price["display_name"])