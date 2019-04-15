import re, json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {item: [quantity, price, buyer, date]}
    with open("write.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

a = write_order_to_json('товар2', '5', '5р', 'Иванов', '10.12.2018')
