Python Functions and Price Processing Tasks

This project contains 7 Python practice tasks covering functions, recursion, lambda functions, map(), filter(), and menu-driven programming.

Task 1: Apply Discount

Create a function apply_discount() that returns the price after applying a discount.

Default discount is 5% if no discount is provided.

Discount cannot exceed 60%.

def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60

    discount = price * discount_percent / 100
    return price - discount


print(apply_discount(1000, 10))
print(apply_discount(500))
print(apply_discount(1000, 70))

Task 2: Recursive Factorial

Create a recursive function factorial() that returns the factorial of n.

Handle n == 0 and n == 1.

Print an error message if n is negative.

def factorial(n):
    if n < 0:
        print("Error: Factorial is not defined for negative numbers")
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(0))
print(factorial(-3))

Task 3: GST Using Lambda

Create a lambda function gst that adds 18% GST to a price.

gst = lambda price: price + (0.18 * price)

print(gst(100))

Output:

118.0

Task 4: Map Prices With GST

Use map() with the GST lambda function to generate a new list containing prices after adding 18% GST.

prices = (100, 250, 400, 1200, 50)

gst = lambda price: price + (0.18 * price)

price_with_gst = list(map(gst, prices))

print("Original prices:", prices)
print("Prices after GST:", price_with_gst)

Output:

Original prices: (100, 250, 400, 1200, 50)
Prices after GST: [118.0, 295.0, 472.0, 1416.0, 59.0]

Task 5: Filter Prices

Use filter() to create two lists:

Prices greater than 500

Prices less than or equal to 500

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(
    filter(lambda price: price > 500, prices)
)

less_than_or_equal_500 = list(
    filter(lambda price: price <= 500, prices)
)

print("Prices greater than 500:", greater_than_500)
print("Prices less than or equal to 500:", less_than_or_equal_500)

Output:

Prices greater than 500: [1200, 2000, 850]
Prices less than or equal to 500: [100, 250, 400, 50]

Task 6: Process Prices Using Map and Filter

Create a function process_prices() that:

Takes a list of prices.

Uses map() and lambda to apply a 10% discount to all prices.

Uses filter() to keep only discounted prices above 300.

Returns both discounted_prices and filtered_prices.

def process_prices(prices):
    discounted_prices = list(
        map(lambda price: price - (price * 0.10), prices)
    )

    filtered_prices = list(
        filter(lambda price: price > 300, discounted_prices)
    )

    return discounted_prices, filtered_prices


discounted_prices, filtered_prices = process_prices(
    [100, 500, 900, 50, 750]
)

print("Discounted prices:", discounted_prices)
print("Filtered prices:", filtered_prices)

Output:

Discounted prices: [90.0, 450.0, 810.0, 45.0, 675.0]
Filtered prices: [450.0, 810.0, 675.0]

Task 7: Menu-Driven Price Manager

Create a simple menu-driven program with these options:

1. Add price
2. Show average price
3. Show highest price
q. Quit

def add_price(prices_list, price):
    prices_list.append(price)


def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list)


def get_max_price(prices_list):
    return max(prices_list)


prices = []

while True:
    print("\n--- Price Menu ---")
    print("1. Add price")
    print("2. Show average price")
    print("3. Show highest price")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices, price)
        print("Price added successfully.")

    elif choice == "2":
        if prices:
            print("Average price:", get_average_price(prices))
        else:
            print("No prices available.")

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

Concepts Covered

Python functions

Function arguments

Default arguments

return

Conditional statements

Recursion

Lambda functions

map()

filter()

Lists and tuples

append()

sum()

len()

max()

while loop

User input

Menu-driven programming

Map vs Filter

map()

filter()

Transforms every item

Selects specific items

Returns a result for each item

Returns only matching items

Example: Apply discount

Example: Prices above 300

Conclusion

These 7 tasks provide practice with fundamental Python programming concepts and demonstrate how functions, lambda expressions, map(), 