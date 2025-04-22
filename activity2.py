# Import necessary libraries
from tkinter import *
from datetime import date

# Create window
root = Tk()
root.title('Getting Started with widgets')
root.geometry('400x300')

# Add a widget
# add a label
lb1 = Label(text="hey There!" ,fg="white", bg="#072F5F", height=2, width=300)

# Add Label for getting name as input from user
# Use Entry Widget to creat a text box for user to enter details
name_lb1 = Label(text="full name", bg="#3895D3")
name_entry = Entry()

# function to display a message
def display():

    # Read input given by user
    name = name_entry.get()

    # Declaring a global variable
    # to make it accessible anywhere in the program
    global message
    message = "Welcome to the appliction! \nToday's date is: "
    greet = f"hello{name}\n"

    # Display details in a text box 
    # Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# Add  a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="begin", command=display, height=1, bg="#1261A0", fg="white")


# Organize all the widgets in the window
lb1.pack()
name_lb1.pack()
name_entry.pack()
btn.pack()
text_box.pack()


root.mainloop()