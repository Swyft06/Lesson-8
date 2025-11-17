from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("Quiz")
root.geometry("400x400")

def Correct():
    tkinter.messagebox.showinfo("Correct",'Your answer is Correct!')



def Incorrect():
    tkinter.messagebox.showinfo("Incorrect",'Your answer is incorrect')


title = Label(root,text = "Quiz",font = ('calibri',20,'normal'))
title.pack()

q_l = Label(root,text="1. What is 15*5?",font = ('calibri',15,'normal'))
q_l.place(y=50)

btn1 = Button(root,text = "35",font = ('calibri',15,'normal'),command=Incorrect)
btn1.place(x=10,y=80)

btn2 = Button(root,text = "75",font=('calibri',15,'normal'),command=Correct)
btn2.place(x=80,y=80)

btn3 = Button(root,text='85',font = ('calibri',15,'normal'),command=Incorrect)
btn3.place(x=150,y=80)

btn4 = Button(root,text = '55',font = ('calibri',15,'normal'),command=Incorrect)
btn4.place(x=220,y=80)


q2_l = Label(root,text="2. How many planets are in the solar system?",font = ('calibri',15,'normal'))
q2_l.place(y=120)

btn_1 = Button(root,text = "7",font = ('calibri',15,'normal'),command=Incorrect)
btn_1.place(x=10,y=150)

btn_2 = Button(root,text = "10",font=('calibri',15,'normal'),command=Incorrect)
btn_2.place(x=80,y=150)

btn_3 = Button(root,text='8',font = ('calibri',15,'normal'),command=Correct)
btn_3.place(x=150,y=150)

btn_4 = Button(root,text = '6',font = ('calibri',15,'normal'),command=Incorrect)
btn_4.place(x=220,y=150)

q3_l = Label(root,text="3. How many continents are in the world",font = ('calibri',15,'normal'))
q3_l.place(y=190)

btn1_1 = Button(root,text = "7",font = ('calibri',15,'normal'),command=Correct)
btn1_1.place(x=10,y=230)

btn2_2 = Button(root,text = "8",font=('calibri',15,'normal'),command=Incorrect)
btn2_2.place(x=80,y=230)

btn3_3 = Button(root,text='5',font = ('calibri',15,'normal'),command=Incorrect)
btn3_3.place(x=150,y=230)

btn4_4 = Button(root,text = '6',font = ('calibri',15,'normal'),command=Incorrect)
btn4_4.place(x=220,y=230)


q3_l = Label(root,text="4. How many states are in the United States",font = ('calibri',15,'normal'))
q3_l.place(y=260)

bt_n_1 = Button(root,text = "45",font = ('calibri',15,'normal'),command=Incorrect)
bt_n_1.place(x=10,y=290)

bt_n_2 = Button(root,text = "49",font=('calibri',15,'normal'),command=Incorrect)
bt_n_2.place(x=80,y=290)

bt_n_3 = Button(root,text='51',font = ('calibri',15,'normal'),command=Incorrect)
bt_n_3.place(x=150,y=290)

bt_n_4 = Button(root,text = '50',font = ('calibri',15,'normal'),command=Correct)
bt_n_4.place(x=220,y=290)



root.mainloop()
