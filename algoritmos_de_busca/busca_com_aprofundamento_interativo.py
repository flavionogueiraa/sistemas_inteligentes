class Estado:
    def __init__(self, valor, pai):
        self.valor = valor
        self.pai = pai
        self.nivel = 0 if pai is None else pai.nivel + 1


def exibe(estado):
    print(estado.valor)


def estado_inicial():
    return Estado(0, None)


def objetivo(estado):
    return False
    # return estado.valor == 6 or estado.valor == 7


def expande(estado):
    valor = estado.valor
    if valor > 6:
        return []
    return [Estado(2 * valor + 2, estado), Estado(2 * valor + 1, estado)]


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
