import numpy as np

GERACOES = 1000
LIMITES_INF = -100
LIMITES_SUP = 100
POPULACAO = 100
DIMENSAO = 30
W = 0.4

def population_start(N):
    return np.random.uniform(low=LIMITES_INF, high=LIMITES_SUP, size=(POPULACAO,N))

def velocity_start(N):
    return np.random.uniform(low=-1, high=+1, size=(POPULACAO,N))

def fitness(indi):
    return np.sum(indi**2)

def best_global(pop):
    pass


def main():
    #INICIALIZACAO 
    pop = population_start(DIMENSAO)
    vel = velocity_start(DIMENSAO)
    indi_vals = np.array([x for x in pop])
    fitness_vals = np.array([fitness(x) for x in pop])
    g_best = np.argmin(fitness_vals)

    for i in range(GERACOES):
        pass
    #Pega o argmin dos pbestscpres  

if __name__ == "__main__":
    main()
# print(population_start(30))