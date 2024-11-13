import math
import colorsys

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

    def draw_line(x1, y1, x2, y2, color):
        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)  # Use canvas for drawing

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

    # Initial position and direction (can be adjusted if needed)
    x, y = 400, 300
    direction = 90
    stack = []

    total_steps = len(commandes)
    depth = 0

    for i, cmd in enumerate(commandes):
        progress = i / total_steps
        color = get_color(progress, depth)  # Can be used for color variation

        if cmd == 'F':
            x1, y1 = x, y
            x2, y2 = x + longueur * math.cos(math.radians(direction)), y + longueur * math.sin(math.radians(direction))
            draw_line(x1, y1, x2, y2, color)  # Use canvas for drawing
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
    # Règle pour un arbre fractal
    regle = ["F", "FF+[+F-F-F]-[-F+F+F]"]
    regle2 = ["F", "F--[+F-F-F]+X", "X", "F[--+--]F"]
    canvas.delete("all")
    dessiner_lsystem(canvas, "F", regle, 4, longueur=20, angle=-122.5)

def fougere(canvas):
    # Règle pour une fougère
    regle = ["X", "F+[[X]-X]-F[-FX]+X", "F", "FF"]
    canvas.delete("all")
    dessiner_lsystem(canvas, "X", regle, 5, longueur=5, angle=25)

def flocon(canvas):
    # Règle pour un flocon de Koch
    regle = ["F", "F+F--F+F"]
    canvas.delete("all")
    dessiner_lsystem(canvas, "F--F--F", regle, 4, longueur=5, angle=60)
