from copy import deepcopy


class Estado:
    def __init__(self, esquerda, direita, barco, pai):
        self.esquerda = esquerda
        # array de arrays que representa os casais que estão na esquerda, cada posição do array representa um casal.

        self.direita = direita
        # array de arrays que representa os casais que estão na direita, cada posição do array representa um casal.

        # O marido sempre vai estar na primeira posição do array interno, e a esposa na segunda posição: [[0,0], [0,0], [0,0]]

        self.barco = barco
        # A posição do barco será representada por "d" quando ele estiver na direita e "e", quando estiver na esquerda

        self.pai = pai
        self.nivel = 0 if pai is None else pai.nivel + 1


def exibe(estado):
    if estado.barco == "d":
        barco = " *"
    else:
        barco = "* "
    print(f"{estado.esquerda} |{barco}| {estado.direita}")


def estado_inicial():
    # Supondo que os casais estão na margem esquerda do rio
    return Estado(
        [[1, 1], [1, 1], [1, 1]], [[0, 0], [0, 0], [0, 0]], "e", None
    )


def estado_objetivo(estado):
    # Supondo que o objetivo seja levar todos os casais para a margem direita do rio
    return (
        estado.esquerda == [[0, 0], [0, 0], [0, 0]]
        and estado.direita == [[1, 1], [1, 1], [1, 1]]
        and estado.barco == "d"
    )


def valido(estado):
    if estado.esquerda[0][1] == 1:
        if estado.esquerda[0][0] != 1:
            if estado.esquerda[1][0] == 1 or estado.esquerda[2][0] == 1:
                return False

    if estado.esquerda[1][1] == 1:
        if estado.esquerda[1][0] != 1:
            if estado.esquerda[0][0] == 1 or estado.esquerda[2][0] == 1:
                return False

    if estado.esquerda[2][1] == 1:
        if estado.esquerda[2][0] != 1:
            if estado.esquerda[0][0] == 1 or estado.esquerda[1][0] == 1:
                return False

    if estado.direita[0][1] == 1:
        if estado.direita[0][0] != 1:
            if estado.direita[1][0] == 1 or estado.direita[2][0] == 1:
                return False

    if estado.direita[1][1] == 1:
        if estado.direita[1][0] != 1:
            if estado.direita[0][0] == 1 or estado.direita[2][0] == 1:
                return False

    if estado.direita[2][1] == 1:
        if estado.direita[2][0] != 1:
            if estado.direita[0][0] == 1 or estado.direita[1][0] == 1:
                return False

    return True


# def acao_levar_mulher(estado, casal):
#     esquerda = estado.esquerda
#     direita = estado.direita
#     barco = estado.barco

#     if estado.barco == "d":
#         esquerda[casal][1] = 1
#         direita[casal][1] = 0
#         barco = "e"
#     else:
#         esquerda[casal][1] = 0
#         direita[casal][1] = 1
#         barco = "d"

#     return Estado(esquerda, direita, barco)


# def acao_levar_marido(estado, casal):
#     esquerda = estado.esquerda
#     direita = estado.direita
#     barco = estado.barco

#     if estado.barco == "d":
#         esquerda[casal][0] = 1
#         direita[casal][0] = 0
#         barco = "e"
#     else:
#         esquerda[casal][0] = 0
#         direita[casal][0] = 1
#         barco = "d"

#     return Estado(esquerda, direita, barco)


def levar(estado, casais, pessoas):
    esquerda = deepcopy(estado.esquerda)
    direita = deepcopy(estado.direita)
    barco = deepcopy(estado.barco)

    if estado.barco == "d":
        if direita[casais[0]][pessoas[0]] == 0:
            return None

        esquerda[casais[0]][pessoas[0]] = 1
        direita[casais[0]][pessoas[0]] = 0

        if casais[1] is not None and pessoas[1] is not None:
            if direita[casais[1]][pessoas[1]] == 0:
                return None

            esquerda[casais[1]][pessoas[1]] = 1
            direita[casais[1]][pessoas[1]] = 0

        barco = "e"
    else:
        if esquerda[casais[0]][pessoas[0]] == 0:
            return None

        esquerda[casais[0]][pessoas[0]] = 0
        direita[casais[0]][pessoas[0]] = 1

        if casais[1] is not None and pessoas[1] is not None:
            if esquerda[casais[1]][pessoas[1]] == 0:
                return None

            esquerda[casais[1]][pessoas[1]] = 0
            direita[casais[1]][pessoas[1]] = 1

        barco = "d"

    return Estado(esquerda, direita, barco, estado)


def expande(estado):
    movimentos = [
        [[0, None], [0, None]],  # Leva a esposa do primeiro casal
        [[0, None], [1, None]],  # Leva o marido do primeiro casal
        #
        [[1, None], [0, None]],  # Leva a esposa do segundo casal
        [[1, None], [1, None]],  # Leva o marido do segundo casal
        #
        [[2, None], [0, None]],  # Leva a esposa do terceiro casal
        [[2, None], [1, None]],  # Leva o marido do terceiro casal
        #
        [[0, 0], [0, 1]],  # Leva a esposa e o marido do primeiro casal
        [[1, 1], [0, 1]],  # Leva a esposa e o marido do segundo casal
        [[2, 2], [0, 1]],  # Leva a esposa e o marido do terceiro casal
        #
        [[0, 1], [0, 0]],  # Leva a primeira e a segunda esposa
        [[0, 2], [0, 0]],  # Leva a primeira e a terceira esposa
        [[1, 2], [0, 0]],  # Leva a segunda e a terceira esposa
        #
        [[0, 1], [1, 1]],  # Leva o primeiro e o segundo marido
        [[0, 2], [1, 1]],  # Leva o primeiro e o terceiro marido
        [[1, 2], [1, 1]],  # Leva o segundo e o terceiro marido
    ]

    filhos = []
    for movimento in movimentos:
        filho = levar(estado, movimento[0], movimento[1])
        if filho is not None and valido(filho):
            filhos.append(filho)

    return filhos


def iguais(estado1, estado2):
    return (
        estado1.esquerda == estado2.esquerda
        and estado1.direita == estado2.direita
        and estado1.barco == estado2.barco
    )


fronteira = []


def adc_na_fronteira(estado):
    fronteira.append(estado)


def vazia():
    return fronteira == []


def rmv_da_fronteira():
    return fronteira.pop(0)


def mostrar_caminho(estado):
    if estado is None:
        return

    mostrar_caminho(estado.pai)
    exibe(estado)


def em_ancestrais(filho):
    ancestral = filho.pai
    while ancestral is not None:
        if iguais(filho, ancestral):
            return True

        ancestral = ancestral.pai

    return False


adc_na_fronteira(estado_inicial())
while not vazia():
    atual = rmv_da_fronteira()
    # exibe(atual)
    if estado_objetivo(atual):
        # print("Solução encontrada!")
        mostrar_caminho(atual)
        break

    filhos = expande(atual)
    for filho in filhos:
        if not em_ancestrais(filho):
            adc_na_fronteira(filho)
