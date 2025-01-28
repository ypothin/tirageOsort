
import os
import tkinter as tk
from PIL import Image, ImageTk

class EcranDeDemarrage(tk.Toplevel):
    def __init__(self, parent, titre, texte, delai):
        super().__init__(parent)
        self.fond_ecran_de_demarrage()
        self.title(titre)
        self.label = tk.Label(self, text=texte, font=("Helvetica", 18))
        self.label.pack(expand=True)
        self.after(delai, self.destroy)

    def center_la_fenetre(self, largeur, hauteur):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (largeur // 2)
        position_y = (screen_height // 2) - (hauteur // 2)
        return f"{largeur}x{hauteur}+{position_x}+{position_y}"
    
    def fond_ecran_de_demarrage(self):
        # Chemin de l'image
        chemin_image = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'ressources', 'splash_screen.jpg'))
        # Ouverture de l'image
        image = Image.open(chemin_image)
        self.fond_ecran = ImageTk.PhotoImage(image)

        largeur_image, hauteur_image = image.width, image.height
        # Création du canvas
        canvas = tk.Canvas(self, width=largeur_image, height=hauteur_image)
        canvas.pack()
        self.ecran_de_demarrage = canvas.create_image(0,0, image=self.fond_ecran, anchor=tk.NW)
        
        # Centrage de la fenêtre
        largeur_ecran, hauteur_ecran = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (largeur_ecran // 2) - (largeur_image // 2)
        y = (hauteur_ecran / 2) - (hauteur_image // 2)
        self.geometry(f"{largeur_image}x{hauteur_image}+{int(x)}+{int(y)}")
        
        
        




