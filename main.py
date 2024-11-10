# -*- coding: utf-8 -*-
import tkinter as tk
import math
import colorsys

def get_color(progress, depth):
    # Changement de couleur selon la progression et la profondeur
    hue = (progress + depth * 0.1) % 1.0
    return colorsys.hsv_to_rgb(hue, 0.8, 0.9)

def interpreter(commandes, longueur=10, angle=25):
    def draw_line(x1, y1, x2, y2, color):
        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

    def turn_right(angle):
        nonlocal direction
        direction = (direction + angle) % 360

    def turn_left(angle):
        nonlocal direction
        direction = (direction - angle) % 360

    def save_position():
        stack.append((x, y, direction))

    def restore_position():
        x, y, direction = stack.pop()

    # Initialize Tkinter window and canvas
    window = tk.Tk()
    window.title("L-System")

    canvas = tk.Canvas(window, width=800, height=600, bg="black")
    canvas.pack()

    # Initial position and direction
    x, y = 400, 300
    direction = 90
    stack = []

    total_steps = len(commandes)
    depth = 0

    for i, cmd in enumerate(commandes):
        #progress = i / total_steps
        #color = get_color(progress, depth)

        if cmd == 'F':
            x1, y1 = x, y
            x2, y2 = x + longueur * math.cos(math.radians(direction)), y + longueur * math.sin(math.radians(direction))
            draw_line(x1, y1, x2, y2, "#FF0000")
            x, y = x2, y2
        elif cmd == '+':
            turn_right(angle)
        elif cmd == '-':
            turn_left(angle)
        elif cmd == '[':
            save_position()
            depth += 1
        elif cmd == ']':
            restore_position()

    window.mainloop()

def lsystem(chaine, regle, iteration):
    for i in range(iteration):
        nxt = ""
        for c in chaine:
            found = False
            for j in range(0, len(regle), 2):
                if c == regle[j]:
                    rep = regle[j + 1]
                    found = True
                    break
            nxt += rep if found else c
        chaine = nxt
    return chaine

def dessiner_lsystem(chaine_depart, regle, iterations, longueur=10, angle=25):
    resultat = lsystem(chaine_depart, regle, iterations)
    interpreter(resultat, longueur, angle)

# Exemples de L-systèmes fractals
def arbre():
    # Règle pour un arbre fractal
    regle = ["F", "FF+[+F-F-F]-[-F+F+F]"]
    regle2 = ["F", "F--[+F-F-F]+X", "X", "F[--+--]F"]
    dessiner_lsystem("F", regle2, 4, longueur=20, angle=-122.5)

def fougere():
    # Règle pour une fougère
    regle = ["X", "F+[[X]-X]-F[-FX]+X", "F", "FF"]
    dessiner_lsystem("X", regle, 5, longueur=5, angle=25)

def flocon():
    # Règle pour un flocon de Koch
    regle = ["F", "F+F--F+F"]
    dessiner_lsystem("F--F--F", regle, 4, longueur=5, angle=60)


arbre() 
