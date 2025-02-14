import random

# Vetor de pesos

w = [1, 1]


def ativacao(x):
    return 1 if x > 0 else -1


def perceptron(entrada):
    entrada_total = 0
    for i in range(len(entrada)):
        entrada_total += w[i] * entrada[i]

    return ativacao(entrada_total)


conjunto_de_treino = []
for _ in range(1000):
    x1 = random.uniform(-10, 10)
    x2 = random.uniform(-10, 10)
    y = 1 if x2 > 0 else -1
    conjunto_de_treino.append([x1, x2, y])

taxa = 0.1

# Fase de treino
for _ in range(100000):
    exemplo = random.choice(conjunto_de_treino)
    resultado_esperado = exemplo[2]

    resultado_obtido = perceptron(exemplo[:2])

    erro = resultado_esperado - resultado_obtido

    if erro != 0:
        for i in range(len(w)):
            w[i] += taxa * erro * exemplo[i]

        print(w)
