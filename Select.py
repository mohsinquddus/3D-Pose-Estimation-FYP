#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:58:24 2021

@author: ayyaz
"""
from tkinter import *
from tkinter import ttk
from menu import menu
from poseMatching import poseMatching


def select():
    system = Tk()
    system.title("Menu")
    system.geometry("370x370")
    
    def angleDetect():
        system.destroy()
        menu()
    
    def poseMatch():
        poseMatching()
    
    Button(system, text = "Angle Detection" ,borderwidth=2,command =angleDetect).grid(row=0,column=1,padx=30,pady=150)
    
    Button(system, text = "Pose Matching" ,borderwidth=2,command =poseMatch).grid(row=0,column=2,padx=10,pady=50)
    # Quit Button

    Quit = Button(system, text = "Quit", width="10", command = system.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.675)

    def backk():
        system.destroy()
        from Code import create
        create()

    Back = Button(system, text = "Back", width="10", command = backk, bd = '3',  font = ('Times', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Back.place(anchor ='se',rely=1,relx=0.675)

    footer=Label(system, bg="white",text="GuidePose",fg="black",font="Leelawadee 14")
    footer.place(height=36,width=350,x=50, y=657)
    
    system.mainloop()

#select()




























































