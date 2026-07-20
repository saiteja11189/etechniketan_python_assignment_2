products = {
    'soap': 50, 
    'oil': 200, 
    'laptop': 60000, 
    'phone': 25000, 
    'mouse': 500
}

costliest_product = None
max_price = 0

# Find the product with the maximum price
for product, price in products.items():
    if price > max_price:
        max_price = price
        costliest_product = product

print(f"Costliest product is {costliest_product}.")
