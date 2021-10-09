from tkinter import *

window = Tk()

can_nang = Entry(master=window)
can_nang.pack()

chieu_cao = Entry(master=window)
chieu_cao.pack()

bmi_result = Label(master=window,text="Kết quả ")
bmi_result.pack()

def caculate_bmi():
    weight = int(can_nang.get())
    tall = getdouble(chieu_cao.get())

    bmi = round(weight / (tall * tall))
    bmi_result.config(text=str(bmi))

button1 = Button(window, text="click me", command=caculate_bmi)
button1.pack()

window.mainloop()