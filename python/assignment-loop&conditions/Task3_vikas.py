orders = []

while True:
    print("1. Add Order")
    print("2. Show order and total")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        order_amount = int(input("Enter order amount: "))


        if order_amount <= 0:
            print("Invalid order amount")
            continue

        orders.append(order_amount)
        print("Ordered added successfully")

    elif choice == "2":
        if len(orders) == 0:
            print("No order found.")
            continue

        total = 0


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

            total += final_amount

            print(order_amount, "       ", discount_percent, "%       ", final_amount)

        print("------------------------------------------")
        print("Total:", total)


    elif choice == "q":
        print("program ended")
        break

    else:
        print("Invalid choice")
        continue    

