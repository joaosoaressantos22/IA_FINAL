from a_star import A_star

mapa_exemplo_1 = [
    ['I', '2', '1', '1', '1', 'F'],
    ['1', '*', '2', '*', '3', '1'],
    ['1', '4', '15', '*', '*', '1'],
    ['2', '*', '15', '*', '4', '1'],
    ['*', '*', '2', '2', '9', '2'],
    ['*', '*', '*', '*', '*', '1']
]

path = A_star(mapa_exemplo_1)

print("Caminho:", path.caminho)
print("Custo:", path.custo)