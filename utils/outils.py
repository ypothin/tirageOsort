
class Outils(object):

    @staticmethod
    def center_la_fenetre(self, largeur, hauteur):
        position_x = (self.winfo_screenwidth() // 2) - (largeur // 2)
        position_y = (self.winfo_screenheight() // 2) - (hauteur // 2)
        self.geometry('{}x{}+{}+{}'.format(largeur, hauteur, position_x, position_y))