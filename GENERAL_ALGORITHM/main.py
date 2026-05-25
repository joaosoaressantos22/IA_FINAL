from ga import Ga
from de import De
from pso import Pso
import numpy as np
LOW = 0
HIGH = 5
import numpy as np

def fitness(x, low=0.0, high=5.0):
    """
    Função fitness baseada na Sphere Function (Minimização).
    """
    # 1. Custo Principal (O que queremos otimizar)
    custo = np.sum(x**2)
    
    # 2. Penalidade Suave (Soft Penalty) para os limites
    penalidade = 0.0
    fator_penalidade = 1000.0 
    
    # Verifica quem estourou o limite inferior
    abaixo = x[x < low]
    if len(abaixo) > 0:
        # Penaliza proporcionalmente à distância que passou do limite
        penalidade += np.sum((low - abaixo)**2) * fator_penalidade
        
    # Verifica quem estourou o limite superior
    acima = x[x > high]
    if len(acima) > 0:
        penalidade += np.sum((acima - high)**2) * fator_penalidade
        
    return custo + penalidade

# float_ga = Ga(fitness, LOW, HIGH, 1000, 30)
# float_ga.plot()

# val = De(fitness, LOW, HIGH, 1000, 30)
# val.plot()

ps_val = Pso(fitness, LOW, HIGH, 1000, 30)
ps_val.plot()