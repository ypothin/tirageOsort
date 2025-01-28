import customtkinter as ctk
from widgets import BoutonSelectionnerDossier
from widgets import BoutonFaireLeTirage

class FenetrePrincipale(ctk.CTk):
    def __init__(self, titre, taille, texte):
        super().__init__()
        self.title(titre)
        self.geometry(taille)
        self.label = ctk.CTkLabel(self, text=texte, font=("Helvetica", 14))
        self.label.pack(pady=20)

        # ajout d'un bouton selectionner dossier
        self.bouton_selectionner_dossier = BoutonSelectionnerDossier(self)

        self.bouton_faire_le_tirage = BoutonFaireLeTirage(self)