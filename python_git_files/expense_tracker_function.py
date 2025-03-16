def get_expense(expenses, date, description, amount):

	expense = {"date": date, "description": description, "amount": amount}
	expenses.append(expense)
	return "Expense added!"


def display_expense(expenses):
	if len(expenses) == 0:
		return("No expenses recorded, Kindly select :1: to add Expense.")

	else:
		for expense in expenses:
			return (f"{expense['date']},{expense['description']}:, #{expense['amount']:.2f}")



def get_total_expense(expenses):
	if len(expenses) == 0:
		return("No expenses recorded, Kindly select :1: to add Expense.")
	total = 0
	for expense in expenses:
		total += expense['amount']
	return(f"Total Expenses: #{total:.2f}")

	


def main():

	expenses = []

	print("WELCOME TO SEMICOLON EXPRESS TRACKER APP")
	print("-------------------------------------------------")

	while True:
		print("""
1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Exit
""")
    
		choice = int(input("Enter your choice: "))
		while choice not in {1,2,3,4}:
			choice = int(input("Incorrect number selected, kindly enter a correct number!: "))

		if choice == 1:
	
			date = input("Enter the date (YYYY-MM-DD): ")
			description = input("Enter the description: ")
			while type(description) != str:
				description = str(input("Incorrect!!! Re-enter the description: "))
			amount = int(input("Enter the amount: "))
			while amount < 1:
				amount = int(input("Incorrect!!! Kindly enter correct amount: "))
			result = get_expense(expenses, date, description, amount)
			print(result)

		elif choice == 2:

			result = display_expense(expenses)
			print(result)


		elif choice == 3:
			result = get_total_expense(expenses)
			print(result)
		

		elif choice == 4:
			print("Exiting the app. Goodbye!")
			break


main()

