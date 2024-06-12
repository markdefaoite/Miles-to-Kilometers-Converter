from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    result_label.config(text=km)


#Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Entries
entry = Entry(width=7)
#Add some text to begin with
entry.insert(END, string="0")
entry.grid(row=0, column=1)

#Labels
miles_label = Label(text="miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="Is equal to ")
equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

#Buttons calls action() when pressed
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

# This line must be at the ned of the program
window.mainloop()
