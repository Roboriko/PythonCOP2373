# Description:
# This program calculates the total, highest and lowest expense you have by entering the total number of expenses you have
# followed by inputting the type of expense and how much it drains your bank account. The program then analyzes the data
# and displays the financial damage done (Total, Highest, and lowest expense and the amount).

# Imports the reduce function
from functools import reduce


# Asks the user to enter their monthly expenses
def get_expenses():

    expenses = []

    # Asks the user for the amount of expenses they have
    num_expenses = int(input("How many expenses do you have? "))

    # Collects expense data through a loop
    for i in range(num_expenses):
        print(f"\nExpense #{i + 1}:")

        expense_type = input("Enter the type of expense (EX: Rent, Food, Utilities, Car, Insurance, Gambling): ")
        expense_amount = float(input("Amount for this expense: "))

        expenses.append((expense_type, expense_amount))

    return expenses


# Analyzes the expenses
def analyze_expenses(expenses):

    # Calculates total amount using the reduce function
    total = reduce(lambda acc, exp: acc + exp[1], expenses, 0)

    # Finds the highest expense
    highest = max(expenses, key=lambda exp: exp[1])

    # Finds the lowest expense
    lowest = min(expenses, key=lambda exp: exp[1])

    return total, highest, lowest


# Run's the program by collecting the user's expenses they input, analyzes them, and then displays the results
def main():

    print("____Monthly Expense Analyzer____\n")

    # Gets the expenses from the user
    expenses = get_expenses()

    # Analyzes the expenses
    total, highest, lowest = analyze_expenses(expenses)

    # Displays the results
    print("\n- Expense Summary -")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} : ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} : ${lowest[1]:.2f}")



# Run's the program
if __name__ == "__main__":
    main()