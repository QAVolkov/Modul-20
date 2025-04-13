import json
from collections import defaultdict

with open("orders_july_2023.json", "r") as file:
    orders = json.load(file)

max_price = 0
max_price_order = ''

max_quantity = 0
max_quantity_order = ''

orders_per_day = defaultdict(int)
orders_per_user = defaultdict(int)
user_total_price = defaultdict(int)

total_price = 0
total_quantity = 0
order_count = 0


for order_num, order_data in orders.items():
    date = order_data['date']
    user_id = order_data['user_id']
    quantity = order_data['quantity']
    price = order_data['price']


    if price > max_price:
        max_price = price
        max_price_order = order_num


    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order = order_num


    orders_per_day[date] += 1


    orders_per_user[user_id] += 1


    user_total_price[user_id] += price


    total_price += price
    total_quantity += quantity
    order_count += 1


busiest_day = max(orders_per_day, key=orders_per_day.get)


top_user_orders = max(orders_per_user, key=orders_per_user.get)


top_user_spending = max(user_total_price, key=user_total_price.get)


average_order_price = total_price / order_count if order_count else 0


average_item_price = total_price / total_quantity if total_quantity else 0


print(f'Номер самого дорогого заказа за июль: {max_price_order}, стоимость: {max_price}')
print(f'Номер заказа с самым большим количеством товаров: {max_quantity_order}, количество: {max_quantity}')
print(f'День с наибольшим количеством заказов в июле: {busiest_day}')
print(f'Пользователь с наибольшим количеством заказов за июль: {top_user_orders}')
print(f'Пользователь с самой большой суммарной стоимостью заказов за июль: {top_user_spending}')
print(f'Средняя стоимость заказа в июле: {average_order_price:.2f}')
print(f'Средняя стоимость товаров в июле: {average_item_price:.2f}')