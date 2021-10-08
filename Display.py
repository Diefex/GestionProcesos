from tkinter import Canvas

class Display:
    def __init__(self, master):
        self.canvas = Canvas(master, bg='black', width=700, height=200)
        self.canvas.pack()
        self.pos = 10

    def pintar_procesos(self, procesos):
        for i in range(len(procesos)):
            status = procesos[i].estado
            if(status == "Ejecutando"):
                color = "green"
            elif(status == "Bloqueado"):
                color = "red"
            elif(status == "Espera"):
                color = "grey"
            elif(status == "Terminado"):
                color = "black"

            x = self.pos
            y = i*10
            self.canvas.create_rectangle(x,y,x+10,y+10, fill=color)
        self.pos += 10