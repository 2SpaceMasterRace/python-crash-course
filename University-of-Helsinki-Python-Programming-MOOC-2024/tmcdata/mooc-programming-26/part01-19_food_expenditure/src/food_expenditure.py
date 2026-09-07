# Write your solution here

cafeteria_visit = int(input("How many times a week do you eat at the student cafeteria?"))
cafeteria_expense = float(input("The price of a typical student lunch"))
groceries_expense = float(input("How much money do you spend on groceries in a week?"))

print("Average food expenditure:")
print(f"Daily: {((cafeteria_expense * cafeteria_visit) + groceries_expense)/7} euros")
print(f"Weekly: {(cafeteria_expense * cafeteria_visit) + groceries_expense} euros")