orders = [1200, 2500, 800, 1750, 3000]

total_discount = 0
discount_orders = 0

print("Order Amount | Discount % | Final Amount")
print("------------------------------------------")

for order_amount in orders:

    if order_amount >= 2000:
        discount_percent = 15
    elif 1500 <= order_amount < 2000:
        discount_percent = 10
    elif 1000 <= order_amount < 1500:
        discount_percent = 7
    else:
        discount_percent = 0

    discount = order_amount * discount_percent / 100

    subtotal = order_amount - discount

    tax = subtotal * 5 / 100

    final_amount = subtotal + tax

    total_discount += discount

    if discount > 0:
        discount_orders += 1

    print(order_amount, "       ", discount_percent, "%       ", final_amount)


print("------------------------------------------")
print("Total Discount:", discount)
print("Orders receiving discount:", discount_orders)