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
        self.nivel = 0 if pai is None else pai.nivel + 1


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


limite = 0
resolvido = False

while True:
    print(f"Executando busca com limite: {limite}")

    lista = []
    empilha(estado_inicial())
    nivel_maximo = 0

    while not vazia():
        atual = desempilha()
        exibe(atual)
        nivel_maximo = max(nivel_maximo, atual.nivel)

        if objetivo(atual):
            print("Solução encontrada!")
            mostrar_caminho(atual)
            resolvido = True
            break

        if atual.nivel < limite:
            filhos = expande(atual)
            for filho in filhos:
                empilha(filho)

    if resolvido:
        break

    if nivel_maximo < limite:
        print("Espaço de estado esgotado!")
        break

    limite = limite + 1
