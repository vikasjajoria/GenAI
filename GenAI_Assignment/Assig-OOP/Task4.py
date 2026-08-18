# ------polymorphism------------

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# Laptop class
class Laptop(Product):

    def get_info(self):
        print("Laptop Details")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# Mobile class
class Mobile(Product):

    def get_info(self):
        print("Mobile Details")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# Creating objects
laptop = Laptop("HP Laptop", 60000, "Electronics")

mobile = Mobile("Samsung Mobile", 25000, "Electronics")


# Store objects in a list
products = [laptop, mobile]


# Polymorphism
for product in products:
    product.get_info()
    print()