from tkinter import Canvas

class Display:
    def __init__(self, master, width=700, height=200):
        self.width = width
        self.height = height
        self.canvas = Canvas(master, bg='black', width=self.width, height=self.height)
        self.canvas.pack()
        self.tam_cr = 15
        self.y_crr = 20
        self.x_crr = 35
        self.pos = self.x_crr

        self.canvas.create_line(self.x_crr, self.y_crr-1, self.width-self.tam_cr, self.y_crr-1, fill='white')   

    def pintar_procesos(self, procesos):
        self.canvas.create_rectangle(0,0, self.x_crr, self.height, fill='black')
        self.canvas.create_text(self.pos+7, self.y_crr-10, text=str(int(self.pos/self.tam_cr)), fill="white")
        for i in range(len(procesos)):
            self.canvas.create_text(self.x_crr-15, self.y_crr+8+(i*self.tam_cr), text="P"+str(i), fill="white")
            self.canvas.create_line(self.x_crr-5, self.y_crr+(i*self.tam_cr), self.x_crr-5, self.y_crr+self.tam_cr+(i*self.tam_cr), fill="white")
            self.canvas.create_line(self.x_crr-8, self.y_crr+self.tam_cr+(i*self.tam_cr), self.x_crr-1, self.y_crr+self.tam_cr+(i*self.tam_cr), fill="white")

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
            y = (i*self.tam_cr)+self.y_crr
            self.canvas.create_rectangle(x,y,x+self.tam_cr,y+self.tam_cr, fill=color)
        self.pos += self.tam_cr