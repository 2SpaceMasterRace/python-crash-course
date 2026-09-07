# Write your solution here

hourly_wage = int(input("Hourly wage:"))
hours_worked = int(input("Hours worked:"))
day = int(input("Day of the week:"))

if day == "Sunday":
    print(f"Daily wages: {(hourly_wage * 2) * hours_worked}")

print(f"Daily wages: {hourly_wage * hours_worked}")