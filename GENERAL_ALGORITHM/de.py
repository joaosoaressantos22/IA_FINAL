import numpy as np
import matplotlib.pyplot as plt
#Funcionando ok!
class De:
    def __init__(self, fitness_func, inf_limit, sup_limit, pop_size, genes, MUT_FACTOR=0.4, custo=True, GERACOES = 300):
        
        self.pop = np.random.uniform(low=inf_limit, high=sup_limit, size=(pop_size, genes))
        self.fitness = fitness_func
        self.pop_size = pop_size
        self.fitness_por_geracao = np.zeros(shape=GERACOES, dtype=float)
        self.geracoes = np.linspace(start=1, stop=GERACOES, num=GERACOES, dtype=int)

        for j in range(GERACOES):
            print(j)
            new_pop = np.zeros((pop_size, genes), float)
            for i in range(pop_size):
                first = self.pop[np.random.randint(pop_size)]
                second = self.pop[np.random.randint(pop_size)]
                third = self.pop[np.random.randint(pop_size)]
                new_pop[i] = first + MUT_FACTOR * (second - third)
                if custo:
                    if fitness_func(self.pop[i]) > self.fitness(new_pop[i]):
                        self.pop[i] = new_pop[i]
                else:
                    if fitness_func(new_pop[i]) > self.fitness(self.pop[i]):
                        self.pop[i] = new_pop[i]

            fitness_arr = np.array([fitness_func(ind) for ind in self.pop])
            melhor_idx = np.argmin(fitness_arr)
            self.fitness_por_geracao[j] = fitness_arr[melhor_idx]
            
    def best(self):
        self.best = self.pop[0]

        for i in range(self.pop_size):
            if self.fitness(self.pop[i]) < self.fitness(self.best):
                self.best = self.pop[i]

        return self.best
    
    def plot(self):
        fig, ax = plt.subplots()

        ax.plot(self.geracoes, self.fitness_por_geracao)

        ax.set_xlabel("Geração")
        ax.set_ylabel("Fitness")
        ax.set_title("Algoritmo DE")
        ax.legend(["Fitness"])

        plt.show()
