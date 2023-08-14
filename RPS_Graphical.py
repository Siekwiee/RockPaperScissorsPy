import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

posibilities = ['rock', 'paper', 'scissors']

def CPU_Choice():
    global Cpu_Choice
    Cpu_Choice = random.choice(posibilities)

def Rock_Button():
    global Choice 
    Choice = 'rock'
    Player_Choice()

def Paper_Button():
    global Choice 
    Choice = 'paper'
    Player_Choice()

def Scissors_Button():
    global Choice 
    Choice = 'scissors'
    Player_Choice()

def Player_Choice():
    global Player_Choose
    Player_Choose = Choice
    print(Player_Choose)
    print(Cpu_Choice)
    if Player_Choose not in posibilities:
        print(Player_Choose)
        messagebox.showwarning("Warning", "Answer invalid!!!")
    Game_Result()

def Restart_Game():
    CPU_Choice()

def Game_Result():
    if Player_Choose == Cpu_Choice:
        messagebox.showinfo("Result", f'The Computer also picked {Cpu_Choice}, so its a draw!')
    if Player_Choose == 'paper' and Cpu_Choice == 'rock':
        messagebox.showinfo("Result", f'The Computer picked {Cpu_Choice}, so you win!')
    if Player_Choose == 'rock' and Cpu_Choice == 'scissors':
        messagebox.showinfo("Result", f'The Computer picked {Cpu_Choice}, so you win!')
    if Player_Choose == 'scissors' and Cpu_Choice == 'paper':
        messagebox.showinfo("Result", f'The Computer picked {Cpu_Choice}, so you win!')
    if Player_Choose == 'rock' and Cpu_Choice == 'paper':
        messagebox.showinfo("Result", f'The Computer picked {Cpu_Choice}, so you loose!')
    if Player_Choose == 'scissors' and Cpu_Choice == 'rock':
        messagebox.showinfo("Result", f'The Computer picked {Cpu_Choice}, so you loose!')
    if Player_Choose == 'paper' and Cpu_Choice == 'scissors':
        messagebox.showinfo("Result", f'The Computer picked {Cpu_Choice}, so you loose!')
    
    Restart_Game()

canvas = tk.Tk()
canvas.title("Rock, Paper, Scissors")
canvas.geometry("800x1000")

CPU_Choice()

Rock_Button = tk.Button(canvas, text='Rock',command=Rock_Button)
Rock_Button.place(relx=0.45, rely=0.5, anchor=E)
Paper_Button = tk.Button(canvas, text='Paper',command=Paper_Button)
Paper_Button.place(relx=0.55 , rely=0.5, anchor=W)
Scissors_Button = tk.Button(canvas, text='Scissors',command=Scissors_Button)
Scissors_Button.place(relx=0.5, rely=0.5, anchor=CENTER)



canvas.mainloop()
