import numpy as np

N = 30
POPULACAO_TOTAL = 1000
MIN_VAL = -32
MAX_VAL = 32


FIFTY_FIFTY = 0.50
TAXA_MUT_F = 0.6
TAXA_CROSS = 0.75

rng = np.random.default_rng()

def start(pop_size):
    
    pop = np.zeros(shape=(POPULACAO_TOTAL , N), dtype=float)

    for i in range(POPULACAO_TOTAL):
        pop[i] = rng.uniform(-32.0, +32.0, size=N)

    return pop     

def mutate(pop):

    new_pop = np.zeros(shape=(POPULACAO_TOTAL , N), dtype=float)

    for i in range(POPULACAO_TOTAL):

        first = pop[np.random.randint(POPULACAO_TOTAL)]
        second = pop[np.random.randint(POPULACAO_TOTAL)]
        third = pop[np.random.randint(POPULACAO_TOTAL)]

        new_pop[i] = first + (second - third)*TAXA_MUT_F

    return new_pop

def cross(pop_ori, pop_mut):
    
    new_pop = np.zeros(shape=(POPULACAO_TOTAL , N), dtype=float)

    for i in range(POPULACAO_TOTAL):

        #Jogamos uma moeda!

        cross_p = np.random.choice([0, 1], p=(1 - TAXA_CROSS, TAXA_CROSS))

        if not cross_p:
            new_pop[i] = pop_mut[i]
        
        for j in range(N):
            
            chance = np.random.choice([0, 1], p=(1 - FIFTY_FIFTY, FIFTY_FIFTY))

            if not chance:
                new_pop[i][j] = pop_ori[i][j]
            
            elif chance:
                new_pop[i][j] = pop_mut[i][j]


    return new_pop 
#Essa brincadeira eu nn fiz nn tmnc!
def ackley_function(x):
    """
    Calcula a função de Ackley para um vetor de entrada x.
    
    Parâmetros:
    x (list ou numpy.array): Vetor de variáveis de entrada.
    
    Retorna:
    float: O valor da função de Ackley.
    """
    # Converte a entrada para um array do numpy caso não seja
    x = np.asarray(x)
    n = len(x)
    
    # Primeiro termo: -20 * exp(-0.2 * sqrt(1/n * sum(x_i^2)))
    sum_sq = np.sum(x**2)
    term1 = -20.0 * np.exp(-0.2 * np.sqrt(sum_sq / n))
    
    # Segundo termo: - exp(1/n * sum(cos(2 * pi * x_i)))
    sum_cos = np.sum(np.cos(2 * np.pi * x))
    term2 = -np.exp(sum_cos / n)
    
    # Soma com as constantes 20 e 'e'
    result = term1 + term2 + 20.0 + np.e
    
    return result

def fitness(indi):

    penalidade = 1
    for i in range(N):
        
        if indi[i] > 32:
            penalidade += 100
        
    return ackley_function(indi) * penalidade #Função de fitness!
        
def selection(pop_ori, pop_crossed, new_pop):
    
    size = 0

    while size < POPULACAO_TOTAL:
        
        first = np.random.randint(POPULACAO_TOTAL)
        second = np.random.randint(POPULACAO_TOTAL)

        first_fitness = fitness(pop_ori[first])
        second_fitness = fitness(pop_crossed[second])
        chosen = pop_ori[first] if first_fitness <= second_fitness else pop_crossed[second]
        new_pop[size] = chosen

        size += 1     

def main():
    pop = start(POPULACAO_TOTAL)
    int_pop = mutate(pop) #No caso a gente nn precisa mais de VIJ, PODEMOS SUBSTITUIR POR UIJ
    int_pop = (cross(pop, int_pop))
    
    geracoes = 200

    new_pop = np.zeros(shape=(POPULACAO_TOTAL , N), dtype=float)

    for i in range(geracoes):
        selection(pop, int_pop, new_pop)

    array_sorted = sorted(new_pop, key=fitness)

    print(array_sorted[0])

    print(f"Esse é o valor: {fitness(array_sorted[0])}")

if __name__ == "__main__":
    main()