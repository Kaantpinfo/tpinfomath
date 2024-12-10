import os

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
