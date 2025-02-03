import math
import random


def f(x):
    """Função objetivo."""
    return (1 / (x * x + 1)) * math.cos(10 * x)


class Estado:
    def __init__(self, x):
        self.x = x
        self.f = f(x)


def exibe(estado):
    print(f"x = {estado.x}, f = {estado.f}")


def estado_inicial():
    return Estado(random.uniform(-10, 10))


def escolhe(populacao):
    ind1 = random.choice(populacao)
    ind2 = random.choice(populacao)

    if ind1.f > ind2.f:
        return ind1
    return ind2


def cruzamento(pai1, pai2):
    return Estado(random.uniform(pai1.x, pai2.x))


def mutacao(individuo):
    return Estado(individuo.x + random.uniform(-0.1, 0.1))


tam_populacao = 100
n_geracoes = 100
taxa_de_mutacao = 0.1
tam_elite = 3

populacao = [estado_inicial() for _ in range(tam_populacao)]


for _ in range(n_geracoes):
    nova_populacao = []

    for i in range(len(populacao) - tam_elite):
        pai1 = escolhe(populacao)
        pai2 = escolhe(populacao)
        filho = cruzamento(pai1, pai2)
        if random.uniform(0, 1) < taxa_de_mutacao:
            filho = mutacao(filho)
        nova_populacao.append(filho)

    populacao.sort(key=lambda ind: ind.f)
    populacao = nova_populacao + populacao[tam_elite:]

for i in populacao:
    exibe(i)
