import tkinter as tk
from tkinter import ttk, colorchooser
import math
import colorsys

class LSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("L-System Designer")

        # Frame principale divisée en deux parties
        self.main_frame = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame gauche (paramètres)
        self.params_frame = ttk.Frame(self.main_frame)
        
        # Frame droite (canvas)
        self.canvas_frame = ttk.Frame(self.main_frame)
        
        self.main_frame.add(self.params_frame)
        self.main_frame.add(self.canvas_frame)

        # Canvas pour le dessin
        self.canvas = tk.Canvas(self.canvas_frame, width=800, height=600, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Variables pour les couleurs personnalisées
        self.start_color = "#FF0000"  # Rouge par défaut
        self.end_color = "#00FF00"    # Vert par défaut
        self.use_custom_colors = tk.BooleanVar(value=False)
        
        # Variables pour les règles personnalisées
        self.custom_axiom = tk.StringVar(value="F")
        self.custom_rules = {}
        
        # Création des widgets de paramètres
        self.create_parameters()

        # Variables pour les règles L-System
        self.current_system = "arbre"  # système par défaut

    def create_parameters(self):
        notebook = ttk.Notebook(self.params_frame)
        notebook.pack(fill="both", expand=True)

        # Onglet des paramètres standard
        standard_frame = ttk.Frame(notebook)
        notebook.add(standard_frame, text="Standard")
        self.create_standard_parameters(standard_frame)

        # Onglet des paramètres personnalisés
        custom_frame = ttk.Frame(notebook)
        notebook.add(custom_frame, text="Personnalisé")
        self.create_custom_parameters(custom_frame)

    def create_standard_parameters(self, parent):
        # Titre
        title_label = ttk.Label(parent, text="Paramètres L-System", font=('Arial', 12, 'bold'))
        title_label.pack(pady=10)

        # Sélection du type de L-System
        system_frame = ttk.LabelFrame(parent, text="Type de L-System")
        system_frame.pack(padx=5, pady=5, fill="x")
        
        self.system_var = tk.StringVar(value="arbre")
        systems = [("Arbre", "arbre"), 
                  ("Fougère", "fougere"), 
                  ("Flocon de Koch", "flocon"),
                  ("Personnalisé", "custom")]
        
        for text, value in systems:
            ttk.Radiobutton(system_frame, text=text, value=value, 
                           variable=self.system_var,
                           command=self.update_drawing).pack(anchor="w", padx=5)

        # Paramètres de base
        self.create_base_parameters(parent)

    def create_custom_parameters(self, parent):
        # Frame pour les règles personnalisées
        rules_frame = ttk.LabelFrame(parent, text="Règles personnalisées")
        rules_frame.pack(padx=5, pady=5, fill="x")

        # Axiome
        ttk.Label(rules_frame, text="Axiome:").pack(anchor="w", padx=5)
        axiom_entry = ttk.Entry(rules_frame, textvariable=self.custom_axiom)
        axiom_entry.pack(padx=5, fill="x")

        # Frame pour les règles
        self.rules_container = ttk.Frame(rules_frame)
        self.rules_container.pack(padx=5, pady=5, fill="x")
        
        # Bouton pour ajouter une règle
        ttk.Button(rules_frame, text="Ajouter une règle", 
                   command=self.add_rule_fields).pack(pady=5)

        # Frame pour les couleurs personnalisées
        colors_frame = ttk.LabelFrame(parent, text="Couleurs personnalisées")
        colors_frame.pack(padx=5, pady=5, fill="x")

        # Checkbox pour activer les couleurs personnalisées
        ttk.Checkbutton(colors_frame, text="Utiliser des couleurs personnalisées", 
                        variable=self.use_custom_colors,
                        command=self.update_drawing).pack(anchor="w", padx=5)

        # Boutons de sélection des couleurs
        ttk.Button(colors_frame, text="Couleur de début", 
                   command=lambda: self.choose_color('start')).pack(pady=5)
        ttk.Button(colors_frame, text="Couleur de fin", 
                   command=lambda: self.choose_color('end')).pack(pady=5)

        # Bouton pour appliquer les règles personnalisées
        ttk.Button(parent, text="Appliquer", 
                   command=self.apply_custom_rules).pack(pady=20)

    def create_base_parameters(self, parent):
        # Paramètres de dessin
        params_frame = ttk.LabelFrame(parent, text="Paramètres")
        params_frame.pack(padx=5, pady=5, fill="x")

        # Longueur
        ttk.Label(params_frame, text="Longueur:").pack(anchor="w", padx=5)
        self.length_var = tk.DoubleVar(value=10)
        self.length_scale = ttk.Scale(params_frame, from_=1, to=50, 
                                    variable=self.length_var,
                                    command=lambda _: self.update_drawing())
        self.length_scale.pack(padx=5, fill="x")

        # Angle
        ttk.Label(params_frame, text="Angle:").pack(anchor="w", padx=5)
        self.angle_var = tk.DoubleVar(value=25)
        self.angle_scale = ttk.Scale(params_frame, from_=0, to=180, 
                                   variable=self.angle_var,
                                   command=lambda _: self.update_drawing())
        self.angle_scale.pack(padx=5, fill="x")

        # Itérations
        ttk.Label(params_frame, text="Itérations:").pack(anchor="w", padx=5)
        self.iterations_var = tk.IntVar(value=4)
        iterations = ttk.Spinbox(params_frame, from_=1, to=6, 
                               textvariable=self.iterations_var,
                               command=self.update_drawing,
                               width=5)
        iterations.pack(anchor="w", padx=5)

        # Couleur de fond
        color_frame = ttk.LabelFrame(parent, text="Couleur de fond")
        color_frame.pack(padx=5, pady=5, fill="x")
        
        self.bg_color_var = tk.StringVar(value="black")
        colors = [("Noir", "black"), 
                 ("Blanc", "white"), 
                 ("Gris", "gray")]
        
        for text, value in colors:
            ttk.Radiobutton(color_frame, text=text, value=value, 
                           variable=self.bg_color_var,
                           command=self.update_background).pack(anchor="w", padx=5)

    def add_rule_fields(self):
        rule_frame = ttk.Frame(self.rules_container)
        rule_frame.pack(fill="x", pady=2)
        
        # Champ pour le caractère
        char_var = tk.StringVar()
        ttk.Label(rule_frame, text="Si:").pack(side="left", padx=2)
        char_entry = ttk.Entry(rule_frame, textvariable=char_var, width=3)
        char_entry.pack(side="left", padx=2)
        
        # Champ pour la règle
        rule_var = tk.StringVar()
        ttk.Label(rule_frame, text="Alors:").pack(side="left", padx=2)
        rule_entry = ttk.Entry(rule_frame, textvariable=rule_var)
        rule_entry.pack(side="left", padx=2, fill="x", expand=True)
        
        # Bouton de suppression
        ttk.Button(rule_frame, text="X", 
                   command=lambda: rule_frame.destroy()).pack(side="right")
        
        self.custom_rules[char_var] = rule_var

    def choose_color(self, which):
        color = colorchooser.askcolor(
            title="Choisir une couleur",
            color=self.start_color if which == 'start' else self.end_color
        )
        if color[1]:  # si une couleur a été choisie
            if which == 'start':
                self.start_color = color[1]
            else:
                self.end_color = color[1]
            self.update_drawing()

    def get_custom_color(self, progress, depth):
        if self.use_custom_colors.get():
            # Conversion des couleurs hex en RGB
            def hex_to_rgb(hex_color):
                hex_color = hex_color.lstrip('#')
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            start_rgb = hex_to_rgb(self.start_color)
            end_rgb = hex_to_rgb(self.end_color)
            
            # Interpolation linéaire entre les deux couleurs
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * progress)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * progress)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * progress)
            
            return f'#{r:02x}{g:02x}{b:02x}'
        else:
            return self.get_color(progress, depth)

    def get_color(self, progress, depth):
        hue = (progress + depth * 0.1) % 1.0
        data = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
        R, G, B = data
        return f'#{int(R*255):02x}{int(G*255):02x}{int(B*255):02x}'

    def interpreter(self, commands, length=10, angle=25):
        x, y = 400, 300
        direction = 90
        stack = []
        total_steps = len(commands)
        depth = 0
        
        for i, cmd in enumerate(commands):
            progress = i / total_steps
            color = self.get_custom_color(progress, depth)
            
            if cmd == 'F':
                x1, y1 = x, y
                rad_angle = math.radians(direction)
                x2 = x + length * math.cos(rad_angle)
                y2 = y + length * math.sin(rad_angle)
                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
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

    def lsystem(self, axiom, rules, iterations):
        for _ in range(iterations):
            next_gen = ""
            for c in axiom:
                found = False
                for j in range(0, len(rules), 2):
                    if c == rules[j]:
                        next_gen += rules[j + 1]
                        found = True
                        break
                if not found:
                    next_gen += c
            axiom = next_gen
        return axiom

    def update_background(self):
        self.canvas.configure(bg=self.bg_color_var.get())
        self.update_drawing()

    def get_custom_rules(self):
        rules = []
        for char_var, rule_var in self.custom_rules.items():
            if char_var.get() and rule_var.get():
                rules.extend([char_var.get(), rule_var.get()])
        return rules

    def apply_custom_rules(self):
        self.system_var.set("custom")
        self.update_drawing()

    def update_drawing(self):
        self.canvas.delete("all")
        system = self.system_var.get()
        length = self.length_var.get()
        angle = self.angle_var.get()
        iterations = self.iterations_var.get()

        if system == "arbre":
            rules = ["F", "FF+[+F-F-F]-[-F+F+F]"]
            self.dessiner_lsystem("F", rules, iterations, length, angle)
        elif system == "fougere":
            rules = ["X", "F+[[X]-X]-F[-FX]+X", "F", "FF"]
            self.dessiner_lsystem("X", rules, iterations, length, angle)
        elif system == "flocon":
            rules = ["F", "F+F--F+F"]
            self.dessiner_lsystem("F--F--F", rules, iterations, length, angle)
        elif system == "custom":
            rules = self.get_custom_rules()
            self.dessiner_lsystem(self.custom_axiom.get(), rules, iterations, length, angle)

    def dessiner_lsystem(self, axiom, rules, iterations, length, angle):
        resultat = self.lsystem(axiom, rules, iterations)
        self.interpreter(resultat, length, angle)

if __name__ == "__main__":
    root = tk.Tk()
    app = LSystemApp(root)
    root.mainloop()