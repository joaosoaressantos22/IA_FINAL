import numpy as np

MUT_FACTOR = 0.4
LIMITE_INF = -32
LIMITE_SUP = +32
GERACOES = 300
GENES = 30
POP_SIZE = 1000

def start(pop_size=POP_SIZE):
    return np.random.uniform(low=LIMITE_INF, high=LIMITE_SUP, size=(pop_size, GENES))

def fitness(indi):
    indi = np.asarray(indi)
    n = len(indi)
    sum_sq = np.sum(indi**2)
    term1 = -20.0 * np.exp(-0.2 * np.sqrt(sum_sq / n))
    sum_cos = np.sum(np.cos(2 * np.pi * indi))
    term2 = -np.exp(sum_cos / n)
    result = term1 + term2 + 20.0 + np.e    

    return result
    
def mutate_pop(pop):
    new_pop = np.zeros((POP_SIZE, GENES), float)
    for i in range(POP_SIZE):
        first = pop[np.random.randint(POP_SIZE)]
        second = pop[np.random.randint(POP_SIZE)]
        third = pop[np.random.randint(POP_SIZE)]

        new_pop[i] = mutate(first, second, third)

    return new_pop

def cruzamento(pop_1, pop_mut):

    new_pop = np.zeros((POP_SIZE, GENES), float) #Cruzamento 

    for i in range(POP_SIZE):
        if fitness(pop_1[i]) <  fitness(pop_mut[i]):
            new_pop[i] = pop_1[i] 
        else:
            new_pop[i] = pop_mut[i]

    return new_pop

def mutate(indi_1, indi_2, indi_3):
    return indi_1 + MUT_FACTOR * (indi_2 - indi_3)


first_pop = start()

for i in range(GERACOES):
    print(i)
    second_pop = mutate_pop(first_pop)
    first_pop = cruzamento(first_pop, second_pop)


best = first_pop[0]

for i in range(POP_SIZE):
    if fitness(first_pop[i]) < fitness(best):
        best = first_pop[i]

print(best)
print(fitness(best))
