expenses = []
salary_income = int(input("Enter your income: "))
expense_limit = int(input("Enter your expense limit: "))
total_expenses_count = int(input("Enter the number of expenses: "))

for i in range(1, total_expenses_count + 1):
    expense = int(input(f"Enter expense {i}: "))
    expenses.append(expense)

total_expenses = sum(expenses)
savings = salary_income - total_expenses

print(f"\nTotal Income: {salary_income}")
print(f"Total Expenses: {total_expenses}")
print(f"Total Savings: {savings}")

if total_expenses > expense_limit:
    print("You are Overspending!")
else:
    print("Good Budget Management!")
