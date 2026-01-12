employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
rating = int(input("Enter Performance Rating (1-5): "))

bonus = 0

if rating == 5:
    bonus = salary * 0.20
elif rating == 4:
    bonus = salary * 0.15
elif rating == 3:
    bonus = salary * 0.10
else:
    bonus = 0

final_salary = salary + bonus

print("\n---- Bonus Evaluation ----")
print("Employee Name       :",employee_name)
print("Performance Rating  :",rating)
print("Bonus Amount        :$", bonus)
print("Final Salary        :$", final_salary)
