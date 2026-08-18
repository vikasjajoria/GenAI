# ------------Singlr Level Inheritance-------------

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)


# class class

class ElecttronicProduct(Product):

    def __init__(self,name,price,category,warranty_years):

        # ------calling parent calass constructor---------
        super().__init__(name,price,category)

        # -------additional attribute----------
        self.warrenty_years=warranty_years


    #--------overriding parent method ---------
    def get_info(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("Warranty:", self.warranty_years, "years")           



laptop=ElecttronicProduct("Acer laptop",50000,"Electronics",3)

laptop.get_info()


