import numpy as np

GERACOES = 1000
LIMITES_INF = -100
LIMITES_SUP = 100
POPULACAO = 100
DIMENSAO = 30
W = 0.4
C1 = 2.05
C2 = 2.05

def population_start(N):
    return np.random.uniform(low=LIMITES_INF, high=LIMITES_SUP, size=(POPULACAO,N))

def velocity_start(N):
    return np.random.uniform(low=-1.0, high=+1.0, size=(POPULACAO,N))

def fitness(indi):
    penalidade = 1
    if np.max(indi) > LIMITES_SUP or np.min(indi) < LIMITES_INF:
        penalidade = 1000
    return np.sum(indi**2) * penalidade   

def new_velocity(v, p_best, g_best, x):
    r1 = np.random.uniform(low=0.0, high=1.0, size=len(x))
    r2 = np.random.uniform(low=0.0, high=1.0, size=len(x))
    return (W * v) + (C1) * r1 * (p_best - x) +  (C2) * r2 * (g_best - x)

def new_position(x, v):
    return x + v

def main():
    custo = True #Altere se for para ser falso!
    #INICIALIZACAO 
    pop = population_start(DIMENSAO)
    vel = velocity_start(DIMENSAO)
    p_bests = np.array([x for x in pop])
    fitness_vals = np.array([fitness(x) for x in pop])
    g_best_idx = np.argmin(fitness_vals) #Esse é só o valor do idx do fitness!
    g_best = np.copy(p_bests[g_best_idx])
    fit_best = fitness(g_best)

    for i in range(GERACOES): #Loop principal!
        for j in range(POPULACAO): #Loop da população!
            
            fit_atual = fitness(pop[j])

            if custo:
                if fitness_vals[j] > fit_atual:
                    p_bests[j] = np.copy(pop[j]) # Salva uma cópia congelada!
                    fitness_vals[j] = fit_atual 

                if fit_best > fit_atual:
                    g_best = np.copy(pop[j]) # Salva uma cópia congelada!
                    fit_best = fit_atual
            else:
                if fitness_vals[j] < fit_atual: 
                    p_bests[j] = np.copy(pop[j]) # Salva uma cópia congelada!
                    fitness_vals[j] = fit_atual 

                if fit_best < fit_atual:
                    g_best = np.copy(pop[j]) # Salva uma cópia congelada!
                    fit_best = fit_atual

            vel[j] = new_velocity(vel[j], p_bests[j], g_best, pop[j])
            pop[j] = pop[j] + vel[j]
    
    print(fit_best)

if __name__ == "__main__":
    main()
# print(population_start(30))