import json
import os
import random
from tkinter import messagebox
from customtkinter import CTkButton
from PIL import Image

class BoutonFaireLeTirage(CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Tirage au sort", command=self.faire_le_tirage, **kwargs)
        self.pack(padx=20, pady=20)
        self.dossier_choisis = None

    def faire_le_tirage(self):
        dossier = self.charger_le_choix_du_dossier()
        photos_selectionnees = self.tirage_au_sort_photos(dossier)
        self.afficher_photos(dossier, photos_selectionnees)

    def tirage_au_sort_photos(self, dossier, nombre_de_photos=3):
        # Liste tous les fichiers dans le dossier
        fichiers = os.listdir(dossier)
        # Filtre uniquement les fichiers qui sont des images (par exemple, jpg, png)
        photos = [fichier for fichier in fichiers if fichier.endswith(('.jpg', '.jpeg', '.png', '.heic'))]
        # Sélectionne aléatoirement le nombre de photos spécifié
        photos_tirees = random.sample(photos, nombre_de_photos)
        return photos_tirees

    def afficher_photos(self, dossier, photos):
        print(photos)
        print(dossier)
        for photo in photos:
            chemin_photo = os.path.join(dossier, photo)
            self.image = Image.open(chemin_photo)
            self.image.show()

    def charger_le_choix_du_dossier(self):
        chemin_du_fichier = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'choixDossier.json'))
        try:
            if os.path.exists(chemin_du_fichier):
                with open(chemin_du_fichier, 'r') as fichier_choix_dossier:
                    config = json.load(fichier_choix_dossier)
                    chemin_choisis = config.get('choix_dossier', '')
                    try:
                        if chemin_choisis:
                            return chemin_choisis
                        else:
                            raise ValueError("Pas de chemin, veuillez reselectionner le dossier")
                    except Exception as e:
                        messagebox.showerror("Erreur", e)
            else:
                raise ValueError("Veuillez d'abord sélectionner un dossier")
        except Exception as e:
            messagebox.showerror("Erreur", e)
            return None
