import customtkinter as ctk
from widgets import BoutonSelectionnerDossier
from widgets import BoutonFaireLeTirage

class FenetrePrincipale(ctk.CTk):
    def __init__(self, titre, taille, texte):
        super().__init__()
        self.title(titre)
        self.center_la_fenetre(400, 400)
        self.label = ctk.CTkLabel(self, text=texte, font=("Helvetica", 14))
        self.label.pack(pady=20)

        # ajout d'un bouton selectionner dossier
        self.bouton_selectionner_dossier = BoutonSelectionnerDossier(self)
        self.bouton_faire_le_tirage = BoutonFaireLeTirage(self)
        self.mainloop()

    def center_la_fenetre(self, largeur, hauteur):
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # position_x = (screen_width // 2) - (largeur // 2)
        # position_y = (screen_height // 2) - (hauteur // 2)
        # return f"{largeur}x{hauteur}+{position_x}+{position_y}"
        position_x = (self.winfo_screenwidth() // 2) - (largeur // 2)
        position_y = (self.winfo_screenheight() // 2) - (hauteur // 2)
        self.geometry('{}x{}+{}+{}'.format(largeur, hauteur, position_x, position_y))