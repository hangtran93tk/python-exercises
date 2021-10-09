from tkinter import  *
window = Tk()
entry1 = Entry(master=window)
entry1.pack()
label1 = Label(master=window, text="Hello Tkinter")
label1.pack(side=LEFT)
label2 = Label(master=window, text="Hello Tkinter2")
label2.pack(side=RIGHT)

def hello_world():
    my_input = entry1.get()
    print("Hello World")
    label1.config(text=my_input)

button1 = Button(window, text="click me", command=hello_world)
button1.pack()

window.mainloop()