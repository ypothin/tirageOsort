from visuel import FenetrePrincipale
from visuel import EcranDeDemarrage

if __name__ == "__main__":

    # Créer une fenêtre de démarrage
    splash = EcranDeDemarrage("Splash", "Bienvenue!")
    # Cacher la fenêtre de démarrage après 2 secondes
    splash.after(6000,splash.cacher_la_fenetre)
    splash.mainloop()

    # Créer une fenêtre principale
    app = FenetrePrincipale("Ma fenêtre", "400x400", "Hello, world!")
    app.mainloop()