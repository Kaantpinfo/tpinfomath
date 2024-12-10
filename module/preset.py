from fractale import *
from export import *

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
