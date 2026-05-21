import numpy as np
import matplotlib.pyplot as plt

# Índices 1 a 5: Estrelas (Astros)
# Índices 6 a 30: Jogadores regulares e reservas
POINT_GUARDS = {
    1 : (35, 95, 80, 'P'), 2 : (40, 97, 85, 'P'), 3 : (38, 92, 88, 'P'), 4 : (42, 94, 82, 'P'), 5 : (33, 90, 85, 'P'),
    6 : (25, 86, 82, 'P'), 7 : (22, 85, 82, 'P'), 8 : (20, 84, 80, 'P'), 9 : (18, 82, 78, 'P'), 10 : (16, 80, 76, 'P'),
    11 : (15, 79, 75, 'P'), 12 : (14, 78, 74, 'P'), 13 : (12, 78, 75, 'P'), 14 : (11, 76, 73, 'P'), 15 : (10, 75, 72, 'P'),
    16 : (9, 74, 70, 'P'), 17 : (8, 73, 68, 'P'), 18 : (7, 72, 65, 'P'), 19 : (6, 70, 64, 'P'), 20 : (5, 68, 62, 'P'),
    21 : (5, 66, 60, 'P'), 22 : (4, 65, 58, 'P'), 23 : (4, 64, 55, 'P'), 24 : (3, 62, 54, 'P'), 25 : (3, 60, 52, 'P'),
    26 : (2, 58, 50, 'P'), 27 : (2, 55, 48, 'P'), 28 : (1, 52, 45, 'P'), 29 : (1, 50, 42, 'P'), 30 : (1, 45, 40, 'P')
}

SHOT_GUARDS = {
    1 : (30, 92, 85, "SG"), 2 : (35, 94, 88, "SG"), 3 : (38, 96, 82, "SG"), 4 : (42, 98, 80, "SG"), 5 : (32, 90, 86, "SG"),
    6 : (26, 88, 84, "SG"), 7 : (24, 86, 82, "SG"), 8 : (22, 84, 80, "SG"), 9 : (20, 82, 78, "SG"), 10 : (18, 80, 88, "SG"),
    11 : (16, 78, 85, "SG"), 12 : (15, 77, 82, "SG"), 13 : (14, 76, 80, "SG"), 14 : (12, 75, 75, "SG"), 15 : (10, 75, 70, "SG"),
    16 : (9, 73, 68, "SG"), 17 : (8, 72, 66, "SG"), 18 : (7, 70, 65, "SG"), 19 : (6, 68, 64, "SG"), 20 : (5, 66, 62, "SG"),
    21 : (5, 65, 60, "SG"), 22 : (4, 64, 58, "SG"), 23 : (4, 62, 56, "SG"), 24 : (3, 60, 54, "SG"), 25 : (3, 58, 52, "SG"),
    26 : (2, 56, 50, "SG"), 27 : (2, 54, 48, "SG"), 28 : (1, 52, 46, "SG"), 29 : (1, 50, 44, "SG"), 30 : (1, 48, 42, "SG")
}

SMAL_FW = {
    1 : (40, 96, 90, "SF"), 2 : (45, 98, 92, "SF"), 3 : (38, 94, 88, "SF"), 4 : (35, 92, 85, "SF"), 5 : (42, 95, 94, "SF"),
    6 : (30, 88, 86, "SF"), 7 : (28, 87, 85, "SF"), 8 : (25, 86, 84, "SF"), 9 : (22, 84, 82, "SF"), 10 : (20, 82, 80, "SF"),
    11 : (18, 80, 78, "SF"), 12 : (16, 78, 76, "SF"), 13 : (15, 76, 78, "SF"), 14 : (14, 75, 75, "SF"), 15 : (12, 74, 74, "SF"),
    16 : (10, 72, 72, "SF"), 17 : (9, 70, 70, "SF"), 18 : (8, 68, 68, "SF"), 19 : (7, 66, 66, "SF"), 20 : (6, 65, 64, "SF"),
    21 : (5, 64, 62, "SF"), 22 : (5, 62, 60, "SF"), 23 : (4, 60, 58, "SF"), 24 : (4, 58, 56, "SF"), 25 : (3, 56, 54, "SF"),
    26 : (3, 54, 52, "SF"), 27 : (2, 52, 50, "SF"), 28 : (2, 50, 48, "SF"), 29 : (1, 48, 46, "SF"), 30 : (1, 45, 45, "SF")
}

