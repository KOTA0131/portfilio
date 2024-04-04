import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text="New Text")

#Button
def button_cilcked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_cilcked)
button.pack()

#Entry入力フィールド




input = tkinter.Entry(width=10)
input.pack()
print(input.get())


window.mainloop()