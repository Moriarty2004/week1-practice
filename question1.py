
name = input("Enter customer name: ")
units = float(input("Enter total units used: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
if bill > 1000:
    surcharge = bill * 0.05
else:
    surcharge = 0
total = bill + surcharge
print("\nBILL SUMMARY")
print("Customer Name:", name)
print("Units Consumed:", units)
print("Electricity Charge: ₹", bill)
print("Surcharge: ₹", surcharge)
print("Final Bill: ₹", total)
