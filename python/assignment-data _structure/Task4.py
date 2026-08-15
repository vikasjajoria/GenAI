# ------crate a list of tuple with name of catalog where each tuple is (product_name , price and category)----------
price_dict = {
    "Apple": 65.50,
    "Shoes": 2000,
    "Phone": 12020,
    "Book": 254.60,
    "Laptop": 45000,
    "Shirt": 350
}

products =["Apple","Shoes","Phone","Book","Laptop","Shirt"]

categories = {
    "Apple": "Fruit",
    "Shoes": "Fashion",
    "Phone": "Electronics",
    "Book": "Education",
    "Laptop": "Electronics",
    "Shirt": "Fashion"
}

product = []

catalog = [(product, price_dict[product], categories[product]) for product in products]

print(catalog)



# --------form catalog, create a new dict category_to_products that map each category to a list of productnames in that categories------

category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category]=[]

    category_to_products[category].append(product)

print(category_to_products)        
