price_dict = {"Apple":65.50, "Shoes":2000, "Phone":12020,"Book":254.60, "Laptop":45000, "Shirt":350}

# ---- add product----
price_dict["Mango"]=100

print(price_dict)

# ------update price-------
price_dict["Apple"]=71.50

print(price_dict)


# ----remove a product by name(handle the case when product does not exists)-------

product = "Phone"

remove_product = price_dict.pop(product, None)

if remove_product is not None:
    print(f"{product} removed successfully")
else:
    print(f"{product} does not exist") 

print(price_dict)       


# -----average price of all products-----

avaerage_price = sum(price_dict.values()) / len(price_dict)

print("Average price:", avaerage_price)


# --------minimum and maximum prices-----------

minimum_price = min(price_dict, key=price_dict.get)
maximum_price = max(price_dict, key=price_dict.get)

print(minimum_price)
print(maximum_price)