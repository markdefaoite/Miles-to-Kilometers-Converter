from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=200, height=200)

#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
entry.grid(row=1, column=2)


#Labels
miles_label = Label(text="miles")
miles_label.grid(row=1, column=3)

equal_label = Label(text="Is equal to ")
equal_label.grid(row=2, column=1)

result_label = Label(text="0")
result_label.grid(row=2, column=2)

km_label = Label(text="KM")
km_label.grid(row=2, column=3)

#Buttons
def action():
    miles = int(entry.get())
    km = miles * 1.609
    result_label.config(text=km)

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=3, column=2)


# This line must be at the ned of the program
window.mainloop()