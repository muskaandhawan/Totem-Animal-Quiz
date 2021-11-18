# GUI result window design.

import tkinter as tk
import questions as q
from PIL import Image, ImageTk

class lastwindow(tk.Frame):
    def __init__(self, x, id):
        super().__init__(x)
        self.x = x
        self.id = id
        self.x.geometry('1920x1080')
        self.x.title('Quiz')
        self.x.configure(background='light yellow')
        self.widgets2()

    def widgets2(self):
    
        self.img = Image.open(q.pics[self.id])
        self.photo = ImageTk.PhotoImage(self.img)
        self.lab = tk.Label(self.x, image = self.photo)
        self.lab.place(x = 0, y = 0)#, height=1000, width=1000)
        #self.lab.pack(LEFT=0, TOP=0)
        self.lab1 = tk.Label(self.x, text = 'And your Totem Animal issss..........')
        self.lab1.place(x = 480, y = 10)
        self.lab1.config(font=("Courier", 20, 'bold'))
        self.lab2 = tk.Label(self.x, text = q.names[self.id])
        self.lab2.place(x=700,y=70)
        self.lab2.config(font=("Courier", 22, 'bold'))
        self.lab3 = tk.Label(self.x, text = q.description[self.id])
        self.lab3.place(x =140, y = 700)
        self.lab3.config(font=(0))
    

# y = lastwindow(tk.Tk(), id=6)
# y.mainloop()
