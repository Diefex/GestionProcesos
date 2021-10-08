from tkinter import Canvas

class Display:
    def __init__(self, master):
        self.canvas = Canvas(master, bg='black', width=700, height=200)
        self.canvas.pack()
        self.pos = 10

    def pintar_procesos(self, procesos):
        x = self.pos
        y = self.pos
        self.canvas.create_rectangle(x,y,x+10,y+10, fill="red")
        self.pos += 10