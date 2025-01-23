'''Write a menu-driven Python program that performs various number-related operations.
The program should use a user-defined function for each task and provide the following options:

1 Check if a number is prime
2 Find the factorial of a number
3 Check whether a number is even or odd
4 Check whether a number is a perfect number
5 Exit the program

The program should continuously display the menu and
execute the chosen option until the user decides to exit.'''
import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the factorial of a number
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Function to check whether a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to check whether a number is a perfect number
def is_perfect(num):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

# Main program
while True:
    print("\nMenu:")
    print("1. Check if a number is prime")
    print("2. Find the factorial of a number")
    print("3. Check whether the number is even or odd")
    print("4. Check whether the number is a perfect number")
    print("5. Exit the program")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    
    elif choice == 2:
        num = int(input("Enter a number to find its factorial: "))
        print(f"The factorial of {num} is {factorial(num)}.")
    
    elif choice == 3:
        num = int(input("Enter a number to check if it's even or odd: "))
        print(f"The number {num} is {even_odd(num)}.")
    
    elif choice == 4:
        num = int(input("Enter a number to check if it's a perfect number: "))
        if is_perfect(num):
            print(f"{num} is a perfect number.")
        else:
            print(f"{num} is not a perfect number.")
    
    elif choice == 5:
        print("Exiting the program. Thank you!")
        break
    
    else:
        print("Invalid choice. Please try again.")