POINT_FW = {
    1 : (28, 88, 92, "PF"), 2 : (35, 90, 95, "PF"), 3 : (40, 92, 96, "PF"), 4 : (42, 94, 94, "PF"), 5 : (32, 89, 90, "PF"),
    6 : (25, 86, 88, "PF"), 7 : (22, 84, 86, "PF"), 8 : (20, 83, 85, "PF"), 9 : (19, 82, 86, "PF"), 10 : (18, 80, 84, "PF"),
    11 : (16, 78, 82, "PF"), 12 : (15, 76, 80, "PF"), 13 : (14, 75, 78, "PF"), 14 : (12, 74, 76, "PF"), 15 : (11, 74, 82, "PF"),
    16 : (10, 72, 78, "PF"), 17 : (9, 70, 76, "PF"), 18 : (8, 68, 74, "PF"), 19 : (7, 66, 72, "PF"), 20 : (6, 65, 70, "PF"),
    21 : (5, 64, 68, "PF"), 22 : (5, 62, 66, "PF"), 23 : (4, 60, 64, "PF"), 24 : (4, 58, 62, "PF"), 25 : (3, 56, 60, "PF"),
    26 : (3, 54, 58, "PF"), 27 : (2, 52, 56, "PF"), 28 : (2, 50, 54, "PF"), 29 : (1, 48, 52, "PF"), 30 : (1, 46, 50, "PF")
}

CENTERS = {
    1 : (32, 90, 95, 'C'), 2 : (38, 92, 96, 'C'), 3 : (45, 95, 98, 'C'), 4 : (40, 94, 94, 'C'), 5 : (35, 88, 92, 'C'),
    6 : (28, 86, 90, 'C'), 7 : (25, 85, 88, 'C'), 8 : (22, 84, 86, 'C'), 9 : (20, 84, 88, 'C'), 10 : (18, 82, 86, 'C'),
    11 : (16, 80, 84, 'C'), 12 : (15, 78, 82, 'C'), 13 : (14, 76, 85, 'C'), 14 : (12, 75, 80, 'C'), 15 : (11, 74, 78, 'C'),
    16 : (10, 72, 76, 'C'), 17 : (9, 70, 74, 'C'), 18 : (8, 68, 72, 'C'), 19 : (7, 66, 70, 'C'), 20 : (6, 64, 68, 'C'),
    21 : (5, 62, 66, 'C'), 22 : (5, 60, 64, 'C'), 23 : (4, 58, 62, 'C'), 24 : (4, 56, 60, 'C'), 25 : (3, 54, 58, 'C'),
    26 : (3, 52, 56, 'C'), 27 : (2, 50, 54, 'C'), 28 : (2, 48, 52, 'C'), 29 : (1, 46, 50, 'C'), 30 : (1, 44, 48, 'C')
}

ARRAY_POS = [POINT_GUARDS, SHOT_GUARDS, SMAL_FW, POINT_FW, CENTERS]

ATAQUE = 1
DEFESA = 2
SALARIO = 0

POPULATION_SIZE = 1000
GERACOES = 1000
GENES = 5

TAXA_PEN = 5
TAXA_MUT = 0.10
TAXA_CROSS = 0.70


def population(N):
    
    pop = np.zeros(shape=(N, GENES), dtype=int)

    for i in range(N):
        for j in range(GENES):
            # Alterado o limite superior de 4 para 31 para incluir todos os 30 jogadores
            pop[i][j] = np.random.randint(1, 31) 
    return pop

def fitness(indi):
    soma_efetiva = 0.0
    soma_salario = 0.0
    star = False 
    penalidade = 10000 

    # idx será 0, 1, 2, 3, 4. 
    # dicionario_posicao será POINT_GUARDS, SHOT_GUARDS, etc.
    for idx, dicionario_posicao in enumerate(ARRAY_POS):
        
        id_jogador = indi[idx] # Pega o ID do jogador (1 a 30) para esta posição específica
        
        if id_jogador <= 5: 
            star = True 

        soma_efetiva += 0.6 * dicionario_posicao[id_jogador][ATAQUE] + 0.4 * dicionario_posicao[id_jogador][DEFESA]
        soma_salario += dicionario_posicao[id_jogador][SALARIO]
        
        if dicionario_posicao[id_jogador][DEFESA] < 80:
            penalidade /= TAXA_PEN

    if not star:
        penalidade /= TAXA_PEN

    if soma_efetiva <= 420:
        penalidade /= TAXA_PEN

    soma_efetiva += 10
    
    if soma_salario == 0: soma_salario = 1 
    
    return (soma_efetiva/soma_salario) * penalidade

def desempenho_salario(indi):
    soma_efetiva = 0
    soma_salario = 0
    for idx, dicionario_posicao in enumerate(ARRAY_POS):
        id_jogador = indi[idx]
        soma_efetiva += 0.6 * dicionario_posicao[id_jogador][ATAQUE] + 0.4 * dicionario_posicao[id_jogador][DEFESA]
        soma_salario += dicionario_posicao[id_jogador][SALARIO]
            
    return soma_efetiva, soma_salario
