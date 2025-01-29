from customtkinter import CTkProgressBar

class BarreDeChargement(CTkProgressBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.start()
        self.pack(expand=True)

    def commencer_progression(self):
        self['value'] = 0
        self.max_value = 100
        self['maximum'] = self.max_value
        self.mise_a_jour_progression()

    def mise_a_jour_progression(self):
        current_value = self["value"]
        if current_value < self.max_value:
            self["value"] = current_value + 20
            self.after(3, self.mise_a_jour_progression)