# -----------map()-----------
price =[100,250,400,1200,50]

gst = lambda price: price + (0.18 * price)

price_with_gst = list(map(gst, price))

print("Original Prices:", price) 
print("Price with gst:", price_with_gst) 