import numpy as np
from utils import first_half, second_half

FLOW_N = 0.013
FLOW_S = 0.005
FLOW_CONVERT = 1000
TOTAL_TUBOS = 10
QUANTIDADE_DE_TUBOS = 4
STOP_PARAMETER = 1
CROSS_OVER_RATE = 0.7
CUSTO = -1
DIAMETRO = 0 

MUTATION_RATE = 0.1
POPULACAO_TOTAL = 100

D = np.array([20, 54, 98, 120, 34, 12, 88, 122, 33, 40]) #Cumprimento das distâncias
TUBOS = {0 : (150, 65), 1 : (200, 98), 2 : (250, 150), 3 : (300, 210), 4: (400, 340)}
V = np.array([2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0]) #vazao acumulada dos tupos indo de negocio até negocio 

def initial(N): #Agora verificar o fitness
    pop = np.zeros(shape=(N, TOTAL_TUBOS), dtype=int)

    for i in range(N):
        for j in range(TOTAL_TUBOS): #Definimos um valor aleatorio dentro do range para os tubos e adicionamos no np.array posicao i, j
             pop[i][j] = np.random.randint(QUANTIDADE_DE_TUBOS + 1)    

    return pop     

def flow(d): #Conta muito louca 
    d_meter = d/1000
    return ((1/FLOW_N) * ((np.pi * d_meter * d_meter)/4) * pow(d_meter/4, 2/3) * pow(FLOW_S, 1/2)) * FLOW_CONVERT 

#No caso queremos o menor fitness
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

def cross(pop):
    rng = np.random.default_rng()
    
    new_pop = np.zeros(shape=(POPULACAO_TOTAL, TOTAL_TUBOS), dtype=int)

    for i in range(0, POPULACAO_TOTAL, 2): 

        first_idx = np.random.randint(POPULACAO_TOTAL)
        second_idx = np.random.randint(POPULACAO_TOTAL)
        
        pai1 = pop[first_idx]
        pai2 = pop[second_idx]

        cross_p = np.random.choice([0, 1], p=(1 - CROSS_OVER_RATE, CROSS_OVER_RATE))

        if not cross_p:
            new_pop[i] = pai1.copy()
            new_pop[i + 1] = pai2.copy()
            continue
        #Cross_over de corte no caso
        # new_pop[i] = np.concatenate([first_half(pai1), second_half(pai2)])
        # new_pop[i + 1] = np.concatenate([first_half(pai2), second_half(pai1)])
        beta = rng.normal(loc=0.0, scale=1.0)

        p1_float = (beta * pai1) + ((1 - beta) * pai2)
        p2_float = ((1 - beta) * pai1) + (beta * pai2)

        p1_round = np.round(p1_float)
        p2_round = np.round(p2_float)

        # Limita entre 0 e QUANTIDADE_DE_TUBOS (que é 4)
        new_pop[i] = np.clip(p1_round, 0, QUANTIDADE_DE_TUBOS).astype(int)
        new_pop[i + 1] = np.clip(p2_round, 0, QUANTIDADE_DE_TUBOS).astype(int)

    return new_pop

def mutate(pop):
    rng = np.random.default_rng()

    new_pop = np.zeros(shape=(POPULACAO_TOTAL, TOTAL_TUBOS), dtype=int)

    for i in range(POPULACAO_TOTAL):
        
        mutate_p = np.random.choice([0, 1], p=(1 - MUTATION_RATE, MUTATION_RATE))

        if not mutate_p:
            new_pop[i] = pop[i]
            continue
        
        alpha = rng.normal(loc=0.0, scale=1.0)
        p1_float = (alpha + pop[i])

        p1_round = np.round(p1_float)

        new_pop[i] = np.clip(p1_round, 0, QUANTIDADE_DE_TUBOS).astype(int)
    
    return new_pop

def selection(pop):

    new_pop = np.zeros(shape=(POPULACAO_TOTAL, TOTAL_TUBOS), dtype=int)
    size = 0
    
    while size < POPULACAO_TOTAL:
        
        first = np.random.randint(POPULACAO_TOTAL)
        second = np.random.randint(POPULACAO_TOTAL)

        first_fitness = fitness(pop[first])
        second_fitness = fitness(pop[second])

        chosen = pop[first] if first_fitness <= second_fitness else pop[second]
        new_pop[size] = chosen

        size += 1 
    
    return new_pop

def main():

    populacao = initial(POPULACAO_TOTAL) #DEFININDO A POPULAÇÃO INICIAL
    penalty = 0

    for j in range(500): #SELECÇÃO ESTÁ FEITA!
        penalty = 0
        for i in range(POPULACAO_TOTAL):
            if fitness(populacao[i]) < 1000000:
                penalty += 1
        # print(f"Tiveram {penalty} não penalidades na iteração {j}")
        
        populacao = selection(populacao)
        populacao = cross(populacao)
        populacao = mutate(populacao)
    
    #Pegamos o menor valor dessas gerações!
    menor = populacao[0]
    for j in range(POPULACAO_TOTAL):
        if fitness(menor) > fitness(populacao[i]):
            menor = populacao[i]

    print(f"CUSTO TOTAL = R${fitness(menor)}\nsequência: {menor}")        

if __name__ == "__main__":
    main()