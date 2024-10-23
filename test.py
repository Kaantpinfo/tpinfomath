# -*- coding: utf-8 -*-
import turtle
import colorsys

def get_color(progress, depth):
    #Changement de couleur selon la progression et la profondeur
    hue = (progress + depth * 0.1) % 1.0
    return colorsys.hsv_to_rgb(hue, 0.8, 0.9)

def interpreter(commandes, longueur=10, angle=25):
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    stack = []  # Pour sauvegarder les positions
    
    # Position initiale
    t.penup()
    t.goto(0, -200)  # Commence en bas pour les arbres
    t.left(90)  # Pointe vers le haut
    t.pendown()
    
    total_steps = len(commandes)
    depth = 0
    
    for i, cmd in enumerate(commandes):
        progress = i / total_steps
        color = get_color(progress, depth)
        t.pencolor(color)
        
        if cmd == 'F':  # Avancer en dessinant
            t.forward(longueur)
        elif cmd == '+':  # Tourner à droite
            t.right(angle)
        elif cmd == '-':  # Tourner à gauche
            t.left(angle)
        elif cmd == '[':  # Sauvegarder la position
            stack.append((t.position(), t.heading(), depth))
            depth += 1
        elif cmd == ']':  # Restaurer la position
            position, heading, depth = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

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
    screen = turtle.Screen()
    screen.title("L-System Fractal")
    screen.bgcolor("black")
    screen.setup(800, 800)  # Taille de fenêtre fixe
    
    resultat = lsystem(chaine_depart, regle, iterations)
    interpreter(resultat, longueur, angle)
    turtle.done()

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