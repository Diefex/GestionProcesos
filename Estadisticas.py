import tkinter as tk
from tkinter import ttk
from typing import Text

def gen_ventana_est(estadisticas_pr, estadisticas_gen):
    ventanta_est = tk.Tk()
    ventanta_est.title('Estadisticas de la Simulacion')
    tabla = [['Proceso', 'Llegada', 'Ejecucion', 'Espera', 'Bloqueo', 'Fin', 'Retorno', 'Perdido', 'Penalidad', 'Respuesta']]
    for est in estadisticas_pr:
        tabla.append(est)
    
    frame_pr = ttk.LabelFrame(ventanta_est, text="Estadisticas por Proceso")
    for j in range(len(tabla)):
        for i in range(len(tabla[j])):
            ttk.Label(frame_pr, text=tabla[j][i], anchor='n', borderwidth=2, relief='solid', width=10).grid(row=j, column=i, sticky='we')
    frame_pr.pack()

    frame_gr = ttk.LabelFrame(ventanta_est, text="Estadisticas Generales")
    for est in estadisticas_gen:
        ttk.Label(frame_gr, text=str(est[0])+": "+str(est[1])).pack()
    frame_gr.pack()

    ventanta_est.mainloop()