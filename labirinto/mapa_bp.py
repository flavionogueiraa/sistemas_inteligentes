mapa = [
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", "G", "x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", "x", "x", "x", "x", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
    ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
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


lista = []


def empilha(estado):
    lista.append(estado)


def vazia():
    return lista == []


def desempilha():
    return lista.pop()


def mostrar_caminho(estado):
    if estado is None:
        return

    mostrar_caminho(estado.pai)
    exibe(estado)


empilha(estado_inicial())
while not vazia():
    atual = desempilha()
    exibe(atual)

    if objetivo(atual):
        print("Solução encontrada!")
        mostrar_caminho(atual)
        break

    mapa[atual.linha][atual.coluna] = "*"

    filhos = expande(atual)
    for filho in filhos:
        if mapa[filho.linha][filho.coluna] != "*":
            empilha(filho)
