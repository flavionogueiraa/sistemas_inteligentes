import random

tempos = [
    [8, 6, 2, 9, 5, 6, 1, 6, 3, 1, 8, 9, 2, 4, 7, 4, 8, 10, 8, 1, 9, 5, 8, 8, 3, 8, 7, 8, 10, 6, 10, 4, 9, 3, 7, 2, 5, 1, 7, 4, 9, 1, 5, 6, 9, 6, 3, 7, 3, 3],  # noqa E501
    [1, 2, 5, 9, 8, 2, 1, 10, 9, 10, 2, 5, 10, 2, 4, 1, 6, 5, 5, 4, 6, 1, 9, 6, 10, 5, 9, 2, 4, 7, 4, 10, 4, 6, 4, 2, 1, 2, 3, 9, 2, 1, 2, 3, 8, 5, 3, 3, 2, 9],  # noqa E501
    [9, 9, 5, 4, 10, 8, 10, 8, 6, 8, 5, 3, 5, 7, 10, 6, 6, 2, 8, 10, 2, 8, 5, 10, 8, 2, 4, 7, 3, 8, 8, 6, 5, 3, 2, 7, 4, 4, 6, 8, 7, 3, 2, 4, 2, 5, 7, 1, 5, 6],  # noqa E501
    [1, 5, 8, 9, 6, 3, 7, 1, 8, 7, 7, 7, 4, 3, 3, 7, 2, 6, 1, 7, 9, 3, 9, 5, 4, 2, 6, 7, 9, 3, 5, 8, 2, 6, 9, 5, 6, 2, 10, 5, 5, 6, 1, 1, 7, 6, 4, 3, 2, 9],  # noqa E501
    [5, 7, 4, 8, 2, 9, 1, 3, 2, 4, 10, 7, 8, 6, 9, 5, 5, 9, 10, 7, 9, 2, 7, 6, 9, 7, 7, 1, 7, 9, 9, 4, 8, 7, 1, 3, 10, 10, 7, 6, 5, 9, 2, 3, 6, 7, 7, 9, 3, 6],  # noqa E501
    [1, 4, 2, 3, 6, 7, 9, 8, 10, 5, 9, 4, 8, 9, 3, 8, 3, 4, 9, 3, 6, 1, 10, 2, 7, 7, 4, 7, 2, 4, 6, 8, 5, 1, 1, 9, 10, 6, 7, 9, 10, 7, 9, 9, 6, 9, 8, 3, 2, 5],  # noqa E501
    [5, 9, 5, 4, 6, 5, 4, 9, 9, 1, 8, 5, 6, 9, 4, 1, 1, 6, 3, 1, 10, 3, 4, 10, 10, 4, 2, 5, 2, 5, 6, 4, 4, 6, 4, 5, 2, 1, 10, 2, 5, 4, 4, 5, 3, 3, 4, 9, 6, 6],  # noqa E501
    [7, 4, 5, 8, 3, 10, 3, 2, 7, 6, 10, 2, 9, 2, 5, 10, 7, 4, 9, 1, 7, 9, 9, 7, 8, 9, 8, 1, 5, 9, 9, 8, 4, 1, 4, 2, 5, 5, 4, 1, 7, 8, 9, 10, 7, 7, 10, 8, 9, 8],  # noqa E501
    [5, 2, 2, 4, 6, 9, 5, 10, 3, 3, 3, 6, 6, 4, 5, 9, 8, 10, 1, 7, 3, 9, 3, 10, 3, 6, 2, 2, 5, 8, 10, 4, 2, 7, 10, 7, 2, 2, 5, 3, 5, 10, 3, 3, 9, 10, 9, 9, 4, 5],  # noqa E501
    [6, 7, 5, 4, 3, 7, 9, 1, 3, 1, 2, 6, 9, 1, 2, 4, 7, 4, 3, 7, 7, 5, 3, 9, 8, 6, 1, 1, 6, 2, 1, 8, 2, 5, 8, 4, 7, 8, 6, 3, 3, 4, 8, 3, 4, 3, 8, 1, 6, 10],  # noqa E501
    [1, 9, 5, 6, 3, 1, 10, 10, 8, 6, 9, 5, 8, 8, 10, 1, 9, 1, 3, 10, 10, 10, 1, 8, 4, 9, 4, 2, 8, 6, 8, 3, 6, 4, 3, 3, 2, 1, 4, 7, 2, 3, 1, 2, 4, 1, 6, 3, 6, 2],  # noqa E501
    [7, 4, 9, 5, 7, 9, 10, 5, 2, 7, 9, 9, 9, 2, 7, 4, 3, 2, 4, 8, 2, 5, 5, 8, 5, 6, 5, 7, 9, 10, 9, 1, 8, 9, 2, 7, 9, 1, 5, 7, 7, 6, 1, 1, 5, 6, 7, 3, 2, 1],  # noqa E501
    [1, 9, 2, 2, 10, 3, 2, 8, 9, 8, 6, 7, 4, 3, 10, 7, 1, 10, 8, 7, 9, 8, 8, 3, 7, 4, 2, 9, 5, 6, 1, 2, 10, 1, 8, 1, 6, 1, 7, 3, 10, 2, 7, 1, 2, 2, 4, 8, 6, 6],  # noqa E501
    [7, 5, 4, 3, 2, 6, 8, 1, 6, 1, 1, 9, 7, 8, 2, 1, 1, 5, 4, 10, 5, 2, 2, 7, 3, 4, 2, 6, 10, 6, 3, 4, 5, 10, 3, 8, 9, 4, 3, 8, 3, 7, 10, 5, 7, 6, 2, 1, 7, 1],  # noqa E501
    [6, 3, 5, 9, 1, 7, 7, 2, 1, 2, 4, 6, 2, 8, 2, 10, 6, 4, 9, 3, 2, 10, 9, 6, 2, 7, 4, 7, 3, 4, 4, 7, 8, 6, 9, 6, 9, 10, 5, 1, 5, 7, 9, 5, 3, 10, 4, 7, 7, 7],  # noqa E501
    [9, 9, 10, 1, 6, 1, 7, 7, 3, 3, 8, 7, 10, 5, 1, 1, 9, 3, 1, 5, 7, 8, 5, 1, 3, 7, 5, 8, 1, 10, 8, 7, 1, 9, 1, 1, 8, 5, 4, 4, 8, 2, 1, 2, 4, 10, 5, 2, 5, 8],  # noqa E501
    [1, 8, 2, 3, 5, 1, 1, 2, 8, 1, 1, 3, 6, 5, 5, 5, 10, 3, 5, 7, 2, 10, 10, 10, 6, 1, 7, 10, 6, 7, 2, 6, 10, 10, 8, 10, 10, 5, 5, 1, 1, 2, 8, 7, 5, 2, 10, 10, 6, 3],  # noqa E501
    [3, 10, 5, 10, 6, 7, 1, 8, 10, 8, 4, 2, 4, 6, 10, 8, 4, 2, 2, 1, 8, 2, 7, 4, 2, 7, 7, 7, 4, 7, 8, 4, 3, 7, 10, 1, 10, 1, 6, 9, 10, 6, 10, 10, 10, 8, 2, 9, 10, 4],  # noqa E501
    [9, 4, 1, 4, 8, 9, 9, 2, 4, 10, 10, 9, 5, 8, 5, 6, 1, 2, 5, 4, 4, 3, 3, 3, 3, 4, 9, 10, 4, 7, 10, 3, 1, 1, 8, 8, 1, 4, 4, 8, 3, 7, 6, 1, 7, 4, 4, 5, 5, 2],  # noqa E501
    [7, 2, 9, 9, 5, 6, 7, 6, 9, 3, 10, 5, 6, 2, 4, 7, 3, 2, 7, 9, 7, 6, 1, 4, 10, 5, 6, 4, 3, 5, 8, 4, 9, 5, 5, 7, 1, 1, 2, 4, 5, 6, 1, 2, 5, 2, 10, 7, 7, 8],  # noqa E501
    [10, 1, 6, 10, 7, 8, 2, 6, 8, 6, 1, 6, 3, 10, 6, 6, 4, 1, 2, 1, 1, 10, 6, 10, 3, 2, 8, 5, 5, 7, 1, 6, 8, 7, 10, 4, 5, 10, 5, 7, 2, 5, 10, 4, 9, 8, 8, 9, 5, 10],  # noqa E501
    [9, 8, 8, 3, 9, 2, 3, 1, 5, 1, 1, 10, 9, 7, 4, 6, 5, 9, 1, 8, 8, 3, 1, 3, 7, 7, 3, 1, 2, 8, 10, 9, 2, 5, 7, 5, 2, 10, 2, 9, 8, 5, 1, 4, 9, 3, 4, 9, 10, 3],  # noqa E501
    [8, 9, 1, 2, 9, 4, 4, 9, 4, 3, 8, 9, 4, 10, 3, 7, 5, 7, 3, 4, 9, 4, 10, 10, 2, 7, 6, 1, 2, 9, 6, 4, 5, 6, 6, 4, 7, 6, 2, 5, 10, 4, 3, 2, 8, 1, 5, 9, 5, 9],  # noqa E501
    [8, 4, 3, 1, 4, 5, 9, 6, 4, 5, 2, 1, 10, 9, 9, 7, 10, 10, 4, 2, 8, 9, 8, 2, 8, 5, 8, 8, 7, 5, 9, 5, 3, 3, 5, 9, 8, 3, 6, 8, 10, 6, 9, 10, 4, 1, 9, 10, 10, 8],  # noqa E501
    [9, 6, 3, 4, 8, 10, 6, 10, 9, 9, 2, 7, 4, 10, 9, 1, 4, 2, 2, 10, 10, 5, 2, 7, 1, 10, 2, 9, 6, 2, 3, 9, 1, 8, 10, 1, 4, 5, 9, 5, 8, 2, 2, 5, 1, 10, 6, 10, 1, 8],  # noqa E501
    [7, 6, 8, 1, 8, 7, 3, 5, 3, 6, 7, 4, 4, 2, 3, 5, 4, 10, 10, 4, 4, 9, 2, 7, 6, 2, 9, 5, 4, 9, 4, 8, 10, 1, 8, 2, 3, 2, 3, 8, 10, 3, 5, 6, 10, 1, 9, 1, 4, 6],  # noqa E501
    [9, 5, 10, 1, 9, 7, 7, 7, 9, 7, 8, 3, 4, 4, 10, 7, 9, 3, 3, 5, 2, 2, 7, 2, 3, 6, 5, 8, 6, 4, 8, 10, 3, 5, 5, 7, 8, 7, 7, 7, 7, 8, 10, 1, 1, 7, 5, 9, 2, 3],  # noqa E501
    [6, 6, 4, 5, 5, 10, 10, 1, 10, 6, 10, 9, 2, 4, 2, 10, 10, 9, 8, 2, 8, 8, 6, 10, 3, 3, 9, 2, 1, 3, 9, 8, 7, 5, 3, 3, 3, 4, 3, 10, 9, 3, 9, 8, 3, 10, 10, 5, 4, 4],  # noqa E501
    [2, 10, 9, 5, 10, 7, 10, 1, 5, 4, 6, 10, 7, 3, 5, 9, 10, 6, 2, 8, 10, 7, 6, 4, 7, 2, 2, 4, 8, 1, 4, 7, 9, 7, 5, 4, 4, 5, 2, 7, 3, 1, 5, 1, 4, 6, 2, 2, 6, 7],  # noqa E501
    [5, 10, 2, 4, 10, 6, 4, 9, 9, 10, 3, 1, 6, 8, 3, 6, 10, 9, 2, 10, 6, 10, 3, 1, 7, 9, 8, 3, 10, 2, 3, 5, 9, 1, 9, 1, 8, 6, 5, 8, 3, 1, 2, 9, 1, 4, 6, 1, 5, 5],  # noqa E501
    [2, 3, 9, 8, 1, 7, 2, 5, 8, 6, 6, 4, 2, 8, 2, 3, 1, 2, 6, 6, 4, 6, 3, 4, 9, 9, 8, 10, 4, 6, 2, 6, 10, 6, 10, 7, 8, 1, 6, 7, 2, 3, 7, 6, 9, 7, 6, 4, 3, 1],  # noqa E501
    [9, 4, 10, 6, 6, 1, 8, 1, 9, 7, 2, 9, 10, 3, 9, 6, 9, 8, 3, 8, 6, 8, 8, 1, 3, 8, 2, 1, 2, 9, 3, 10, 8, 1, 3, 6, 9, 3, 2, 8, 2, 3, 3, 4, 3, 10, 7, 5, 2, 1],  # noqa E501
    [4, 3, 6, 1, 2, 10, 10, 7, 9, 7, 10, 8, 9, 10, 2, 5, 6, 9, 9, 2, 7, 9, 6, 6, 5, 7, 2, 5, 10, 4, 5, 7, 8, 10, 7, 8, 9, 4, 2, 6, 8, 1, 4, 2, 1, 7, 10, 8, 10, 8],  # noqa E501
    [6, 10, 6, 7, 1, 2, 6, 4, 9, 4, 2, 5, 1, 6, 8, 8, 7, 8, 8, 4, 9, 6, 7, 2, 3, 9, 9, 4, 4, 1, 8, 2, 1, 10, 9, 2, 1, 2, 10, 5, 3, 6, 9, 2, 6, 5, 10, 7, 5, 1],  # noqa E501
    [4, 5, 4, 10, 4, 6, 4, 7, 4, 8, 2, 7, 1, 5, 7, 2, 8, 5, 4, 3, 5, 7, 2, 6, 10, 3, 9, 1, 10, 10, 5, 9, 8, 6, 8, 1, 3, 1, 2, 3, 3, 5, 2, 5, 3, 7, 1, 1, 7, 2],  # noqa E501
    [10, 9, 10, 9, 3, 9, 10, 8, 6, 2, 2, 10, 9, 10, 9, 6, 9, 5, 10, 1, 10, 5, 10, 1, 5, 8, 9, 8, 5, 10, 10, 2, 5, 1, 7, 10, 6, 8, 7, 2, 6, 4, 3, 8, 3, 8, 7, 2, 9, 7],  # noqa E501
    [10, 4, 9, 1, 5, 3, 1, 6, 10, 8, 7, 7, 7, 5, 9, 4, 1, 9, 1, 4, 9, 3, 4, 8, 6, 2, 4, 2, 6, 8, 3, 6, 9, 9, 1, 6, 1, 5, 1, 9, 10, 6, 7, 9, 6, 1, 6, 3, 3, 8],  # noqa E501
    [10, 8, 4, 7, 7, 4, 9, 1, 2, 9, 9, 1, 7, 8, 10, 5, 8, 1, 10, 3, 1, 7, 6, 5, 5, 7, 8, 10, 5, 4, 5, 7, 5, 1, 5, 7, 5, 9, 8, 8, 3, 10, 7, 4, 10, 9, 7, 5, 2, 10],  # noqa E501
    [5, 6, 1, 9, 3, 2, 2, 7, 9, 6, 9, 4, 9, 9, 4, 1, 6, 5, 2, 3, 8, 4, 5, 3, 6, 1, 9, 1, 9, 10, 9, 2, 6, 4, 4, 9, 3, 6, 1, 4, 8, 2, 8, 8, 4, 6, 6, 1, 8, 1],  # noqa E501
    [4, 4, 2, 8, 8, 8, 8, 10, 7, 1, 10, 7, 10, 9, 2, 3, 1, 6, 2, 9, 2, 3, 6, 9, 10, 10, 9, 3, 10, 1, 3, 6, 1, 3, 3, 9, 10, 5, 7, 3, 3, 3, 2, 10, 9, 10, 6, 2, 1, 6],  # noqa E501
    [1, 5, 7, 8, 4, 6, 4, 4, 6, 2, 10, 2, 8, 4, 1, 1, 3, 9, 2, 3, 1, 10, 3, 2, 1, 5, 9, 2, 2, 4, 7, 7, 7, 4, 5, 9, 5, 1, 2, 4, 9, 8, 4, 5, 6, 4, 10, 4, 2, 7],  # noqa E501
    [10, 2, 9, 2, 3, 8, 5, 10, 7, 10, 4, 6, 4, 6, 7, 3, 4, 4, 1, 3, 1, 10, 10, 8, 4, 3, 6, 8, 8, 10, 4, 9, 6, 10, 9, 7, 9, 7, 3, 8, 10, 3, 9, 8, 9, 2, 6, 1, 1, 8],  # noqa E501
    [2, 5, 8, 9, 4, 1, 9, 5, 3, 2, 8, 7, 4, 8, 10, 7, 9, 9, 10, 3, 4, 7, 8, 7, 4, 8, 5, 10, 3, 5, 7, 8, 2, 9, 9, 5, 3, 7, 9, 4, 4, 7, 5, 4, 7, 3, 9, 6, 5, 9],  # noqa E501
    [3, 1, 3, 1, 10, 9, 4, 1, 1, 10, 5, 3, 7, 3, 4, 9, 3, 6, 9, 10, 8, 9, 9, 7, 6, 3, 10, 9, 6, 4, 1, 5, 9, 9, 10, 5, 9, 5, 8, 9, 6, 5, 10, 10, 1, 2, 7, 5, 7, 4],  # noqa E501
    [4, 7, 5, 10, 4, 2, 3, 1, 9, 4, 1, 9, 5, 2, 3, 9, 7, 2, 4, 9, 4, 6, 1, 8, 7, 9, 10, 2, 3, 6, 6, 8, 10, 7, 1, 9, 3, 6, 10, 5, 4, 6, 4, 7, 3, 6, 5, 3, 9, 5],  # noqa E501
    [5, 9, 7, 7, 2, 3, 3, 1, 1, 4, 9, 9, 4, 3, 1, 4, 2, 3, 9, 4, 10, 2, 8, 5, 1, 7, 9, 7, 2, 1, 7, 8, 7, 7, 7, 7, 4, 4, 4, 10, 4, 10, 7, 6, 8, 3, 10, 4, 3, 4],  # noqa E501
    [2, 4, 7, 3, 2, 10, 6, 7, 2, 10, 7, 4, 5, 9, 6, 1, 2, 3, 2, 3, 5, 10, 6, 7, 1, 9, 7, 5, 8, 7, 7, 8, 6, 5, 8, 4, 7, 10, 3, 7, 1, 1, 8, 7, 9, 5, 1, 7, 9, 7],  # noqa E501
    [7, 3, 6, 5, 7, 3, 6, 7, 5, 10, 6, 7, 5, 9, 10, 2, 8, 3, 9, 8, 7, 5, 10, 1, 4, 1, 6, 8, 7, 8, 6, 6, 4, 5, 1, 3, 6, 9, 3, 9, 2, 5, 3, 9, 3, 6, 4, 6, 1, 6],  # noqa E501
    [2, 4, 6, 2, 4, 1, 10, 9, 7, 1, 9, 9, 9, 1, 8, 6, 8, 1, 5, 8, 6, 9, 7, 4, 6, 1, 9, 9, 6, 10, 2, 6, 1, 8, 6, 9, 5, 10, 5, 9, 3, 3, 1, 3, 6, 9, 3, 10, 7, 9],  # noqa E501
    [9, 1, 9, 6, 7, 6, 9, 7, 1, 3, 2, 9, 7, 5, 5, 1, 6, 7, 9, 4, 9, 1, 7, 9, 4, 5, 5, 3, 6, 6, 7, 5, 2, 3, 5, 6, 9, 1, 7, 7, 7, 8, 3, 10, 9, 2, 6, 9, 8, 10],  # noqa E501
]

