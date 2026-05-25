from ga import Ga
import numpy as np
TOTAL_TUBOS = 10

FLOW_N = 0.013
FLOW_S = 0.005
FLOW_CONVERT = 1000
CUSTO = -1
DIAMETRO = 0 
D = np.array([20, 54, 98, 120, 34, 12, 88, 122, 33, 40]) #Cumprimento das distâncias
TUBOS = {0 : (150, 65), 1 : (200, 98), 2 : (250, 150), 3 : (300, 210), 4: (400, 340)}
V = np.array([2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0]) #vazao acumulada dos tupos indo de negocio até negocio 


def flow(d): #Conta muito louca 
    d_meter = d/1000
    return ((1/FLOW_N) * ((np.pi * d_meter * d_meter)/4) * pow(d_meter/4, 2/3) * pow(FLOW_S, 1/2)) * FLOW_CONVERT 

def fitness(indi):

    custo = 0
    penalidade = 0
    vazao = 0

    for i in range(TOTAL_TUBOS):

        custo += D[i] * TUBOS[indi[i]][CUSTO] #Essa é do custo 
    
        vazao = V[i] 

        Q_MAX = flow(TUBOS[indi[i]][DIAMETRO])

        if vazao >= 0.75*Q_MAX: #NÃO RESPEITA A RESTRIÇÃO 
            penalidade = 1000000
            return custo + penalidade

    return custo + penalidade

solucao = Ga(fitness, 0, 5, 1000, 10, Int_alg=True)
print(solucao.best())
solucao.plot()