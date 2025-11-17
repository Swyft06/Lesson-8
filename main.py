from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.geometry("400x300")
root.title("Guess the number game")
number = random.randint(1,20)

def Greet():
    name = name_e.get()
    tkinter.messagebox.showinfo("Label",'Well,'+name+',I am thinking of a number between 1 and 20.')

def Guess():
    guess = guess_e.get()
    guess = int(guess)
    if guess == number:
        tkinter.messagebox.showinfo("Correct",'Good Job!')
    elif guess < number:
        tkinter.messagebox.showinfo("Low",'Your guess is too low')
    else:
        tkinter.messagebox.showinfo("High",'Your guess is too high')

title_l = Label(root,text="Welcome to our game!",font=('calibri',15,'normal'))
title_l.pack()

name_l = Label(root,text="What is your name?",font=('calibri',15,'normal'))
name_l.place(y=80)

name_e = Entry(root,width = 30)
name_e.place(y=110)

guess_l = Label(root,text='Take a guess:',font = ('calibri',15,'normal'))
guess_l.place(y=180)

guess_e = Entry(root,width = 15)
guess_e.place(x=120,y=190)

ok_btn = Button(root,text='OK',font = ('calibri',15,'normal'),command = Greet)
ok_btn.place(x=200,y=100)

g_btn = Button(root,text='Guess',font=('calibri',15,'normal'),command = Guess)
g_btn.place(x=200,y=180)


root.mainloop()
