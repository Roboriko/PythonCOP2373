# This program creates a BankAcct Class that manages a bank account. The program will ask the user to enter their
# account info as well as deposit/withdraw money, change and calculate the interest rate and how much would be earned
# over a number of days and displays the updated balance and interest rate.

# Constant used to calculate interest
DAYS_IN_YEAR = 365


class BankAcct:

    # Initializes the bank account information
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name

        self.account_number = account_number

        self.amount = amount

        self.interest_rate = interest_rate

    # Function to change interest rate
    def set_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Function to deposit money
    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    # Function to withdraw money
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= withdraw_amount

    # Function to see balance
    def get_balance(self):
        return self.amount

    # Function that calculates interest for certain amount of days
    def calculate_interest(self, days):
        interest = self.amount * self.interest_rate * (days / DAYS_IN_YEAR)
        return interest

    # Function that displays account info
    def __str__(self):
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\nCurrent Balance: ${self.amount:.2f}"


# Function that tests the BankAcct class
def test_bank_account():
    print("Let’s set up your bank account.")
    name = input("Account Holder's name: ")
    account_number = input("Account number: ")
    amount = float(input("Starting balance: $"))
    interest_rate = float(input("Interest rate (as a decimal, 0.05+5%): "))

    # Creates the BankAcct object
    account = BankAcct(name, account_number, amount, interest_rate)

    # Displays options for the user to pick from for their bank account
    while True:
        print("\nWhat would you like to do?")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Calculate Interest")
        print("4. Change Interest Rate")
        print("5. Check Balance")
        print("6. Display Account Information")
        print("7. Exit Program")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            deposit_amount = float(input("Please enter the amount you would like to deposit: $"))
            account.deposit(deposit_amount)
            print("Deposit successful.")

        elif choice == "2":
            withdraw_amount = float(input("Please enter the amount you would like to withdraw: $"))
            account.withdraw(withdraw_amount)

        elif choice == "3":
            days = int(input("Please enter the number of days you would like to calculate interest for: "))
            interest = account.calculate_interest(days)
            print(f"Interest earned in {days} days: ${interest:.2f}")

        elif choice == "4":
            new_rate = float(input("Please enter the new desired interest rate (decimal 0.05=5%): "))
            account.set_interest_rate(new_rate)
            print("Interest rate is now updated.")

        elif choice == "5":
            print(f"Current balance: ${account.get_balance():.2f}")

        elif choice == "6":
            print(account)

        elif choice == "7":
            print("Have a great day!")
            break

        else:
            print("Invalid Choice. Please Enter A Number Shown From The List.")


# Runs the program
if __name__ == "__main__":
    test_bank_account()
