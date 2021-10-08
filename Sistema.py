import tkinter as tk
from tkinter import ttk

from Display import Display

class Sistema:
    def __init__(self):
        self.procesos = []
        self.display = None
        self.planificador = None

        self.init_ventana_principal()
    
    def ciclo(self):
        # atender procesos
        # planificar
        # pintar procesos
        self.display.pintar_procesos(self.procesos)
        
        self.ventana_principal.after(1000, self.ciclo)

    def init_ventana_principal(self):
        self.ventana_principal = tk.Tk()
        # panel de agregar procesos
        panel_agregar = ttk.LabelFrame(self.ventana_principal, text="Agregar Proceso")
        panel_agregar.grid(row=0, column=0, sticky="w")
        ttk.Label(panel_agregar, text="Agregacion de procesos").pack()
        # panel de lista de procesos
        panel_procesos = ttk.LabelFrame(self.ventana_principal, text="Procesos")
        panel_procesos.grid(row=0, column=1, sticky="e")
        ttk.Label(panel_procesos, text="Lista de Procesos").pack()

        # panel del display
        panel_simulacion = ttk.LabelFrame(self.ventana_principal, text="Simulacion")
        self.display = Display(panel_simulacion)
        panel_simulacion.grid(row=1, column=0, columnspan=2)

        self.ciclo()
        self.ventana_principal.mainloop()

sistema = Sistema()