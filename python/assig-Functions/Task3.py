# ---------lambda function-------------
gst = lambda price: price + (0.18 * price)
print(gst(100))


final_price = lambda price, discount:gst(price) - (gst(price) * discount/100)

print(gst(100,10))