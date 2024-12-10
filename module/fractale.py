import math
import colorsys
from export import *

def get_color(progress, depth):
    # Changement de couleur selon la progression et la profondeur
    hue = (progress + depth * 0.1) % 1.0
    data = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
    # Transforme une couleur en RGB en hexadecimal
    R = data[0]
    G = data[1]
    B = data[2]
    color = f'#{int(R*255):02X}{int(G*255):02X}{int(B*255):02X}'
    return color

    
def interpreter(commandes, canvas, longueur=10, angle=25):

    x, y = 400, 100
    direction = 90
    stack = []
    total_steps = len(commandes)
    depth = 0
            
    for i, cmd in enumerate(commandes):
        progress = i / total_steps
        color = get_color(progress, depth)
                
        if cmd == 'F':
            x1, y1 = x, y
            rad_angle = math.radians(direction)
            x2 = x + longueur * math.cos(rad_angle)
            y2 = y + longueur * math.sin(rad_angle)
            canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
            x, y = x2, y2
        elif cmd == '+':
            direction = (direction + angle) % 360
        elif cmd == '-':
            direction = (direction - angle) % 360
        elif cmd == '[':
            stack.append((x, y, direction))
            depth += 1
        elif cmd == ']':
            x, y, direction = stack.pop()

def lsystem(chaine, regle, iteration):
    for _ in range(iteration):
        next_gen = ""
        for c in chaine:
            found = False
            for j in range(0, len(regle), 2):
                if c == regle[j]:
                    next_gen += regle[j + 1]
                    found = True
                    break
            if not found:
                next_gen += c
        chaine = next_gen
    return chaine

def dessiner_lsystem(canvas, chaine_depart, regle, iterations, longueur=10, angle=25):
    resultat = lsystem(chaine_depart, regle, iterations)
    interpreter(resultat, canvas, longueur, angle)

# Exemples de L-systèmes fractals
def arbre(canvas):
    # Importer les données depuis le fichier arbre.frtl
    graine, regle, iteration, longueur, angle = importer('./preset/arbre.frtl')
    canvas.delete("all")
    dessiner_lsystem(canvas, graine, regle, iteration, longueur, angle)

def fougere(canvas):
    # Importer les données depuis le fichier fougere.frtl
    graine, regle, iteration, longueur, angle = importer('./preset/fougere.frtl')
    canvas.delete("all")
    dessiner_lsystem(canvas, graine, regle, iteration, longueur, angle)

def flocon(canvas):
    # Importer les données depuis le fichier flocon.frtl
    graine, regle, iteration, longueur, angle = importer('./preset/flocon.frtl')
    canvas.delete("all")
    dessiner_lsystem(canvas, graine, regle, iteration, longueur, angle)

def hilbert(canvas):
    # Importer les données depuis le fichier hilbert.frtl
    graine, regle, iteration, longueur, angle = importer('./preset/hilbert.frtl')
    canvas.delete("all")
    dessiner_lsystem(canvas, graine, regle, iteration, longueur, angle)

