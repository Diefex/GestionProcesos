import tkinter as tk
from tkinter import ttk

from Display import Display
from Proceso import Proceso
from Planificador import FCFS

class Sistema:
    def __init__(self):
        self.procesos = []

        self.lista_procesos = []
        self.lista_procesos.append(Proceso(0, 6, [[3,2]]))
        self.lista_procesos.append(Proceso(1, 8, [[1,3]]))
        self.lista_procesos.append(Proceso(2, 7, [[5,1]]))
        self.lista_procesos.append(Proceso(4, 3, [[0,0]]))
        self.lista_procesos.append(Proceso(6, 9, [[2,4]]))
        self.lista_procesos.append(Proceso(6, 2, [[0,0]]))

        self.display = None
        self.planificador = FCFS()

        self.quantum = 0

        self.init_ventana_principal()
    
    def ciclo(self):
        # agregar procesos
        for pr in self.lista_procesos:
            if(pr.t_llegada==self.quantum):
                self.procesos.append(pr)

        # cambiar estados
        for i in range(len(self.procesos)):
            self.procesos[i].cambiar_estado()
        # planificar
        self.procesos = self.planificador.planificar(self.procesos)
        # atender procesos
        for i in range(len(self.procesos)):
            self.procesos[i].atender()
        # pintar procesos
        self.display.pintar_procesos(self.procesos)
        
        self.quantum += 1
        self.ventana_principal.after(1000, self.ciclo)

    def agregar_proceso_lista(self):
        print("agreg")

    def init_ventana_principal(self):
        self.ventana_principal = tk.Tk()
        # panel de agregar procesos
        panel_agregar = ttk.LabelFrame(self.ventana_principal, text="Agregar Proceso")
        panel_agregar.grid(row=0, column=0, sticky="w")
        ttk.Button(panel_agregar, text="Agregacion de procesos", command=self.agregar_proceso_lista).pack()
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