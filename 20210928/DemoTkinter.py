from tkinter import  *
window = Tk()

label1 = Label(master=window, text="Hello Tkinter")
label1.pack(side=LEFT)
label2 = Label(master=window, text="Hello Tkinter2")
label2.pack(side=RIGHT)

def hello_world():
    print("Hello World")
    label1.config(text="Who ???")

button1 = Button(window, text="click me", command=hello_world)
button1.pack()

window.mainloop()