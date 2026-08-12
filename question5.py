def calculate_salary(basic_salary, bonus_percentage=5):
    bonus_amount = (basic_salary * bonus_percentage) / 100
    final_salary = basic_salary + bonus_amount
    return bonus_amount, final_salary


name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

has_special = input("Do you have a special bonus percentage? (yes/no): ").lower()

if has_special == "yes":
    bonus_pct = float(input("Enter bonus percentage: "))
    bonus, total_salary = calculate_salary(basic, bonus_pct)
else:
    bonus_pct = 5
    bonus, total_salary = calculate_salary(basic)

print("\n--- SALARY DETAILS ---")
print("Employee Name:", name)
print("Basic Salary: ₹", basic)
print("Bonus Percentage:", bonus_pct, "%")
print("Bonus Amount: ₹", bonus)
print("Final Salary: ₹", total_salary)