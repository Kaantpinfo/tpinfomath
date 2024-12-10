import os
import tkinter as tk
from tkinter import filedialog
from fractale import dessiner_lsystem

def exporter(graine, regle, iteration, longueur, angle, nom_fichier, dossier):
    try:
        # Créer le dossier s'il n'existe pas
        os.makedirs(dossier, exist_ok=True)

        # Créer le chemin complet pour le fichier dans le dossier donné
        chemin_fichier = os.path.join(dossier, nom_fichier)

        # Écrire les données dans le fichier
        with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
            fichier.write(f"graine: {graine}\n")
            fichier.write(f"regle: {regle}\n")
            fichier.write(f"iteration: {iteration}\n")
            fichier.write(f"longueur: {longueur}\n")
            fichier.write(f"angle: {angle}\n")
        
        print(f"Les données ont été exportées dans '{chemin_fichier}' avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def importer(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()
            
            # Extraction des données ligne par ligne
            graine = lignes[0].split(":")[1].strip()  # La graine est une chaîne (par ex. "F")
            regle = eval(lignes[1].split(":")[1].strip())  # La règle est une liste d'expressions
            iteration = int(lignes[2].split(":")[1].strip())  # Le nombre d'itérations est un entier
            longueur = float(lignes[3].split(":")[1].strip())  # La longueur est un nombre flottant
            angle = float(lignes[4].split(":")[1].strip())  # L'angle est un nombre flottant

        return graine, regle, iteration, longueur, angle
    
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'importation : {e}")
        return None

def charger(canvas):
    # Créer une fenêtre tkinter (sans l'afficher)
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale tkinter

    # Ouvrir une boîte de dialogue pour choisir le fichier à importer
    fichier_selectionne = filedialog.askopenfilename(
        title="Sélectionnez un fichier .frtl",
        filetypes=[("Fichiers Fractales", "*.frtl"), ("Tous les fichiers", "*.*")]
    )

    if fichier_selectionne:  # Si l'utilisateur a sélectionné un fichier
        # Utiliser la fonction importer pour traiter le fichier sélectionné
        result = importer(fichier_selectionne)

        if result:
            graine, regle, iteration, longueur, angle = result
            print(f"Fichier importé avec succès !\nGraine: {graine}\nRègle: {regle}\nItérations: {iteration}\nLongueur: {longueur}\nAngle: {angle}")

            dessiner_lsystem(canvas, graine, regle, iteration, longueur, angle)
        else:
            print("Erreur dans l'importation du fichier.")
    else:
        print("Aucun fichier sélectionné.")
