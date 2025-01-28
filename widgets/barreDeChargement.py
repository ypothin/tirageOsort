
from tkinter.ttk import Progressbar

class BarreDeChargement(Progressbar):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, orient='horizontal', length=300, mode='determinate', **kwargs)
        self.pack(pady=20)
        self.start()
        self.commencer_progression()

    def commencer_progression(self):
        self['value'] = 0
        self.max_value = 100
        self['maximum'] = self.max_value
        self.mise_a_jour_progression()

    def mise_a_jour_progression(self):
        current_value = self["value"]
        if current_value < self.max_value:
            print(current_value)
            self["value"] = current_value + 20
            self.after(3, self.mise_a_jour_progression)