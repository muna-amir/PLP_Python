def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        new_price = price - discount
        return new_price
    else:
        return price
price = float(input("Enter the original price of the product: "))
discount_percent = float(input("Enter the percentage discount: "))
new_price = calculate_discount(price, discount_percent)
if new_price != price:
    print("Final price after applying the discount: ", new_price)
else:
    print("No discount applied. Original price: ", price)
