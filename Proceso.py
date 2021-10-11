class Proceso():
    def __init__(self, t_llegada, t_ejecucion, bloqueos):
        
        self.bloqueos = bloqueos
        self.estado = "Espera"
        
        self.t_llegada = t_llegada
        self.t_ejecucion = t_ejecucion
        self.t_espera = 0
        self.t_bloqueado = 0
        self.t_fin = 0
        self.t_respuesta = 0
        self.t_restante = t_ejecucion
        self.t_bloqueo = 0

    def cambiar_estado(self):
        if self.estado=="Ejecutando" and len(self.bloqueos)>0 and self.bloqueos[-1][0] == self.t_ejecucion-self.t_restante:
            self.bloquear()
        if self.estado=="Bloqueado" and self.t_bloqueo<1:
            self.esperar()
        if self.t_restante<1:
            self.terminar()

    def atender(self):
        if self.estado=="Ejecutando" and self.t_restante>0:
            self.t_restante -= 1
        if self.estado=="Bloqueado" and self.t_bloqueo>0:
            self.t_bloqueo -= 1
            self.t_bloqueado += 1
        if self.estado=="Espera":
            self.t_espera += 1
    
    def bloquear(self, t_bloqueo=0):
        if self.estado=="Ejecutando":
            try:
                if t_bloqueo!=0:
                    self.t_bloqueo = t_bloqueo
                else:
                    self.t_bloqueo = self.bloqueos.pop()[1]
                self.estado = "Bloqueado"
            except:
                print("El proceso no se puede suspender")

    def esperar(self):
        if self.estado!="Terminado":
            self.estado = "Espera"

    def ejecutar(self):
        if self.estado!="Terminado":
            self.estado = "Ejecutando"
            if self.t_ejecucion==self.t_restante:
                self.t_respuesta = self.t_espera

    def terminar(self, q=-1):
        if q>=0:
            self.t_fin = q
        else:
            self.t_fin = self.t_llegada+self.t_ejecucion+self.t_espera+self.t_bloqueado
        self.estado = "Terminado"

class ProcesoRR(Proceso):
    def __init__(self):
        super().__init__(0, 0, [[0,0]])
        self.cola = []
        self.estado = "Terminado"
    
    def cambiar_estado(self):
        return

    def atender(self):
        if self.t_ejecucion<1:
            self.ejecutar()
        if self.estado=="Terminado":
            self.t_ejecucion-=1
        return
    
    def bloquear(self):
        return
    
    def esperar(self):
        return

    def ejecutar(self):
        self.estado = "Desp"
    
    def terminar(self):
        self.t_ejecucion = 3
        self.estado = "Terminado"