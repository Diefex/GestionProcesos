import tkinter as tk
from tkinter import ttk

from Display import Display
from Proceso import Proceso, ProcesoRR
from Planificador import *
from Estadisticas import gen_ventana_est

class Sistema:
    def __init__(self):
        self.procesos = []
        self.lista_procesos = []

        self.quantum = 0
        self.lim_sim = 55
        self.correr_sim = False

        self.ventana_principal = tk.Tk()
        self.init_ventana_principal()
        self.ventana_principal.mainloop()

    def listenerRR(self):
        if self.sel_plan.get()=='RR' and len([RR for RR in self.lista_procesos if isinstance(RR, ProcesoRR)])<1:
            self.lista_procesos.insert(0, ProcesoRR())
            for item in self.panel_procesos.winfo_children():
                item.destroy()
            self.lista_lbl = []
            self.agregar_proceso_lista(RR=True)
            for i in range(1,len(self.lista_procesos)):
                self.agregar_proceso_lista(i=i)
        elif self.sel_plan.get()!='RR' and len([RR for RR in self.lista_procesos if isinstance(RR, ProcesoRR)])>0:
            self.lista_procesos.pop(0)
            for item in self.panel_procesos.winfo_children():
                item.destroy()
            self.lista_lbl = []
            for i in range(len(self.lista_procesos)):
                self.agregar_proceso_lista(i=i)
        self.ventana_principal.after(10, self.listenerRR)
    
    def ciclo(self):
        if not self.correr_sim:
            return

        # agregar procesos
        for pr in self.lista_procesos:
            if(pr.t_llegada==self.quantum):
                self.procesos.append(pr)
                if len(self.procesos)>1 and isinstance(self.procesos[0], ProcesoRR):
                    self.procesos[0].cola.append(pr)

        # cambiar estados
        for i in range(len(self.procesos)):
            self.procesos[i].cambiar_estado()
        # planificar
        plan = self.sel_plan.get()
        if plan=="FCFS":
            self.procesos = FCFS(self.procesos)
        elif plan=="SJF":
            self.procesos = SJF(self.procesos)
        elif plan=="SRTF":
            self.procesos = SRTF(self.procesos)
        elif plan=="RR":
            self.procesos = RR(self.procesos)
        elif "DPCM" in plan:
            self.procesos = Derecho_Preferente(self.procesos)
        # atender procesos
        for i in range(len(self.procesos)):
            self.procesos[i].atender(Retro=True if 'Con' in plan else False)
        # pintar procesos
        self.display.pintar_procesos(self.procesos, 
        RR=(len(self.procesos)>0 and isinstance(self.procesos[0], ProcesoRR)),
        DP=True if 'DP' in self.sel_plan.get() else False)
        for i in range(len(self.procesos)):
            if self.procesos[i].estado == "Ejecutando":
                self.lista_lbl[i]['background'] = 'green'
            elif self.procesos[i].estado == "Bloqueado":
                self.lista_lbl[i]['background'] = 'red'
            elif self.procesos[i].estado == "Espera":
                self.lista_lbl[i]['background'] = 'grey'
            elif self.procesos[i].estado == 'Desp':
                self.lista_lbl[i]['background'] = 'cyan'
            else:
                self.lista_lbl[i]['background'] = 'black'
        
        self.quantum += 1
        if self.quantum>self.lim_sim:
            self.detener_sim()
        
        self.ventana_principal.after(200, self.ciclo)
    
    def iniciar_sim(self):
        self.correr_sim = True
        self.sel_plan.configure(state='disabled')
        self.ciclo()
    
    def detener_sim(self):
        self.correr_sim = False
        gen_ventana_est(self.estadisticas(RR=len(self.procesos)>1 and isinstance(self.procesos[0], ProcesoRR)))
    
    def reiniciar_sim(self):
        self.correr_sim = False
        self.procesos = []
        self.lista_procesos = []
        self.quantum = 0
        for item in self.panel_procesos.winfo_children():
            item.destroy()
        self.init_ventana_principal()

    def estadisticas(self, RR=False):
        tabla = []
        for i in range((1 if RR else 0),len(self.procesos)):
            est = [
                i,
                self.procesos[i].t_llegada,
                self.procesos[i].t_ejecucion,
                self.procesos[i].t_espera,
                self.procesos[i].t_bloqueado
            ]
            if self.procesos[i].estado=='Terminado':
                est.extend([
                    self.procesos[i].t_fin,
                    self.procesos[i].t_fin-self.procesos[i].t_llegada,
                    (self.procesos[i].t_fin-self.procesos[i].t_llegada)-self.procesos[i].t_ejecucion,
                    round((self.procesos[i].t_fin-self.procesos[i].t_llegada)/self.procesos[i].t_ejecucion, 2)
                ])
            else:
                est.extend(['-','-','-','-'])
            est.append(self.procesos[i].t_respuesta)
            tabla.append(est)
        return tabla

    def agregar_proceso(self):
        if(self.dr_nv_proc.get().isdigit()):
            self.nv_bloq.sort()
            self.nv_bloq.reverse()
            self.lista_procesos.append(Proceso(self.quantum, int(self.dr_nv_proc.get()), self.nv_bloq, prioridad=int(self.sel_prio.get())))

            self.agregar_proceso_lista()

            self.nv_bloq = []
            self.lb_nv_bloq.set('')

    def agregar_proceso_lista(self, i=-1, RR=False):
        i = len(self.lista_procesos)-1 if i==-1 else i
        pnl = ttk.LabelFrame(self.panel_procesos, text=("Proceso "+str(i) if not RR else "RR"))
        lb = ttk.Label(pnl, text=('P'+str(i) if not RR else "RR"), background="black", foreground='white')
        lb.grid(row=0, column=0)
        self.lista_lbl.insert(i, lb)
        ttk.Button(pnl, text='||', width=3, command= lambda: self.bloquear_proceso(i, 3)).grid(row=0,column=1)
        ttk.Button(pnl, text='■', width=3, command= lambda: self.terminar_proceso(i)).grid(row=0,column=2)
        pnl.grid(row=i%2 if not RR else 0, column=int(i/2) if not RR else 0)

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
        self.lista_procesos.append(Proceso(0, 6, [[3,2]], prioridad=1))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(1, 8, [[1,3]], prioridad=2))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(2, 7, [[5,1]], prioridad=3))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(4, 3, [[0,0]], prioridad=1))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(6, 9, [[2,4]], prioridad=2))
        self.agregar_proceso_lista()
        self.lista_procesos.append(Proceso(6, 2, [[0,0]], prioridad=3))
        self.agregar_proceso_lista()

    def init_ventana_principal(self):
        self.ventana_principal.title('Simulacion Gestion de Procesos')

        self.dr_nv_proc = tk.StringVar()
        self.in_nv_bloq = tk.StringVar()
        self.dr_nv_bloq = tk.StringVar()
        self.pr_nv_proc = tk.StringVar()
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
        ttk.Label(self.panel_agregar, textvariable=self.lb_nv_bloq).grid(row=2, column=0)
        ttk.Button(self.panel_agregar, text="+", command=self.agr_nv_bloq, width=2).grid(row=1, column=3)
        ttk.Label(self.panel_agregar, text="ini").grid(row=2, column=1, sticky='n')
        ttk.Label(self.panel_agregar, text="dur").grid(row=2, column=2, sticky='n')
        ttk.Label(self.panel_agregar, text="Prioridad: ").grid(row=3, column=0)
        self.sel_prio = ttk.Combobox(self.panel_agregar, state="readonly", values=["0", "1", "2"], width=2)
        self.sel_prio.grid(row=3, column=1, columnspan=2 ,sticky='we')
        self.sel_prio.set(self.sel_prio['values'][0])
        ttk.Button(self.panel_agregar, text="Agregar Proceso", command=self.agregar_proceso).grid(row=4, column=0, columnspan=4, sticky='we')

        # panel de control de simulacion
        self.panel_ctrl_sim = ttk.LabelFrame(self.ventana_principal, text="Control")
        self.panel_ctrl_sim.grid(row=0, column=1, sticky="w")
        ttk.Button(self.panel_ctrl_sim, text="Iniciar", command=self.iniciar_sim).grid(row=0, column=0, sticky='we')
        ttk.Button(self.panel_ctrl_sim, text="Detener", command=self.detener_sim).grid(row=1, column=0, sticky='we')
        ttk.Button(self.panel_ctrl_sim, text="Predet.", command=self.lista_predeterminada).grid(row=2, column=0, sticky='we')
        ttk.Button(self.panel_ctrl_sim, text="Reiniciar", command=self.reiniciar_sim).grid(row=3, column=0, sticky='we')
        self.sel_plan = ttk.Combobox(self.panel_ctrl_sim, state="readonly", values=["FCFS", "SJF", "SRTF", "RR", "DPCM Sin Retro.", "DPCM Con Retro."])
        self.sel_plan.grid(row=4, column=0, sticky='we')
        self.sel_plan.set(self.sel_plan['values'][0])

        self.lista_lbl = []
        # panel de lista de procesos
        self.panel_procesos = ttk.LabelFrame(self.ventana_principal, text="Procesos")
        self.panel_procesos.grid(row=0, column=2, sticky="e")

        # panel del display
        self.panel_simulacion = ttk.LabelFrame(self.ventana_principal, text="Simulacion")
        self.display = Display(self.panel_simulacion, width=self.lim_sim)
        self.panel_simulacion.grid(row=1, column=0, columnspan=3)

        #Listener
        self.listenerRR()


sistema = Sistema()