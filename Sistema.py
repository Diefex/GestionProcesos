import tkinter as tk
from tkinter import ttk

from Display import Display
from Proceso import Proceso
from Planificador import *

class Sistema:
    def __init__(self):
        self.procesos = []
        self.lista_procesos = []

        self.quantum = 0
        self.correr_sim = False

        self.ventana_principal = tk.Tk()
        self.init_ventana_principal()
        self.ventana_principal.mainloop()
    
    def ciclo(self):
        if not self.correr_sim:
            return

        # agregar procesos
        for pr in self.lista_procesos:
            if(pr.t_llegada==self.quantum):
                self.procesos.append(pr)

        # cambiar estados
        for i in range(len(self.procesos)):
            self.procesos[i].cambiar_estado()
        # planificar
        self.procesos = SRTF(self.procesos)
        # atender procesos
        for i in range(len(self.procesos)):
            self.procesos[i].atender()
        # pintar procesos
        self.display.pintar_procesos(self.procesos)
        for i in range(len(self.procesos)):
            if self.procesos[i].estado == "Ejecutando":
                self.lista_lbl[i]['background'] = 'green'
            elif self.procesos[i].estado == "Bloqueado":
                self.lista_lbl[i]['background'] = 'red'
            elif self.procesos[i].estado == "Espera":
                self.lista_lbl[i]['background'] = 'grey'
            else:
                self.lista_lbl[i]['background'] = 'black'
        
        self.quantum += 1
        self.ventana_principal.after(1000, self.ciclo)
    
    def iniciar_sim(self):
        self.correr_sim = True
        self.ciclo()
    
    def detener_sim(self):
        self.correr_sim = False
    
    def reiniciar_sim(self):
        self.correr_sim = False
        self.procesos = []
        self.lista_procesos = []
        self.quantum = 0
        for item in self.panel_procesos.winfo_children():
            item.destroy()
        self.init_ventana_principal()

    def agregar_proceso(self):
        if(self.dr_nv_proc.get().isdigit()):
            self.nv_bloq.sort()
            self.nv_bloq.reverse()
            self.lista_procesos.append(Proceso(self.quantum, int(self.dr_nv_proc.get()), self.nv_bloq))

            self.agregar_proceso_lista()

            self.nv_bloq = []
            self.lb_nv_bloq.set('')

    def agregar_proceso_lista(self):
        i = len(self.lista_procesos)-1
        pnl = ttk.LabelFrame(self.panel_procesos, text="Proceso "+str(i))
        lb = ttk.Label(pnl, text='P'+str(i), background="black", foreground='white')
        lb.grid(row=0, column=0)
        self.lista_lbl.append(lb)
        ttk.Button(pnl, text='||', width=3, command= lambda: self.bloquear_proceso(i, 3)).grid(row=0,column=1)
        ttk.Button(pnl, text='■', width=3, command= lambda: self.terminar_proceso(i)).grid(row=0,column=2)
        pnl.grid(row=i%2, column=int(i/2))

    def agr_nv_bloq(self):
        if (self.in_nv_bloq.get().isdigit() and self.dr_nv_bloq.get().isdigit()):
            self.nv_bloq.append([int(self.in_nv_bloq.get()), int(self.dr_nv_bloq.get())])
            self.lb_nv_bloq.set(self.nv_bloq)
       
    def bloquear_proceso(self, i, t):
        if i<len(self.procesos):
            self.procesos[i].bloquear(t_bloqueo=t)

    def terminar_proceso(self, i):
        if i<len(self.procesos):
            self.procesos[i].terminar()

    def lista_predeterminada(self):
        self.lista_procesos.append(Proceso(0, 6, [[3,2]]))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(1, 8, [[1,3]]))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(2, 7, [[5,1]]))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(4, 3, [[0,0]]))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(6, 9, [[2,4]]))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(6, 2, [[0,0]]))
        self.agregar_proceso_lista()

    def init_ventana_principal(self):

        self.dr_nv_proc = tk.StringVar()
        self.in_nv_bloq = tk.StringVar()
        self.dr_nv_bloq = tk.StringVar()
        self.nv_bloq = []
        self.lb_nv_bloq = tk.StringVar()
        # panel de agregar procesos
        self.panel_agregar = ttk.LabelFrame(self.ventana_principal, text="Agregar Proceso")
        self.panel_agregar.grid(row=0, column=0, sticky="w")
        ttk.Label(self.panel_agregar, text="Duracion: ").grid(row=0, column=0)
        ttk.Entry(self.panel_agregar, textvariable=self.dr_nv_proc, width=3).grid(row=0, column=1, columnspan=2 ,sticky='we')
        ttk.Label(self.panel_agregar, text="Bloqueos: ").grid(row=1, column=0)
        ttk.Entry(self.panel_agregar, textvariable=self.in_nv_bloq, width=3).grid(row=1, column=1)
        ttk.Entry(self.panel_agregar, textvariable=self.dr_nv_bloq, width=3).grid(row=1, column=2)
        ttk.Label(self.panel_agregar, textvariable=self.lb_nv_bloq).grid(row=1, column=3)
        ttk.Button(self.panel_agregar, text="Agregar Bloqueo", command=self.agr_nv_bloq).grid(row=2, column=0)
        ttk.Label(self.panel_agregar, text="ini").grid(row=2, column=1, sticky='n')
        ttk.Label(self.panel_agregar, text="dur").grid(row=2, column=2, sticky='n')
        ttk.Button(self.panel_agregar, text="Agregar Proceso", command=self.agregar_proceso).grid(row=3, column=0, columnspan=3, sticky='we')

        # panel de control de simulacion
        self.panel_ctrl_sim = ttk.LabelFrame(self.ventana_principal, text="Control")
        self.panel_ctrl_sim.grid(row=0, column=1, sticky="w")
        ttk.Button(self.panel_ctrl_sim, text="Iniciar", command=self.iniciar_sim).grid(row=0, column=0, sticky='we')
        ttk.Button(self.panel_ctrl_sim, text="Detener", command=self.detener_sim).grid(row=1, column=0, sticky='we')
        ttk.Button(self.panel_ctrl_sim, text="Predet.", command=self.lista_predeterminada).grid(row=2, column=0, sticky='we')
        ttk.Button(self.panel_ctrl_sim, text="Reiniciar", command=self.reiniciar_sim).grid(row=3, column=0, sticky='we')

        self.lista_lbl = []
        # panel de lista de procesos
        self.panel_procesos = ttk.LabelFrame(self.ventana_principal, text="Procesos")
        self.panel_procesos.grid(row=0, column=2, sticky="e")

        # panel del display
        self.panel_simulacion = ttk.LabelFrame(self.ventana_principal, text="Simulacion")
        self.display = Display(self.panel_simulacion)
        self.panel_simulacion.grid(row=1, column=0, columnspan=3)


sistema = Sistema()