
from collections import defaultdict
import os


class Outils(object):

    @staticmethod
    def center_la_fenetre(self, largeur, hauteur):
        position_x = (self.winfo_screenwidth() // 2) - (largeur // 2)
        position_y = (self.winfo_screenheight() // 2) - (hauteur // 2)
        self.geometry('{}x{}+{}+{}'.format(largeur, hauteur, position_x, position_y))

    @staticmethod
    def compter_et_classer_les_fichiers_du_dossiers(chemin_dossier):
        file_types = defaultdict(int)
        
        for root, dirs, files in os.walk(chemin_dossier):
            for file in files:
                file_extension = os.path.splitext(file)[1]
                file_types[file_extension] += 1
        
        return dict(file_types)