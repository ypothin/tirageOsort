from customtkinter import CTk
from customtkinter import CTkLabel
from widgets import BoutonSelectionnerDossier
from widgets import BoutonFaireLeTirage
from utils import Outils

class FenetrePrincipale(CTk):
    def __init__(self, titre, texte):
        super().__init__()
        self.title(titre)
        self.geometry(Outils.center_la_fenetre(self, 400, 400))
        self.label = CTkLabel(self, text=texte, font=("Helvetica", 14))
        self.label.pack(pady=20)

        # ajout d'un bouton selectionner dossier
        self.bouton_selectionner_dossier = BoutonSelectionnerDossier(self)
        self.bouton_faire_le_tirage = BoutonFaireLeTirage(self)
        # self.mainloop()
        