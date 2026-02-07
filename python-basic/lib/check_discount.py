def calculate_discount_price(price, discount_percent):
    discount_amound = price * (discount_percent / 100)
    final_price = price - discount_amound
    return final_price

def check_discount(price):
    if price >= 600000:
        print("The discount is 15")
        discount_price = price - (price * 15 / 100)
        return discount_price
    elif price >= 300000 and price <= 500000:
        print("The discount is 10")
        discount_price = price - (price * 10 / 100)
        return discount_price
    else:
        print("The discount is 7")
        discount_price = price - (price * 7 / 100)
        return discount_price