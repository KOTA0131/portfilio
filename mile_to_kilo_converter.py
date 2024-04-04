from tkinter import *

window = Tk()
window.title("mile_to_kilo_converter")
window.minsize(width=400, height=150)

mile = Label(text="Miles", font=("Arial", 12, "bold"))
mile.grid(column=2, row=0)

equal = Label(text="is equal to", font=("Arial", 12, "bold"))
equal.grid(column=0, row=1)

km = Label(text="Km", font=("Arial", 12, "bold"))
km.grid(column=2, row=1)

score = Label(text="0", font=("Arial", 12, "bold"))
score.grid(column=1, row=1)

def button_clicked():
    aa = int(input.get()) * 1.6
    score.config(text=aa)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


input = Entry()
input.grid(column=1, row=0)






window.mainloop()