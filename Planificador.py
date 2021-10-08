class Planificador:
    def __init__(self):
        pass

    def planificar(self, procesos):
        # algoritmo de planificacion correspondiente
        return procesos

class FCFS(Planificador):
    def __init__(self):
        super().__init__()

    def planificar(self, procesos):
        if len([p for p in procesos if p.estado=="Ejecutando"])==0:     #si no hay ningun proceso en ejecucion
            en_espera = [p.t_llegada for p in procesos if p.estado=="Espera"]       #lista de los tiempos de llegada de los procesos en espera
            i = en_espera.index(min(en_espera))     #indice del proceso en espera que llego antes
            procesos[i].ejecutar()

        return procesos

class SPN(Planificador):
    def __init__(self):
        super().__init__()

class SRTF(Planificador):
    def __init__(self):
        super().__init__()

class RR(Planificador):
    def __init__(self):
        super().__init__()

class Derecho_Preferente(Planificador):
    def __init__(self):
        super().__init__()