#AQUI MUTAMOS 
def mutate(indi):
        
    for i in range(GENES):
        mutate_p = np.random.choice((0, 1), p= (1 - TAXA_MUT, TAXA_MUT))
        
        if not mutate_p:
            continue
        
        indi[i] = np.random.randint(1, 31) #Novo valor de indi 

    return indi

def mutacoes(pop):
    new_pop = np.zeros(shape=(POPULATION_SIZE, GENES), dtype=int)

    for i in range(POPULATION_SIZE):
        new_pop[i] = mutate(pop[i])
    
    return new_pop


def cross(indi_1, indi_2):
    mutate_p = np.random.choice((0, 1), p= (1 - TAXA_CROSS, TAXA_CROSS))
    
    if not mutate_p:
        return indi_1, indi_2
    
    cut = np.random.randint(0, GENES) #AQUI DECIDIMOS O PONTO DE CORTE
    
    new_indi_1 = np.concatenate((indi_1[cut:], indi_2[:cut]))
    new_indi_2 = np.concatenate((indi_2[cut:], indi_1[:cut]))

    return new_indi_1, new_indi_2

def cruzamento(pop):
    i = 0
    new_pop = np.zeros(shape=(POPULATION_SIZE, GENES), dtype=int)

    while i < POPULATION_SIZE:
        
        first = np.random.randint(0, POPULATION_SIZE)
        second = np.random.randint(0, POPULATION_SIZE)

        new_pop[i], new_pop[i + 1] = cross(pop[first], pop[second])

        i += 2 
    return new_pop
    

def selection(pop):
    new_pop = np.zeros(shape=(POPULATION_SIZE, GENES), dtype=int)

    for i in range(POPULATION_SIZE):

        first = np.random.randint(0, POPULATION_SIZE)
        second = np.random.randint(0, POPULATION_SIZE)
        chosen = pop[first] if fitness(pop[first]) > fitness(pop[second]) else pop[second]
        
        new_pop[i] = chosen

    return new_pop

def main():
    
    # É fundamental aumentar a população para o algoritmo ter espaço para evoluir
    # Lembre-se de mudar a constante lá no topo: POPULATION_SIZE = 100
    
    pop = population(POPULATION_SIZE)

    # Listas para guardar a história e gerar o gráfico depois
    historico_melhor_fitness = []
    historico_media_fitness = []

    print("Iniciando a evolução...")

    for i in range(GERACOES):
        pop = selection(pop) 
        pop = cruzamento(pop)
        pop = mutacoes(pop)

        # --- NOVA PARTE: COLETANDO DADOS PARA O GRÁFICO ---
        # Avalia todos os indivíduos desta geração específica
        notas_geracao = [fitness(individuo) for individuo in pop]
        
        melhor_nota = max(notas_geracao)
        media_nota = sum(notas_geracao) / POPULATION_SIZE
        
        historico_melhor_fitness.append(melhor_nota)
        historico_media_fitness.append(media_nota)
        
        # Opcional: imprimir o progresso a cada 10 gerações
        if i % 10 == 0 or i == GERACOES - 1:
            print(f"Geração {i}: Melhor = {melhor_nota:.2f} | Média = {media_nota:.2f}")

    # Encontrar o vencedor absoluto no final
    melhor = pop[0]
    for individuo in pop:
        if fitness(melhor) < fitness(individuo):
            melhor = individuo

    print("\n--- RESULTADO FINAL ---")
    print(f"IDs do Melhor Time: {melhor}")
    print(f"Desempenho Total: {desempenho_salario(melhor)[0]:.1f} pontos")
    print(f"Custo (Salário): $ {desempenho_salario(melhor)[1]} Milhões")
    print(f"Fitness (Custo-Benefício): {fitness(melhor):.2f}")

    # --- DESENHANDO O GRÁFICO COM MATPLOTLIB ---
    plt.figure(figsize=(10, 6))
    
    # Linha do melhor indivíduo de cada geração
    plt.plot(historico_melhor_fitness, label='Melhor Indivíduo', color='blue', linewidth=2)
    
    # Linha da média da população
    plt.plot(historico_media_fitness, label='Média da População', color='orange', linestyle='--')
    
    plt.title('Evolução do Algoritmo Genético - Otimização de Elenco da NBA', fontsize=14)
    plt.xlabel('Gerações', fontsize=12)
    plt.ylabel('Nota de Fitness (Desempenho / Salário)', fontsize=12)
    
    plt.legend(loc='lower right')
    plt.grid(True, linestyle=':', alpha=0.7)
    
    # Trava a execução do terminal e mostra a janela do gráfico
    plt.show()


if __name__ == "__main__":
    main()