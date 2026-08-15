def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list)/len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

prices = []

while True:
    print("\n--- Price Menu ---")
    print("1. Add price")
    print("2. Show average price")
    print("3. Show highest price")
    print("q. Quit")


    choice = input("Enter your choice....")

    if choice == "1":
        price = float(input("Enter price..."))
        print("Price added successfully")

    elif choice == "2":
        if prices:
            print("Average price", get_average_price)
        else:
            print("No prices avalable")

    elif choice == "3":
        if prices:
            print("Highest price:", get_max_price(prices))
        else:
            print("No prices available.")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")                        

