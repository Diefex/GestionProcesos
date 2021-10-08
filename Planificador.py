class Planificador:
    def __init__(self):
        pass

    def planificar(self, procesos):
        # algoritmo de planificacion correspondiente
        return procesos

class FCFS(Planificador):
    def __init__(self):
        super().__init__()
    
    def get_llegada(self, pr):
        return pr.t_llegada

    def planificar(self, procesos):
        if(len([p for p in procesos if p.estado=="Ejecutando"])==0):
            procesos.sort(key=self.get_llegada)
            for i in range(len(procesos)):
                if procesos[i].estado == "Espera":
                    procesos[i].ejecutar()
                    break

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