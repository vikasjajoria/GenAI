class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic method __str__
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator overloading
    def __add__(self, other):
        return self.price + other.price


# Creating two objects
product1 = Product("Laptop", 50000, "Electronics")
product2 = Product("Mobile", 20000, "Electronics")


# Testing __str__()
print(product1)
print(product2)


# Testing __add__()
total_price = product1 + product2

print("Total Combined Price:", total_price)