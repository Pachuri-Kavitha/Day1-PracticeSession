product_id = input()
product_name = input()
category = input()
unit_price = float(input())
quantity = int(input())
reorder_level = int(input())

# Create the fixed product record as a tuple
product = (product_id, product_name, category, unit_price, quantity, reorder_level)

# Access the product ID and product name using indexes
name = product[1]
id = product[0]
# Unpack the complete tuple
a, b, c, d, e, f = product

# Calculate the stock value
stock_value = quantity * unit_price

# Determine the stock status
stock_status = ""
if quantity == 0:
    stock_status = "Out of Stock"
elif quantity >= 0 and quantity <= reorder_level:
    stock_status = "Reorder Required"
else:
    stock_status = "Sufficient Stock"

# Display the processed product record
print(f"Product ID: {id}")
print(f"Product Name: {name}")
print(f"Category: {category}")
print(f"Unit Price: {unit_price:.2f}")
print(f"Available Quantity: {quantity}")
print(f"Stock Value: {stock_value:.2f}")
print(f"Stock Status: {stock_status}")
