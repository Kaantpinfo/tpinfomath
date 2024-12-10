from interface import *
import sys


# Créer et lancer la fenêtre
fenetre = Fenetre()
fenetre.protocol("WM_DELETE_WINDOW", lambda: sys.exit())
fenetre.mainloop()
