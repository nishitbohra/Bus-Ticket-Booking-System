from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Bus Ticket Booking System")
root.geometry("400x275")

# Label
label1 = Label(root, text="Booking Page", font=("Times New Roman", 18))
label1.grid(row=0, column=1)

# Name Label and Entry
name_label = Label(root, text="Name:")
name_label.grid(row=1, column=0)

name_entry = Entry(root)
name_entry.grid(row=1, column=1)

# Age Label and Entry
age_label = Label(root, text="Age:")
age_label.grid(row=2, column=0)

age_entry = Entry(root)
age_entry.grid(row=2, column=1)

# Gender Label and Entry
gender_label = Label(root, text="Gender:")
gender_label.grid(row=3, column=0)

gender_entry = Entry(root)
gender_entry.grid(row=3, column=1)

# Source Label and Entry
source_label = Label(root, text="Source:")
source_label.grid(row=4, column=0)

source_entry = Entry(root)
source_entry.grid(row=4, column=1)

# Destination Label and Entry
destination_label = Label(root, text="Destination:")
destination_label.grid(row=5, column=0)

destination_entry = Entry(root)
destination_entry.grid(row=5, column=1)


# Bus Type Label and Drop-down Menu
bus_type_label = Label(root, text="Bus Type:")
bus_type_label.grid(row=6, column=0)

bus_type_options = ["AC", "Non-AC"]
bus_type_var = StringVar(root)
bus_type_var.set(bus_type_options[0])

bus_type_menu = OptionMenu(root, bus_type_var, *bus_type_options)
bus_type_menu.grid(row=6, column=1)
# Book Ticket Function
def book_ticket():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    source = source_entry.get()
    destination = destination_entry.get()

    if name == "" or age == "" or gender == "" or source == "" or destination == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        with open("bookings.txt", "a") as file:
            file.write(f"{name}, {age}, {gender}, {source}, {destination}\n")
        messagebox.showinfo("Success", "Ticket booked successfully!")

# Cancel Ticket Function
def cancel_ticket():
    name = name_entry.get()
    with open("bookings.txt", "r") as file:
        lines = file.readlines()
    with open("bookings.txt", "w") as file:
        for line in lines:
            if name not in line:
                file.write(line)
    messagebox.showinfo("Success", "Ticket canceled successfully!")

# Display Bookings Function
def display_bookings():
    with open("bookings.txt", "r") as file:
        bookings = file.read()
        messagebox.showinfo("Bookings", bookings)


# Check Availability Function
def check_availability():
    with open("bookings.txt", "r") as file:
        num_entries = len(file.readlines())
    num_available = 50 - num_entries
    messagebox.showinfo("Availability", f"{num_available} seats available")


# Book Ticket Button
book_button = Button(root, text="Book Ticket", command=book_ticket)
book_button.grid(row=17, column=0)

# Cancel Ticket Button
cancel_button = Button(root, text="Cancel Ticket", command=cancel_ticket)
cancel_button.grid(row=17, column=1)

# Check Availability Button
check_button = Button(root, text="Check Availability", command=check_availability)
check_button.grid(row=25, column=1)

# Display Bookings Button
display_button = Button(root, text="Display Bookings", command=display_bookings)
display_button.grid(row=17, column=2)

#List of Buses Available Button
def list_buses():
    # Read bus data from file
    with open("buses.txt", "r") as f:
        buses = f.read()
    
    # Show bus data in message box
    messagebox.showinfo("Buses Available", buses)

buses_button = Button(root, text="Buses Available", command=list_buses)
buses_button.grid(row=25, column=0)
root.mainloop()

root.mainloop()
