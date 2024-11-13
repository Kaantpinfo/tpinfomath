from tkinter import Tk, Button, Canvas, Menu
from fractale import *

class Window(Tk):
    def __init__(self):
        super().__init__()

        menu_bar = Menu(self)
        Window.config(self, menu=menu_bar)
        
        menu_file = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=menu_file)
        menu_file.add_command(label="Charger")
        menu_file.add_command(label="Exporter")
        
        menu_fractal = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fractale", menu=menu_fractal)
        menu_fractal.add_command(label="Arbre", command=lambda: arbre(canvas))
        menu_fractal.add_command(label="Fougère", command=lambda: fougere(canvas))
        menu_fractal.add_command(label="Flocon de Koch", command=lambda: flocon(canvas))

        
        button1 = Button(self, text="Button 1")
        button1.grid(column=0, row =0)
        button2 = Button(self, text="Button 2")
        button2.grid(column=0, row =1)
        button3 = Button(self, text="Button 3")
        button3.grid(column=0, row =2)

        canvas = Canvas(self, width=800, height=600, bg="black")
        canvas.grid(column=1, row=0, rowspan=10)

        self.title("L-System")



window = Window()
window.mainloop()
        
