def calculate_bill(price, quantity):
    total = price * quantity
    if total >= 2000:
        discount = total * 0.10
    else:
        discount = 0
    final_amount = total - discount
    return total, discount, final_amount


item_name = input("Enter product name: ")
item_price = float(input("Enter price: "))
item_qty = int(input("Enter quantity: "))

total, discount, final_amount = calculate_bill(item_price, item_qty)

print("SHOPPING BILL")
print("Product Name:", item_name)
print("Price: ", item_price)
print("Quantity:", item_qty)
print("Total Amount: ", total)
print("Discount: ", discount)
print("Final Amount: ", final_amount)