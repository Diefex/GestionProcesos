from Proceso import ProcesoRR


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
    RR = procesos[0]

    for p in procesos:
        if p not in RR.cola and p.estado=="Espera":
            RR.cola.append(p)

    ej = [p for p in procesos if p.estado=="Ejecutando"]
    if RR.t_ejecucion<1 and len(ej)>0:
        for p in ej:
            p.esperar()

    if RR.estado == "Desp" and len(RR.cola)>0:
        pr = RR.cola.pop(0)
        pr.ejecutar()
        RR.terminar()
    
    ej = [p for p in procesos if p.estado=="Ejecutando"]
    if len(ej)<1:
        RR.ejecutar()

    return procesos

def Derecho_Preferente(procesos):
    return procesos