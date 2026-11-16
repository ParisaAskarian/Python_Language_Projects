import tkinter as tk
from tkinter import Button
from tkinter import messagebox
import random
from PIL import Image , ImageTk
import pygame
class minesweeper:
    def __init__(self,master):

        self.master = master
        master.title("minesweeper")

        image = Image.open("D:/University/Python_Study/Projects/flag.png")
        image = image.resize((50, 50))
        photo = ImageTk.PhotoImage(image,100)
        self.flag = photo

        image2 = Image.open("D:/University/Python_Study/Projects/mine.png")
        image2 = image2.resize((50, 50))
        photo2 = ImageTk.PhotoImage(image2,size=100)
        self.mine = photo2

        #creat a frame that show the reset button and number of boombs
        self.frame_show = tk.Frame(self.master)
        self.frame_show.grid(row=0,column=0,sticky="nsew")
        self.frame_show.config(bg="orchid1")
        
        #this label show the number of boombs that not find
        self.label = tk.Label(master=self.frame_show,text=18)
        self.label.grid(row=0,column=0)
        self.label.config(bg="orchid1")

        #this button is a restart button
        self.restart = tk.Button(master= self.frame_show,text='restart',command=self.reset)
        self.restart.grid(row=0,column=1)
        self.restart.config(bg="yellow")

        #creat a frame that contain buttons
        self.frame2 = tk.Frame(master=master)
        self.frame2.grid(row=1,column=0)
        self.frame2.config(bg="plum1")

        #creat a board of buttons
        #creat buttons
        self.buttons = {}
        for i in range(10):
            for j in range(10):
                button = tk.Button(master=self.frame2,height=4,width=10)
                button.grid(row=i , column=j,sticky="wens")
                self.buttons[(i,j)] = button
                button.config(bg="plum1")
                button.bind("<Button-3>",lambda event,row =i,col = j:self.click_boomb(event, row , col))        
                button.bind("<Button-1>",lambda event,row =i,col = j:self.click(event, row , col))
        
        #make boardgame        
        self.board = [[' ' for k in range(12)] for k in range(12)]        
        self.boombs()
        self.make_board()

    #this function is for right click
    def click_boomb(self,event,x,y):
        Butt = self.buttons[(x,y)]
        if Butt["image"] == '' :
            Butt["image"] = self.flag
            self.label['text'] -= 1
        else:
            Butt["image"] = ''    
            self.label['text'] += 1

    #put boombs on board
    def boombs(self):
        list_boombs=[]
        but = 0
        while but != 18:
            x_boomb = random.randint(1,10)
            y_boomb = random.randint(1,10)
            boomb =[x_boomb,y_boomb]
            if boomb not in list_boombs:
                list_boombs.append(boomb)
                but += 1
        for boombs in list_boombs:
            self.board[boombs[0]][boombs[1]] = 'boomb'
    
    #put numbers and empty in board game
    def make_board(self):
        for i in range(1,11):
            for j in range(1,11):
                if self.board[i][j] != 'boomb':
                #the number of boombs around the senter of squer
                    counter = 0

                    #loop on the squer
                    for k in range(i-1,i+2):
                        for r in range(j-1,j+2):
                            if self.board[k][r] == 'boomb':
                                counter +=1
                    
                    self.board[i][j] = f'{counter}'  

        self.board =[[self.board[k][p] for k in range(1,11)] for p in range(1,11)]                                                                          

    #change the button that contain a number to a label
    def change_numbers(self,ro,co):
        but = self.buttons[(ro,co)]
        but.destroy()
        label = tk.Label(master=self.frame2,text=self.board[ro][co],height=4,width=10)
        label.grid(row=ro,column=co)
        self.buttons[(ro,co)] = label

    #this function use when the player click on a mine
    def show_board(self):
        for x in range(10):
            for y in range(10):
                item = self.buttons[(x,y)]
                if isinstance(item,Button):
                    item.destroy()
                    if self.board[x][y] == 'boomb':
                    
                        label = tk.Label(master= self.frame2,image=self.mine,height=4,width=10,text=self.board[x][y],bg="red")
                        label.grid(row=x,column=y,sticky="wens")
                    elif self.board[x][y] == '0':
                        label = tk.Label(master= self.frame2,height=4,width=10,text='')
                        label.grid(row=x,column=y)   
                    else:
                        label = tk.Label(master= self.frame2,height=4,width=10,text=self.board[x][y])
                        label.grid(row=x,column=y)    

    #change the buttons to labels
    def click(self,event,x,y):
        ro = x
        co= y
        but = self.buttons[(ro,co)]
        if but["image"] == self.flag:
            return
        if  not isinstance(but,Button):
            return
         
        if self.board[ro][co]!='boomb' and self.board[ro][co]!='0':
            self.change_numbers(ro,co) 
        elif self.board[ro][co]=='0':
            but.destroy()
            label = tk.Label(master=self.frame2,text='',height=4,width=10)
            label.grid(row=ro,column=co)
            self.buttons[(ro,co)] = label
            for k in range(max(0,ro-1),min(10,ro+2)):
                for l in range(max(0,co-1),min(10,co+2)):
                    self.click(event,k,l)
        else:
            self.show_board()
            messagebox.showinfo(title="you lose!",message="you lose!game finished")
        self.win()

    #this function check that the player win or not    
    def win(self):
        for x in range(10):
            for y in range(10):
                item = self.buttons[(x,y)]
                if isinstance(item, Button) and self.board[x][y] != 'boomb':
                    return

        messagebox.showinfo(title='we have winner!',message='you win!')        

    #this function restart the game
    def reset(self):
        
        self.__init__(master=self.master)

    # this Function is for load and display images
    #def load_image(self,choice):
        #image = Image.open(choice)
        #image = image.resize((100, 100))
        #photo = ImageTk.PhotoImage(image,size=10)
        #return photo               
                




root = tk.Tk()

window = minesweeper(master=root)
root.mainloop()
       