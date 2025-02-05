import random

# def quantidade_nao_ameacadas(vetor):
#     qtd = 0
#     for i in range(8):
#         ameacada = False
#         for j in range(8):
#             if i == j:
#                 continue

#             if vetor[i] == vetor[j]:
#                 ameacada = True
#                 break

#         if not ameacada:
#             qtd += 1

#     return qtd


# def f(colunas):
#     """Função objetivo."""
#     linha_mais_coluna = [i + coluna for i, coluna in enumerate(colunas)]
#     linha_menos_coluna = [i - coluna for i, coluna in enumerate(colunas)]

#     qtd_nao_ameacadas = 0
#     qtd_nao_ameacadas += quantidade_nao_ameacadas(colunas)
#     qtd_nao_ameacadas += quantidade_nao_ameacadas(linha_mais_coluna)
#     qtd_nao_ameacadas += quantidade_nao_ameacadas(linha_menos_coluna)

#     return qtd_nao_ameacadas


def ameaca(i, j, rainhas):
    col_i = rainhas[i]
    col_j = rainhas[j]

    if col_i == col_j:
        return True

    diag_desc_i = i + col_i
    diag_desc_j = j + col_j

    if diag_desc_i == diag_desc_j:
        return True

    diag_asc_i = i - col_i
    diag_asc_j = j - col_j

    if diag_asc_i == diag_asc_j:
        return True

    return False


def f(rainhas):
    cont = 0
    for i in range(len(rainhas)):
        ameacada = False
        for j in range(len(rainhas)):
            if i == j:
                continue

            if ameaca(i, j, rainhas):
                ameacada = True
                break

        if not ameacada:
            cont += 1
    return cont


class Estado:
    def __init__(self, rainhas):
        self.rainhas = rainhas
        self.f = f(rainhas)


def exibe(estado):
    print(f"Colunas: {estado.rainhas} F:{estado.f}")


def estado_inicial():
    return Estado([random.randint(0, 7) for _ in range(8)])


def escolhe(populacao):
    ind1 = random.choice(populacao)
    ind2 = random.choice(populacao)

    if ind1.f > ind2.f:
        return ind1
    return ind2


# def cruzamento(pai1, pai2):
#     colunas = [
#         random.randint(
#             min(coluna_pai1, coluna_pai2), max(coluna_pai1, coluna_pai2)
#         )
#         for coluna_pai1, coluna_pai2 in zip(pai1.colunas, pai2.colunas)
#     ]
#     return Estado(colunas)


def cruzamento(pai1, pai2):
    rainhas = []
    for i in range(len(pai1.rainhas)):
        rainha = random.choice([pai1.rainhas[i], pai2.rainhas[i]])
        rainhas.append(rainha)

    return Estado(rainhas)


# def mutacao(individuo):
#     colunas = [coluna + random.randint(-1, 1) for coluna in individuo.colunas]
#     colunas_validas = []
#     for coluna in colunas:
#         coluna = min(coluna, 7)
#         coluna = max(coluna, 0)

#         colunas_validas.append(coluna)
#     return Estado(colunas_validas)


def mutacao(individuo):
    i = random.randint(0, 7)
    rainhas = individuo.rainhas.copy()
    rainhas[i] = random.randint(0, 7)
    return Estado(rainhas)


tam_populacao = 10
n_geracoes = 15
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
