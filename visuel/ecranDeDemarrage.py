
import os
import tkinter as tk
from PIL import Image, ImageTk
from widgets import BarreDeChargement

class EcranDeDemarrage(tk.Tk):
    def __init__(self, titre, texte):
        super().__init__()
        # self.fond_ecran_de_demarrage()
        self.title(titre)
        self.config(background="#FF6600")
        self.center_la_fenetre(400, 400)
        self.label = tk.Label(self, text=texte, font=("Helvetica", 18), bg="#FF6600", fg="white")
        self.label.pack(expand=True)
        #self.barre_de_chargement = BarreDeChargement(self)
        #self.after(delai, self.destroy)
        self.overrideredirect(True)
        self.resizable(False, False)
        #self.cacher_la_fenetre(delai)
        print("ecran de démarrage affichée")
        # self.mainloop()

    def cacher_la_fenetre(self):
        self.withdraw()
        print("ecran de démarrage cachée")
        self.destruire_la_fenetre()

    def destruire_la_fenetre(self):
        self.destroy()
        print("ecran de démarrage détruite")

    def center_la_fenetre(self, largeur, hauteur):
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # position_x = (screen_width // 2) - (largeur // 2)
        # position_y = (screen_height // 2) - (hauteur // 2)
        # return f"{largeur}x{hauteur}+{position_x}+{position_y}"
        position_x = (self.winfo_screenwidth() // 2) - (largeur // 2)
        position_y = (self.winfo_screenheight() // 2) - (hauteur // 2)
        self.geometry('{}x{}+{}+{}'.format(largeur, hauteur, position_x, position_y))
    
    def fond_ecran_de_demarrage(self):
        # Chemin de l'image
        chemin_image = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'ressources', 'splash_screen.jpg'))
        # Ouverture de l'image
        image = Image.open(chemin_image)
        self.fond_ecran = ImageTk.PhotoImage(image)

        largeur_image, hauteur_image = image.width, image.height
        # Création du canvas
        canvas = tk.Canvas(self, width=largeur_image, height=hauteur_image, bd=0, highlightthickness=0)
        canvas.pack()
        canvas.create_image(0,0, image=self.fond_ecran, anchor=tk.NW)
        canvas.create_image(0,0, image=self.fond_ecran, anchor=tk.NW)
        
        # Centrage de la fenêtre
        largeur_ecran, hauteur_ecran = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (largeur_ecran // 2) - (largeur_image // 2)
        y = (hauteur_ecran / 2) - (hauteur_image // 2)
        self.geometry(f"{largeur_image}x{hauteur_image}+{int(x)}+{int(y)}")
        
        
        




