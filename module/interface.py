from tkinter import Tk, Button, Canvas, Menu, Label, Entry, Spinbox, Frame, ttk, Scale
from fractale import *
import tkinter as tk
from math import cos, sin, radians

class Fenetre(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("✧ Générateur de Fractales ✧")
        self.configure(bg='#2C3E50')  # Bleu foncé professionnel
        self.geometry("1200x800")
        
        # Variables pour le zoom et la rotation
        self.zoom_factor = 1.0
        self.rotation_angle = 0
        self.last_x = 0
        self.last_y = 0
        self.dragging = False
        
        # Style moderne
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Custom.TFrame', background='#34495E')
        
        # Frame principal
        main_frame = ttk.Frame(self, style='Custom.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Frame de contrôle
        controls_frame = ttk.Frame(main_frame, style='Custom.TFrame')
        controls_frame.pack(side='left', fill='y', padx=5)
        
        # Titre
        Label(controls_frame,
              text="Paramètres L-System",
              font=('Helvetica', 12, 'bold'),
              bg='#34495E',
              fg='#ECF0F1',
              pady=10).pack(fill='x')

        # Paramètres avec style moderne
        params = [
            ("Graine", Entry),
            ("Règle", Entry),
            ("Itérations", lambda parent: Spinbox(parent, from_=1, to=10)),
            ("Longueur", lambda parent: Spinbox(parent, from_=1, to=50)),
            ("Angle", lambda parent: Spinbox(parent, from_=0, to=360))
        ]

        entry_style = {
            'font': ('Helvetica', 10),
            'bg': '#ECF0F1',
            'fg': '#2C3E50',
            'relief': 'flat',
            'width': 20
        }

        for label_text, widget_class in params:
            container = ttk.Frame(controls_frame, style='Custom.TFrame')
            container.pack(fill='x', padx=5, pady=2)
            
            Label(container,
                  text=label_text,
                  font=('Helvetica', 10),
                  bg='#34495E',
                  fg='#ECF0F1').pack(anchor='w')
            
            widget = widget_class(container) if callable(widget_class) else widget_class(container)
            widget.configure(**entry_style)
            widget.pack(fill='x', pady=2)
            
            setattr(self, f"_{label_text.lower()}", widget)

        # Contrôles de zoom et rotation
        zoom_frame = ttk.Frame(controls_frame, style='Custom.TFrame')
        zoom_frame.pack(fill='x', pady=10)
        
        Label(zoom_frame,
              text="Zoom",
              bg='#34495E',
              fg='#ECF0F1').pack()
        
        self.zoom_scale = Scale(zoom_frame,
                              from_=0.1, to=3.0,
                              resolution=0.1,
                              orient='horizontal',
                              command=self.update_view,
                              bg='#34495E',
                              fg='#ECF0F1',
                              troughcolor='#ECF0F1',
                              length=200)
        self.zoom_scale.set(1.0)
        self.zoom_scale.pack()

        # Bouton Générer avec style moderne
        Button(controls_frame,
               text="Générer la Fractale",
               font=('Helvetica', 11, 'bold'),
               bg='#3498DB',
               fg='white',
               activebackground='#2980B9',
               activeforeground='white',
               relief='flat',
               command=self.appliquer_parametres_lsystem).pack(pady=10, padx=5, fill='x')

        # Canvas amélioré
        self.canvas = Canvas(main_frame,
                           bg='#2C3E50',
                           width=800,
                           height=600,
                           highlightthickness=1,
                           highlightbackground='#3498DB')
        self.canvas.pack(side='right', fill='both', expand=True, padx=5)
        
        # Événements souris pour le drag & drop
        self.canvas.bind('<ButtonPress-1>', self.start_drag)
        self.canvas.bind('<B1-Motion>', self.drag)
        self.canvas.bind('<ButtonRelease-1>', self.stop_drag)
        self.canvas.bind('<MouseWheel>', self.mouse_wheel)  # Pour Windows
        self.canvas.bind('<Button-4>', self.mouse_wheel)    # Pour Linux
        self.canvas.bind('<Button-5>', self.mouse_wheel)    # Pour Linux
        
        self._create_menu()
        
    def _create_menu(self):
        menubar = Menu(self, bg='#2C3E50', fg='#ECF0F1', activebackground='#3498DB', activeforeground='white')
        self.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0, bg='#2C3E50', fg='#ECF0F1',
                        activebackground='#3498DB', activeforeground='white')
        menubar.add_cascade(label="Fichier", menu=file_menu)
        file_menu.add_command(label="Nouveau")
        file_menu.add_command(label="Ouvrir")
        file_menu.add_command(label="Enregistrer")
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.quit)

        fractals_menu = Menu(menubar, tearoff=0, bg='#2C3E50', fg='#ECF0F1',
                           activebackground='#3498DB', activeforeground='white')
        menubar.add_cascade(label="Fractales", menu=fractals_menu)
        fractals_menu.add_command(label="Arbre fractal", command=lambda: self.load_preset('arbre'))
        fractals_menu.add_command(label="Fougère", command=lambda: self.load_preset('fougere'))
        fractals_menu.add_command(label="Flocon de Koch", command=lambda: self.load_preset('flocon'))
        fractals_menu.add_command(label="Courbe de Hilbert", command=lambda: self.load_preset('hilbert'))

    def start_drag(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.dragging = True

    def drag(self, event):
        if self.dragging:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            self.canvas.move('all', dx, dy)
            self.last_x = event.x
            self.last_y = event.y

    def stop_drag(self, event):
        self.dragging = False

    def mouse_wheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.zoom_scale.set(min(self.zoom_scale.get() + 0.1, 3.0))
        else:
            self.zoom_scale.set(max(self.zoom_scale.get() - 0.1, 0.1))
        self.update_view()

    def update_view(self, *args):
        self.zoom_factor = self.zoom_scale.get()
        # Redessiner la fractale avec le nouveau zoom
        self.appliquer_parametres_lsystem()

    def appliquer_parametres_lsystem(self):
        try:
            self.canvas.delete("all")
            parametres = {
                'chaine_depart': self._graine.get(),
                'regle': self._regle.get(),
                'iterations': int(self._iterations.get()),
                'longueur': int(self._longueur.get()) * self.zoom_factor,
                'angle': int(self._angle.get())
            }
            dessiner_lsystem(self.canvas, **parametres)
        except ValueError:
            print("⚠️ Erreur: Veuillez vérifier vos paramètres")

    def load_preset(self, preset_name):
        if preset_name == 'arbre':
            arbre(self.canvas)
        elif preset_name == 'fougere':
            fougere(self.canvas)
        elif preset_name == 'flocon':
            flocon(self.canvas)
        elif preset_name == 'hilbert':
            hilbert(self.canvas)

