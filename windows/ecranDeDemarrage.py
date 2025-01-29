
import os
from customtkinter import CTk
from customtkinter import CTkLabel
from customtkinter import CTkProgressBar
from PIL import Image, ImageTk
from utils import Outils
from widgets.barreDeChargement import BarreDeChargement


class EcranDeDemarrage(CTk):

    def __init__(self, titre, texte):
        super().__init__()
        # self.fond_ecran_de_demarrage()
        self.title(titre)
        self.config(background="#FF6600")
        self.chemin_ressources = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'ressources'))
        self.geometry(Outils.center_la_fenetre(self,400, 400))
        self.label = CTkLabel(self, text=texte, font=("Helvetica", 18), fg_color='#FF6600', text_color='white')
        self.label.pack(expand=True)
        # label_image = Image.open(os.path.join(self.chemin_ressources, 'Hourglass.gif'))
        # self.image_loader = ImageTk.PhotoImage(label_image)
        # self.label_2 = tk.Label(self, image=self.image_loader, width=256, height=256, bg="#FF6600", fg="white")
        # self.label_2.pack(expand=True)
        # self.barre_de_chargement = CTkProgressBar(self, width=300, height=15, mode='indeterminate', border_color='#FF6600')
        self.barre_de_chargement = BarreDeChargement(self)

        self.overrideredirect(True)
        self.resizable(False, False)
        print("ecran de démarrage affichée")

    def cacher_la_fenetre(self):
        self.withdraw()
        self.barre_de_chargement.stop()
        print("ecran de démarrage cachée")
        self.destruire_la_fenetre()

    def destruire_la_fenetre(self):
        self.destroy()
        print("ecran de démarrage détruite")

    
    
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
        
        # Centrage de la fenêtre
        largeur_ecran, hauteur_ecran = self.winfo_screenwidth(), self.winfo_screenheight()
        x = (largeur_ecran // 2) - (largeur_image // 2)
        y = (hauteur_ecran / 2) - (hauteur_image // 2)
        self.geometry(f"{largeur_image}x{hauteur_image}+{int(x)}+{int(y)}")
        
        
        




