from tkinter import *
import cv2
from tkinter import messagebox

root = Tk()
root.geometry("290x500")
root.title("locker")
root.iconbitmap('icon.png')
root.resizable(False, False)

title = Label(root, text='screen loock', fg='white', bg='#D82148', font=('Stencil', 21))
title.pack(fill=X)

def one():  En1.insert(END,1)
def tow():  En1.insert(END,2)
def three(): En1.insert(END,3)
def four(): En1.insert(END,4)
def five(): En1.insert(END,5)
def six(): En1.insert(END,6)
def seven():En1.insert(END,7)
def eight():En1.insert(END,8)
def nine():En1.insert(END,9)
def zero():En1.insert(END,0)
def reset():En1.delete(0,END); erorr1.place(x=1200,y=1200)




def ok():
    passord = En1.get()
    if passord == '123456':
        win = Tk()
        win.geometry("290x20")
        win.title('marwan')
        text = Label(win, text="weolcome")
        text.pack()
        win.mainloop()
    else:
        global erorr1
        erorr1 = Label(F1, text="erorr passord!!", fg='red', bg='white')
        erorr1.place(x=100, y=100)
        s = cv2.VideoCapture(0)
        ret, image = s.read()
        cv2.imwrite('lock.png', image)
        del(s)

F1 = Frame(root, bg='white')
F1.place(x=1, y=38, width=298, height=460)
title1 = Label(F1, text='Enter password', fg="black", bg='white', font=('Stencil', 15))
title1.place(x=55, y=10)
En1 = Entry(F1, justify=CENTER, font=('impact', 25), bd=2, relief=RIDGE, width=10, bg="white", fg='#D82148')
En1.place(x=50, y=50)

# إضافة الأزرار الرقمية وأزرار التحكم
buttons = [
('1',one,20,130),('2',tow,110,130),('3',three,200,130),('4',four,20,215),('5',five,110,215),(6,six,200,215),
('7',seven,20,300),('8',eight,110,300),(9,nine,200,300),('0',zero,110,385),
('✔',ok,200,385),('X',reset,20,385),
]


for (text, command, x, y) in buttons:
    Button(F1, text=text, font=('Stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=command).place(x=x, y=y)

root.mainloop()