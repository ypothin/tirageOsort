import json
import os
from tkinter import filedialog, messagebox
from customtkinter import CTkButton

class BoutonSelectionnerDossier(CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Sélectionner un dossier", command=self.selection_dossier, **kwargs)
        self.pack(padx=20, pady=10)
        self.dossier_choisis = None

    def selection_dossier(self):
        try:
            chemin_du_dossier = filedialog.askdirectory()
            if not chemin_du_dossier:
                raise ValueError("Aucun dossier sélectionné")
            self.sauvegarder_le_choix_du_dossier(chemin_du_dossier)
        except Exception as e:
            messagebox.showerror("Erreur", e)
    
    def sauvegarder_le_choix_du_dossier(self, dossier_choisis):
        chemin_du_fichier = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'choixDossier.json'))
        print(chemin_du_fichier)
        with open(chemin_du_fichier, "w") as fichier_choix_dossier:
            json.dump({"choix_dossier": dossier_choisis}, fichier_choix_dossier)