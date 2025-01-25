mapa = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", " ", " ", " ", " ", "x", "G", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", "x"],
    ["x", " ", "x", "x", "x", "x", "x", "x", "x", "x", "x", " ", " ", "x"],
    ["x", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", "x", " ", " ", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]


class Estado:
    def __init__(self, linha, coluna, pai):
        self.linha = linha
        self.coluna = coluna
        self.pai = pai


def exibe(estado):
    print(f"({estado.linha}, {estado.coluna})")


def estado_inicial():
    return Estado(1, 1, None)


def objetivo(estado):
    return mapa[estado.linha][estado.coluna] == "G"


def valido(estado):
    return mapa[estado.linha][estado.coluna] != "x"


def mover(estado, dir_vert, dir_hor):
    return Estado(estado.linha + dir_vert, estado.coluna + dir_hor, estado)


def expande(estado):
    estados_filhos = []
    direcoes = [
        [-1, 0],  # Move pra cima
        [+1, 0],  # Move pra baixo
        [0, -1],  # Move pra esquerda
        [0, +1],  # Move pra direita
    ]
    for direcao in direcoes:
        filho = mover(estado, direcao[0], direcao[1])
        if valido(filho):
            estados_filhos.append(filho)

    return estados_filhos


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
    mapa[estado.linha][estado.coluna] = "#"


def iguais(estado1, estado2):
    return estado1.linha == estado2.linha and estado1.coluna == estado2.coluna


def em_ancestrais(filho):
    ancestral = filho.pai
    while ancestral is not None:
        if iguais(filho, ancestral):
            return True

        ancestral = ancestral.pai

    return False


def esta_na_fronteira(filho):
    for estado in fronteira:
        if iguais(estado, filho):
            return True

    return False


def esta_em_visitados(filho):
    for estado in visitados:
        if iguais(estado, filho):
            return True

    return False


total_visitados = 0
tam_max_fronteira = 0
visitados = []

matriz_visitados = []
for linha in mapa:
    linha_visitados = [0] * len(linha)
    matriz_visitados.append(linha_visitados)

adc_na_fronteira(estado_inicial())
while not vazia():
    tam_max_fronteira = max(tam_max_fronteira, len(fronteira))
    atual = rmv_da_fronteira()
    total_visitados += 1
    exibe(atual)
    if objetivo(atual):
        print("Solução encontrada!")
        mostrar_caminho(atual)
        break

    # visitados.append(atual)
    matriz_visitados[atual.linha][atual.coluna] = 1
    filhos = expande(atual)

    for filho in filhos:
        # if (
        #     not em_ancestrais(filho)
        #     and not esta_na_fronteira(filho)
        #     and not esta_em_visitados(filho)
        # ):
        if matriz_visitados[filho.linha][filho.coluna] != 1:
            adc_na_fronteira(filho)
            matriz_visitados[filho.linha][filho.coluna] = 1

print(f"Total de visitados: {total_visitados}")
print(f"Tamanho máximo da fronteira: {tam_max_fronteira}")
for linha in mapa:
    print(linha)
