# Start window design

import tkinter as tk
from PIL import Image, ImageTk
import questions as q
import QuizWindowDesign as qwd

class firstWindow(tk.Frame):
    def __init__(self, x):
        super().__init__(x)
        self.x = x
        self.x.geometry('1920x1080')
        self.x.title('Quiz')
        #self.x.wm_attributes('-transparentcolor', "blue")
        self.widgets()

    def widgets(self):
        self.img = Image.open(q.clouds)
        self.photo = ImageTk.PhotoImage(self.img)
        self.lab = tk.Label(self.x, image = self.photo)
        self.lab.place(x = 0, y = 0)
        self.lab1 = tk.Label(self.x, text = "What's your Totem Animal Quiz :P")
        self.lab1.place(x = 280, y = 100)
        self.lab1.config(font=("Cooper Black", 44), bg="white")
        self.lab2 = tk.Label(self.x, text = "Click on 'START' to begin!")
        self.lab2.place(x = 600, y = 500)
        self.lab2.config(font=("Courier", 16), bg="white")
        self.lab3 = tk.Button(self.x, text = 'START', command= self.display)
        self.lab3.place(x = 710, y = 570, width = 120, height = 25)
        self.lab3.config(font=("Courier", 16, "bold"))

    def display(self):
        self.x.destroy()
        z = qwd.window(tk.Tk(), id = 0, score = 0)
        z.mainloop()


y = firstWindow(tk.Tk())
y.mainloop()