limite_centros = 5


def f(centros_escolhidos):
    menores_tempos = [11] * len(tempos)
    for i, centro in enumerate(centros_escolhidos):
        if centro == 1:
            maior_tempo = max(tempos[i])
            menores_tempos[i] = min(menores_tempos[i], maior_tempo)

    return max(menores_tempos)


class Estado:
    centros_escolhidos = []

    def __init__(self, centros_escolhidos):
        self.centros_escolhidos = centros_escolhidos
        self.f = f(centros_escolhidos)


def exibe(estado):
    print(f"Centros escolhidos: {estado.centros_escolhidos}, f: {estado.f}")


def estado_inicial():
    centros_escolhidos = [random.choice([0, 1]) for _ in tempos]
    return Estado(centros_escolhidos)


def mutacao(estado):
    centros_escolhidos = estado.centros_escolhidos.copy()
    probabilidade_mudanca = 0.1

    for i, _ in enumerate(centros_escolhidos):
        if random.randint(0, 1) < probabilidade_mudanca:
            centros_escolhidos[i] = 1 - centros_escolhidos[i]

    return Estado(centros_escolhidos)


def cruzamento(estado1, estado2):
    centros_escolhidos = []
    for centro1, centro2 in zip(
        estado1.centros_escolhidos,
        estado2.centros_escolhidos
    ):
        centro = random.choice([centro1, centro2])
        centros_escolhidos.append(centro)

    return Estado(centros_escolhidos)


def melhor_sucessor(estado):
    melhor = estado
    for _ in range(5):
        vizinho = mutacao(melhor)
        if vizinho.f < melhor.f:
            melhor = vizinho

    return melhor


melhor = estado_inicial()


while True:
    atual = estado_inicial()
    while True:
        vizinho = melhor_sucessor(atual)
        if vizinho.f >= atual.f:
            break
        atual = vizinho

    if atual.f < melhor.f:
        exibe(atual)
        melhor = atual
