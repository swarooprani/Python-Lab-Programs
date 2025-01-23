'''Create a Python program to simulate a bank account system with the following functionalities:
1.	Create Account: Create a new account with a unique account number, account holder's name, and initial balance.
2.	Deposit Money: Deposit money into the account.
3.	Withdraw Money: Withdraw money from the account if sufficient balance exists.
4.	Check Balance: Check the current balance of the account.
5.	Display Account Details: View account details like account number, holder's name, and balance.
6.	Menu-Driven: Implement a menu where users can select options to perform these tasks.
The program should continue running until the user chooses to exit.
'''
class BankAccount:
    # Class variable to generate account numbers
    account_number_counter = 1000

    def __init__(self, account_holder, initial_balance=0):
        # Private attributes (encapsulation)
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__account_number = BankAccount.account_number_counter
        BankAccount.account_number_counter += 1  # Increment to generate the next account number

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: " + str(amount))
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn: " + str(amount))
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    # Method to check balance
    def check_balance(self):
        return self.__balance

    # Method to display account details
    def display_account(self):
        print("Account Number: " + str(self.__account_number))
        print("Account Holder: " + self.__account_holder)
        print("Balance: " + str(self.__balance))

    # Method to get account number (not directly accessible)
    def get_account_number(self):
        return self.__account_number


# Main program with menu
accounts = {}

while True:
    print("\nMenu:")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_holder = input("Enter the account holder's name: ")
        initial_balance = float(input("Enter initial balance (default is 0): "))
        account = BankAccount(account_holder, initial_balance)
        accounts[account.get_account_number()] = account
        print("Account created successfully! Account Number: " + str(account.get_account_number()))

    elif choice == 2:
        account_number = int(input("Enter account number: "))
        if account_number in accounts:
            amount = float(input("Enter the amount to deposit: "))
            accounts[account_number].deposit(amount)
        else:
            print("Account not found.")

    elif choice == 3:
        account_number = int(input("Enter account number: "))
        if account_number in accounts:
            amount = float(input("Enter the amount to withdraw: "))
            accounts[account_number].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == 4:
        account_number = int(input("Enter account number: "))
        if account_number in accounts:
            balance = accounts[account_number].check_balance()
            print("Current Balance: " + str(balance))
        else:
            print("Account not found.")

    elif choice == 5:
        account_number = int(input("Enter account number: "))
        if account_number in accounts:
            accounts[account_number].display_account()
        else:
            print("Account not found.")

    elif choice == 6:
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
