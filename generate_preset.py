from module.export import exporter

def exporter_arbre():
    """
    Exporte les règles pour l'arbre fractal dans un fichier .frtl.
    """
    regle = ["F", "FF+[+F-F-F]-[-F+F+F]"]
    # Appel de la fonction exporter avec le dossier './preset'
    exporter("F", regle, 4, 20, -122.5, "arbre.frtl", "./preset")

def exporter_fougere():
    """
    Exporte les règles pour la fougère fractale dans un fichier .frtl.
    """
    regle = ["X", "F+[[X]-X]-F[-FX]+X", "F", "FF"]
    # Appel de la fonction exporter avec le dossier './preset'
    exporter("X", regle, 5, 5, 25, "fougere.frtl", "./preset")

def exporter_flocon():
    """
    Exporte les règles pour le flocon de Koch dans un fichier .frtl.
    """
    regle = ["F", "F+F--F+F"]
    # Appel de la fonction exporter avec le dossier './preset'
    exporter("F", regle, 4, 5, 60, "flocon.frtl", "./preset")

def exporter_hilbert():
    """
    Exporte les règles pour la courbe de Hilbert dans un fichier .frtl.
    """
    regle = ["X", "+YF", "Y", "-X+Y", "F", "F"]
    # Appel de la fonction exporter avec le dossier './preset'
    exporter("X", regle, 10, 20, 12, "hilbert.frtl", "./preset")

# Exemple d'utilisation
exporter_arbre()
exporter_fougere()
exporter_flocon()
exporter_hilbert()
