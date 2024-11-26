import tkinter as tk

def afficher_bouton():
    bouton.pack()

def cacher_bouton():
    bouton.pack_forget()

fenetre = tk.Tk()
fenetre.title("L-System")

# Menu déroulant
menu_bar = tk.Menu(fenetre)
fenetre.config(menu=menu_bar)

menu_fichier = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Fichier", menu=menu_fichier)
menu_fichier.add_command(label="Ouvrir")
menu_fichier.add_command(label="Enregistrer")

menu_options = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Options", menu=menu_options)
variable = tk.StringVar()
menu_options.add_radiobutton(label="Option 1", variable=variable, value="option1")
menu_options.add_radiobutton(label="Option 2", variable=variable, value="option2")
menu_options.add_radiobutton(label="Custom", variable=variable, value="custom", command=afficher_bouton)

# Bouton (initialement caché)
bouton = tk.Button(fenetre, text="Bouton personnalisé", command=cacher_bouton)

# Vérification initiale de l'option sélectionnée
if variable.get() == "custom":
    bouton.pack()

fenetre.mainloop()
