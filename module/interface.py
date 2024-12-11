from tkinter import Tk, Button, Canvas, Menu, Label, Entry, Spinbox
from fractale import *
from export import *
from preset import *

class Fenetre(Tk):
    def __init__(self):
        super().__init__()

        # Variables pour stocker les paramètres actuels
        self.graine = ""
        self.regle = []
        self.iterations = 0
        self.longueur = 0
        self.angle = 0

        # Barre de menu
        menu_bar = Menu(self)
        Fenetre.config(self, menu=menu_bar)
        
        # Menu Fichier
        menu_fichier = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fichier", menu=menu_fichier)
        menu_fichier.add_command(label="Charger", command=lambda: charger(self.canvas))
        menu_fichier.add_command(label="Exporter", command=lambda: sauvegarder(self.graine, self.regle, self.iterations, self.longueur, self.angle))
        
        # Menu Fractale
        menu_fractale = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Fractale", menu=menu_fractale)
        menu_fractale.add_command(label="Arbre", command=lambda: (arbre(self.canvas), self.cacher_parametres()))
        menu_fractale.add_command(label="Fougère", command=lambda: (fougere(self.canvas), self.cacher_parametres()))
        menu_fractale.add_command(label="Flocon de Koch", command=lambda: (flocon(self.canvas), self.cacher_parametres()))
        menu_fractale.add_command(label="Hilbert", command=lambda: (hilbert(self.canvas), self.cacher_parametres()))
        menu_fractale.add_command(label="Personnalisé", command=self.afficher_parametres)

        # Canvas pour afficher les fractales
        self.canvas = Canvas(self, width=800, height=600, bg="black")
        self.canvas.grid(column=2, row=0, rowspan=14)

        # Champs de saisie pour les paramètres de L-System
        self.chaine_depart_label = Label(self, text="Graine")
        self.chaine_depart_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.chaine_depart_entry = Entry(self)
        self.chaine_depart_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        self.regle_label = Label(self, text="Règle")
        self.regle_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.regle_entry = Entry(self)
        self.regle_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        self.iterations_label = Label(self, text="Itérations")
        self.iterations_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.iterations_spinbox = Spinbox(self, from_=1, to=10, width=5)
        self.iterations_spinbox.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        self.longueur_label = Label(self, text="Longueur")
        self.longueur_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.longueur_spinbox = Spinbox(self, from_=1, to=50, width=5)
        self.longueur_spinbox.grid(row=6, column=1, sticky="w", padx=5, pady=5)

        self.angle_label = Label(self, text="Angle")
        self.angle_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.angle_spinbox = Spinbox(self, from_=1, to=180, width=5)
        self.angle_spinbox.grid(row=7, column=1, sticky="w", padx=5, pady=5)

        # Bouton pour appliquer les paramètres du L-System
        self.bouton_appliquer = Button(self, text="Appliquer", command=self.appliquer_parametres_lsystem)
        self.bouton_appliquer.grid(row=8, column=0, columnspan=2, pady=5)

        # Masquer les champs de saisie au départ
        self.cacher_parametres()

        self.title("L-System")

    def afficher_parametres(self):
        """ Affiche les champs de saisie pour les paramètres du L-System """
        print("Affichage du menu personnalisé")
        self.chaine_depart_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.chaine_depart_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        self.regle_label.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.regle_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        self.iterations_label.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.iterations_spinbox.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        self.longueur_label.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        self.longueur_spinbox.grid(row=6, column=1, sticky="w", padx=5, pady=5)
        self.angle_label.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        self.angle_spinbox.grid(row=7, column=1, sticky="w", padx=5, pady=5)
        self.bouton_appliquer.grid(row=8, column=0, columnspan=2, pady=5)

    def cacher_parametres(self):
        """ Cache les champs de saisie pour les paramètres du L-System """
        self.chaine_depart_label.grid_forget()
        self.chaine_depart_entry.grid_forget()
        self.regle_label.grid_forget()
        self.regle_entry.grid_forget()
        self.iterations_label.grid_forget()
        self.iterations_spinbox.grid_forget()
        self.longueur_label.grid_forget()
        self.longueur_spinbox.grid_forget()
        self.angle_label.grid_forget()
        self.angle_spinbox.grid_forget()
        self.bouton_appliquer.grid_forget()

    def appliquer_parametres_lsystem(self):
        """ Applique les paramètres à la fonction du L-System """
        print("Appliquer la règle personnalisée")
        self.graine = self.chaine_depart_entry.get()  # Enregistrer la graine
        self.regle = self.regle_entry.get().split(",")  # Enregistrer la règle comme une liste
        self.iterations = int(self.iterations_spinbox.get())  # Enregistrer les itérations
        self.longueur = int(self.longueur_spinbox.get())  # Enregistrer la longueur
        self.angle = int(self.angle_spinbox.get())  # Enregistrer l'angle

        # Effacer l'ancien dessin
        self.canvas.delete("all")
        
        # Appeler la fonction dessiner_lsystem avec les paramètres définis par l'utilisateur
        dessiner_lsystem(self.canvas, self.graine, self.regle, self.iterations, self.longueur, self.angle)


