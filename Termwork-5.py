'''Create a Python program using Object-Oriented Programming concepts to manage and perform operations on time.
The program should support the following functionalities:

Add Time: Allow the user to input two times in HH:MM:SS format, and add them together using operator overloading.
Convert Time to Seconds: Convert the time objects to total seconds, making it easier to compare or perform other calculations.
Reset Time: Reset the time objects to 00:00:00.
Exit: Allow the user to exit the program.'''

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __add__(self, other):
        """Overload the + operator to add two Time objects."""
        total_seconds = self.__seconds + other.__seconds
        total_minutes = self.__minutes + other.__minutes
        total_hours = self.__hours + other.__hours

        # Calculate overflow for seconds and minutes
        total_minutes += total_seconds // 60
        total_seconds = total_seconds % 60

        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes, total_seconds)

    def __str__(self):
        """Return time in HH:MM:SS format."""
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

    def to_seconds(self):
        """Convert time to total seconds."""
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    def reset(self):
        """Reset the time to 00:00:00."""
        self.__hours, self.__minutes, self.__seconds = 0, 0, 0


# Menu-driven program
time1 = None
time2 = None

while True:
    print("\n1. Add Time")
    print("2. Convert Time to Seconds")
    print("3. Reset Time")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Input times in HH:MM:SS format
        time1_input = input("Enter the first time (HH:MM:SS): ").split(":")
        time2_input = input("Enter the second time (HH:MM:SS): ").split(":")

        # Convert to Time objects
        time1 = Time(int(time1_input[0]), int(time1_input[1]), int(time1_input[2]))
        time2 = Time(int(time2_input[0]), int(time2_input[1]), int(time2_input[2]))

        result = time1 + time2  # Using operator overloading
        print("Sum of time:")
        print(result)  # Uses __str__ method to print

    elif choice == 2:
        if time1 and time2:
            print(f"First time in seconds: {time1.to_seconds()}")
            print(f"Second time in seconds: {time2.to_seconds()}")
        else:
            print("No times added yet. Please add time first.")

    elif choice == 3:
        if time1 and time2:
            time1.reset()
            time2.reset()
            print("Times have been reset to 00:00:00")
        else:
            print("No times added yet. Please add time first.")

    elif choice == 4:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
