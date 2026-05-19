import heapq 
from math import inf 
from pqdict import pqdict # Make sure to run: pip install pqdict

grid = [
    ['I', 2, 1, 1, 1, 2],
    [1, '*', 2, '*', 3, 1],
    [1, 4, 15, '*', '*', 1],
    [2, '*', 15,'*', 4, 1],
    ['*', '*', 2, 2, 9, 2],
    ['*', '*', '*', '*', 'F', 1]
]

class node:
    def __init__(self, weight, pos_x, pos_y):
        self.weight = weight
        self.adjacency = []
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    # --- CRITICAL ADDITION ---
    # These two methods allow the node object to be used as a dictionary key.
    # It ensures that node(2, 1, 1) and another node(2, 1, 1) are treated as the same key.
    def __eq__(self, other):
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y

    def __hash__(self):
        return hash((self.pos_x, self.pos_y))
    # -------------------------

    def __lt__(self, other):
        return self.weight < other.weight
        
    def __le__(self,other):
        return self.weight <= other.weight
        
    # Adiciona nas listas de adjacência essa bodega já 
    def add(self, node_obj):
        heapq.heappush(self.adjacency, (node_obj.weight, node_obj))

class graph:
    def __init__(self, map_astar):
        self.map = map_astar
        self.rows = len(map_astar)    
        self.cols = len(map_astar[0]) 
        
        # Inicializa o pqdict! (Key: Node object, Value: Priority/Weight)
        self.nodes = pqdict() 
        self.nodes_visited = []
        self.goal = None 

        for i in range(self.rows):
            for j in range(self.cols):
                if type(map_astar[i][j]) == int: 
                    node_adder = node(map_astar[i][j], i, j)
                    
                    # Adiciona no pqdict com peso infinito
                    self.nodes[node_adder] = inf 
                    
                    if (i - 1) >= 0 and map_astar[i - 1][j] != '*' and map_astar[i - 1][j] != 'I': 
                        w = map_astar[i - 1][j] if map_astar[i - 1][j] != 'F' else -1 
                        node_adder.add(node(w, i - 1, j)) 
                    if (i + 1) <= (self.rows - 1) and map_astar[i + 1][j] != '*' and map_astar[i + 1][j] != 'I':
                        w = map_astar[i + 1][j] if map_astar[i + 1][j] != 'F' else -1
                        node_adder.add(node(w, i + 1, j)) 
                    if (j - 1) >= 0 and map_astar[i][j - 1] != '*' and map_astar[i][j - 1] != 'I': 
                        w = map_astar[i][j - 1] if map_astar[i][j -1] != 'F' else -1
                        node_adder.add(node(w, i, j - 1)) 
                    if (j + 1) <= (self.cols - 1) and map_astar[i][j + 1] != '*' and map_astar[i][j + 1] != 'I':
                        w = map_astar[i][j + 1] if map_astar[i][j + 1] != 'F' else 0
                        node_adder.add(node(map_astar[i][j+ 1 ], i, j + 1))

                elif map_astar[i][j] == '*':
                    continue 

                elif map_astar[i][j] == 'I':
                    node_adder = node(-1, i, j)
                    
                    # O nó inicial recebe prioridade 0 (ou o valor de start que você preferir)
                    self.nodes[node_adder] = -1 
                    
                    if (i - 1) >= 0 and map_astar[i - 1][j] != '*' and map_astar[i - 1][j] != 'I':  
                        w = map_astar[i - 1][j] if map_astar[i - 1][j] != 'F' else -1 
                        node_adder.add(node(w, i - 1, j)) 
                    if (i + 1) <= (self.rows - 1) and map_astar[i + 1][j] != '*' and map_astar[i + 1][j] != 'I':
                        w = map_astar[i + 1][j] if map_astar[i + 1][j] != 'F' else -1
                        node_adder.add(node(w, i + 1, j)) 
                    if (j - 1) >= 0 and map_astar[i][j - 1] != '*' and map_astar[i][j - 1] != 'I': 
                        w = map_astar[i][j - 1] if map_astar[i][j -1] != 'F' else -1
                        node_adder.add(node(w, i, j - 1)) 
                    if (j + 1) <= (self.cols - 1) and map_astar[i][j + 1] != '*' and map_astar[i][j + 1] != 'I':
                        w = map_astar[i][j + 1] if map_astar[i][j + 1] != 'F' else 0
                        node_adder.add(node(map_astar[i][j+ 1 ], i, j + 1))

                elif map_astar[i][j] == 'F':
                    node_adder = node(inf, i, j)
                    self.goal = node_adder
                    
                    # Adiciona o Goal no pqdict
                    self.nodes[node_adder] = inf 

    def print_graph(self):
        # Iterar sobre pqdict retorna as chaves (os objetos node)
        for n in self.nodes:
            print(f"[{n.pos_x}] [{n.pos_y}]",  end=': ')
            for weight, adj_n in n.adjacency:
                 print(f"Is in this list [{adj_n.pos_x}] [{adj_n.pos_y}] weight: {adj_n.weight}", end = ' ')
            print(" ")
    
    def astar(self):

        n = None

        while self.nodes: 

            # popitem() tira o menor elemento e retorna a (chave, valor)
            n, current_priority = self.nodes.popitem() 
            print(f"Fui para [{n.pos_x}] [{n.pos_y}]")
            self.nodes_visited.append(n)

            if n == self.goal:
                print(f"Achou o Goal! Em x:{n.pos_x}, y:{n.pos_y}")
                break

            # Checamos as listas de adjacências desse nó e mudamos o valor na heap
            for adj_weight, ad_node in n.adjacency:
                
                new_cost = current_priority + adj_weight
                
                # Se o vizinho ainda não foi visitado (está no pqdict) 
                # e o novo caminho é mais rápido que o salvo na heap
                if ad_node in self.nodes and new_cost < self.nodes[ad_node]:
                    # MAGIA DO PQDICT AQUI: Só reatribuir o valor altera a prioridade na Heap!
                    self.nodes[ad_node] = new_cost


def main():
    G = graph(grid)
    # G.print_graph()
    G.astar()

if __name__ == "__main__":
    main()