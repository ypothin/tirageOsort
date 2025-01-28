import time
from visuel import FenetrePrincipale
from visuel import EcranDeDemarrage

if __name__ == "__main__":
    app = FenetrePrincipale("Ma fenêtre", "400x400", "Hello, world!")
    splash = EcranDeDemarrage(app, "Splash", "Bienvenue!", 2000)

    app.withdraw()

    splash.update()
    time.sleep(5)
    app.deiconify()
    app.mainloop()
