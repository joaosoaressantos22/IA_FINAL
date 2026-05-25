import heapq
import math


def calcular_heuristica(atual, destino):
    return math.sqrt((atual[0] - destino[0])**2 + (atual[1] - destino[1])**2)

class A_star:
    #No caso vamos considerar o fitness como uma função que recebe dois args!
    def __init__(self, mapa, fitness=calcular_heuristica,):
        self.fit = fitness
        self.lin = len(mapa)
        self.cols = len(mapa[0])
        self.caminho = None
        self.custo = 0 
        inicio = None
        fim = None
        #Procuramos o inicio e o fim!
        for i in range(self.lin):
            for j in range(self.cols):
                if mapa[i][j] == 'I':
                    inicio = (i, j)
                elif mapa[i][j] == 'F':
                    fim = (i, j)
                    
        if inicio == None or fim == None:
            print("Error! Inicio ou fim não encontrados!")
            return
        lista_aberta = []
        contador = 0
        # Inicialmente o custo em 'I' é 0. E o caminho percorrido tbm é 'I'
        heapq.heappush(lista_aberta, (0, contador, 0, inicio, [inicio]))
        # Dicionário para encontrar o menor G de cada célula, G É CUSTO NO CASO!
        melhor_g = { inicio: 0 }
        celulas_expandidas = set()     # lista de células expandidas
        direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # Movimentos possíveis: Direita, Baixo, Esquerda, Cima
        while lista_aberta:
            f, _, g_atual, atual, caminho = heapq.heappop(lista_aberta)         #Pega a célula com menor custo F
            if atual in celulas_expandidas:
                continue
            celulas_expandidas.add(atual)
            if atual == fim: #CHEGAMOS NO FIM!
                self.caminho = caminho
                self.custo = g_atual
            for dr, dc in direcoes:         # Explora as direções distintas
                vizinho_r, vizinho_c = atual[0] + dr, atual[1] + dc
                vizinho = (vizinho_r, vizinho_c)
                if 0 <= vizinho_r < self.lin and 0 <= vizinho_c < self.cols:
                    valor_celula = mapa[vizinho_r][vizinho_c]
                #caminho bloqueado!
                if valor_celula == '*':
                    continue
                custo_passo = 0
                if valor_celula != 'F' and valor_celula != 'I':
                    custo_passo = int(valor_celula)

                # Calcula o novo custo acumulado (G)
                novo_g = g_atual + custo_passo
                if vizinho not in melhor_g or novo_g < melhor_g[vizinho]:
                    melhor_g[vizinho] = novo_g
                    h = fitness(vizinho, fim)
                    novo_f = novo_g + h
                    novo_caminho = caminho + [vizinho]
                    contador += 1
                    heapq.heappush(lista_aberta, (novo_f, contador, novo_g, vizinho, novo_caminho))