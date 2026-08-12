# Get input from user
name = input("Enter customer name: ")
units = float(input("Enter total units used: "))

# Calculate base charge step by step
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

# Check if surcharge applies
if bill > 1000:
    surcharge = bill * 0.05
else:
    surcharge = 0

# Calculate final total
total = bill + surcharge

# Print results
print("\n--- BILL SUMMARY ---")
print("Customer Name:", name)
print("Units Consumed:", units)
print("Electricity Charge: ₹", bill)
print("Surcharge: ₹", surcharge)
print("Final Bill: ₹", total)