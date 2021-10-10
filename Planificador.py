def get_llegada(pr):
    return pr.t_llegada

def FCFS(procesos):
    if(len([p for p in procesos if p.estado=="Ejecutando"])==0): # si no hay ningun proceso en ejecucion
        pr = procesos.copy()
        pr.sort(key=get_llegada)
        for i in range(len(pr)):
            if pr[i].estado == "Espera":
                pr[i].ejecutar()
                break

    return procesos


def get_t_ejecucion(pr):
    return pr.t_ejecucion

def SJF(procesos):
    if(len([p for p in procesos if p.estado=="Ejecutando"])==0): # si no hay ningun proceso en ejecucion
        pr = procesos.copy()
        pr.sort(key=get_t_ejecucion)
        for i in range(len(pr)):
            if pr[i].estado == "Espera":
                pr[i].ejecutar()
                break

    return procesos


def get_t_restante(pr):
    return pr.t_restante

def SRTF(procesos):
    if(len([p for p in procesos if p.estado=="Ejecutando"])==0): # si no hay ningun proceso en ejecucion
        pr = procesos.copy()
        pr.sort(key=get_t_restante)
        for i in range(len(pr)):
            if pr[i].estado == "Espera":
                pr[i].ejecutar()
                break

    return procesos

def RR(procesos):
    return procesos

def Derecho_Preferente(procesos):
    return procesos