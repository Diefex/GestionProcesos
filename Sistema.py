import tkinter as tk
from tkinter import ttk

from Display import Display

class Sistema:
    def __init__(self) -> None:
        self.procesos = []
        self.display = Display()
        self.planificador

        self.init_ventana_principal()
    
    def ciclo(self):
        # atender procesos
        # planificar
        # pintar procesos
        self.ventana_principal.after(1000, self.ciclo)

    def init_ventana_principal(self):
        self.ventana_principal = tk.Tk()
        # panel de agregar procesos
        # panel de lista de procesos
        # panel del display
        self.ciclo()
        self.ventana_principal.mainloop()