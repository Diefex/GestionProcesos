import tkinter as tk
from tkinter import ttk

def gen_ventana_est(estadisticas):
    ventanta_est = tk.Tk()
    ventanta_est.title('Estadisticas de la Simulacion')
    tabla = [['Proceso', 'Llegada', 'Ejecucion', 'Espera', 'Bloqueo', 'Fin', 'Retorno', 'Perdido', 'Penalidad', 'Respuesta']]
    for est in estadisticas:
        tabla.append(est)
    
    for j in range(len(tabla)):
        for i in range(len(tabla[j])):
            ttk.Label(ventanta_est, text=tabla[j][i], anchor='n', borderwidth=2, relief='solid', width=10).grid(row=j, column=i, sticky='we')

    ventanta_est.mainloop()