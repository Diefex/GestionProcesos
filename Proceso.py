class Proceso():
    def __init__(self, t_llegada, t_ejecucion, bloqueos):
        
        self.t_llegada = t_llegada
        self.bloqueos = bloqueos
        self.estado = "Espera"
        self.t_ejecucion = t_ejecucion
        self.t_restante = t_ejecucion
        self.t_bloqueo = 0

    def atender(self):
        if self.estado=="Ejecutando" and self.bloqueos[0][0] == self.t_ejecucion-self.t_restante:
            self.bloquear()
        if self.estado=="Bloqueado" and self.t_bloqueo<1:
            self.esperar()
        if self.t_restante<1:
            self.terminar()

        if self.estado=="Ejecutando" and self.t_restante>0:
            self.t_restante -= 1
        if self.estado=="Bloqueado" and self.t_bloqueo>0:
            self.t_bloqueo -= 1
    
    def bloquear(self):
        if self.estado!="Terminado":
            try:
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

    def terminar(self):
        if self.t_restante<1:
            self.estado = "Terminado"