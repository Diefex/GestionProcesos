class proceso():
    def __init__(self, t_llegada, t_ejecucion, bloqueos):
        
        self.t_llegada = t_llegada
        self.bloqueos = bloqueos
        self.estado = "Listo"
        self.t_ejecucion = t_ejecucion
        self.t_bloqueo = 0

    def atender(self):
        # resta unidad de tiempo si en ejecucion o bloqueado
        pass
    
    def suspender(self):
        self.estado = "Bloqueado"
        self.t_bloqueo = self.bloqueos.pop()[1]

    def reanudar(self):
        self.estado = "Listo"
    
    def ejecutar(self):
        self.estado = "Ejecutando"

    def terminar(self):
        self.estado = "Terminado"