from lib.math_lib import sum, sub
from lib.check_discount import calculate_discount_price, check_discount

result_sum = sum(x=1, y=2)
print(result_sum)
print("########################################################################################\n")

# App -> Calculate Discount
# app.py , libs/check_discount.py.
# Looping

# List of original price
cart_prices = [100000, 650000, 800000, 325000, 775000]
discount_rate = 10 # 10% discount

total_cost = 0

for item_price in cart_prices:
    discounted_price = calculate_discount_price(item_price, discount_rate)
    total_cost += discounted_price # Accumulate the total cost

# Print the final total price outside the loop
print(f"Original cart items: {cart_prices}")
print(f"Discount applied: {discount_rate}%")
print(f"Total cost after discount: ${total_cost:.2f}")

print("########################################################################################\n")

shopping_list = [
    {"name":"A", "price": 500000},
    {"name":"B", "price": 250000},
    {"name":"C", "price": 900000},
    {"name":"D", "price": 625000},
    {"name":"E", "price": 475000},
]

for item in shopping_list:
    price = item["price"]
    discount = check_discount(price)
    print(f"Item: {item['name']}, Price: {price}, Discount: {discount}")