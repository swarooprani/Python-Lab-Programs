'''Create a GUI application using Tkinter to design the form that read quantity of products purchased
and perform the actions mentioned below.

● Price of Product1=Rs.500/unit
● Price of Product2=Rs.50/unit upto 50 units, otherwise it is Rs.45
● Price of Product3=Rs.100/unit and minimum quantity to buy is 10 units
● When the Compute Bill button is clicked, the final billing amount should be displayed'''
from tkinter import *
from tkinter import messagebox

def billing():
    p1 = int(product1_entry.get())
    p2 = int(product2_entry.get())
    p3 = int(product3_entry.get())

    p1_total = p1 * 500

    if p2 <= 50:
        p2_total = p2 * 50
    else:
        p2_total = p2 * 45

    if p3 >= 10:
        p3_total = p3 * 100
    else:
        p3_total = 0

    total = p1_total + p2_total + p3_total

    # Create the message to display in the message box
    message = f"Product 1: {p1_total}\n"
    message += f"Product 2: {p2_total}\n"
    message += f"Product 3: {p3_total}\n"
    message += f"Total: {total}"

    # Show the message box with the billing details
    messagebox.showinfo("Billing Details", message)

window = Tk()
window.title("Billing")
window.geometry('300x300')

product1_label = Label(window, text="Product1")
product1_label.grid(row=0, column=0)

product2_label = Label(window, text="Product2")
product2_label.grid(row=1, column=0)

product3_label = Label(window, text="Product3")
product3_label.grid(row=2, column=0)

product1_entry = Entry(window)
product1_entry.grid(row=0, column=1)

product2_entry = Entry(window)
product2_entry.grid(row=1, column=1)

product3_entry = Entry(window)
product3_entry.grid(row=2, column=1)

compute_button = Button(window, text="Compute Bill", command=billing)
compute_button.grid(row=3, column=1)

window.mainloop()
