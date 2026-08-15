order_amount = int(input("Enter order amount: "))

if order_amount >= 2000:
    discount_percent = 15
elif 1500 <= order_amount < 2000:
    discount_percent = 10
elif 100 <= order_amount < 1500:
    discount_percent = 7
else:
    discount_percent = 0


discount = order_amount * discount_percent/100

# ------amount after discount-----
subtotal = order_amount-discount

# --------tax after discount----------
tax = subtotal * 5/100

# -------final total------------
final_total = subtotal + tax


print("order amount:", order_amount)
print("discount:", discount)
print("sub total:", subtotal)
print("tax:", tax)
print("final amonut:", final_total)