# GUI window design for python quiz project

import tkinter as tk
import questions as q
import lastwindow as lw
from PIL import Image, ImageTk

class window(tk.Frame):
    def __init__(self, x, id, score):
        super().__init__(x)
        self.x = x
        self.id = id
        self.score = score
        self.x.geometry('1920x1080')
        self.x.title('Quiz')
        #self.x.configure(background = q.bg_colors[self.id])
        self.widgets1()

    def widgets1(self):
        self.img = Image.open("wood.jpg")
        self.photo = ImageTk.PhotoImage(self.img)
        self.lab = tk.Label(self.x, image = self.photo)
        self.lab.place(x=0,y=0)
        self.var1 = tk.StringVar(value="1")
        self.lab1 = tk.Label(self.x, text = "What's your Totem Animal???")
        self.lab1.place(x = 280, y = 30)
        self.lab1.config(font=("Courier", 44, "bold"))#background=q.bg_colors[self.id])
        self.lab2 = tk.Label(self.x, text = q.questions[self.id])
        self.lab2.place(x = 500, y = 200)
        self.lab2.config(font=("Courier", 18, "bold"))#background=q.bg_colors[self.id])
        self.lab3 = tk.Radiobutton(self.x, text = q.options[self.id][0], variable = self.var1, value = q.options[self.id][0])
        self.lab3.place(x = 550, y = 280)
        self.lab3.config(font=("Courier", 16, "bold"))#background=q.bg_colors[self.id])
        self.lab4 = tk.Radiobutton(self.x, text = q.options[self.id][1], variable = self.var1, value = q.options[self.id][1])
        self.lab4.place(x = 550, y = 360)
        self.lab4.config(font=("Courier", 16, "bold"))#background=q.bg_colors[self.id])
        self.lab5 = tk.Radiobutton(self.x, text = q.options[self.id][2], variable = self.var1, value = q.options[self.id][2])
        self.lab5.place(x = 550, y = 440)
        self.lab5.config(font=("Courier", 16, "bold"))#background=q.bg_colors[self.id])
        self.lab6 = tk.Radiobutton(self.x, text = q.options[self.id][3], variable = self.var1, value = q.options[self.id][3])
        self.lab6.place(x = 550, y = 520)
        self.lab6.config(font=("Courier", 16, "bold"))#background=q.bg_colors[self.id])
        self.lab7 = tk.Button(self.x, text = 'Next', command = self.display1)
        self.lab7.place(x = 710, y = 600, width = 120, height = 25)
        self.lab7.config(font=("Courier", 16, "bold"))
    
    
    def display1(self):
        if self.id <= 3:
            self.id = self.id + 1
            print(self.var1.get())
           
            if self.var1.get() in q.water:    
                self.score = self.score + 10
            elif self.var1.get() in q.earth:  
                self.score = self.score + 20
            elif self.var1.get() in q.woods:  
                self.score = self.score + 30
            elif self.var1.get() in q.sky:                                                                                                                
                self.score = self.score + 40 
            
            print(self.score)
            self.x.destroy()
            z = window(x = tk.Tk(), id = self.id, score = self.score)
            z.mainloop()
        else:
            print(self.var1.get())

            if self.var1.get() in q.water:   
                self.score = self.score + 10
            elif self.var1.get() in q.earth:  
                self.score = self.score + 20
            elif self.var1.get() in q.woods:  
                self.score = self.score + 30
            elif self.var1.get() in q.sky:                                                                                                                 
                self.score = self.score + 40 
            print(self.score)
            self.x.destroy()
            a = self.score
            if 50<=a<=70:
                z = lw.lastwindow(tk.Tk(), id=0)
                z.mainloop()
            elif 80<=a<=90:
                z = lw.lastwindow(tk.Tk(), id=1)
                z.mainloop()
            elif 100<=a<=110:
                z = lw.lastwindow(tk.Tk(), id=2)
                z.mainloop()
            elif 120<=a<=140:
                z = lw.lastwindow(tk.Tk(), id=3)
                z.mainloop()
            elif 150<=a<=170:
                z = lw.lastwindow(tk.Tk(), id=4)
                z.mainloop()
            elif 180<=a<=190:
                z = lw.lastwindow(tk.Tk(), id=5)
                z.mainloop()
            elif 200<=a:
                z = lw.lastwindow(tk.Tk(), id=6)
                z.mainloop()


# root = tk.Tk()
# y = window(x=root, id = 0, score = 0)
# y.mainloop()

