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
    return estado.valor == 6 or estado.valor == 7


def expande(estado):
    valor = estado.valor
    if valor > 6:
        return []
    return [Estado(2 * valor + 2, estado), Estado(2 * valor + 1, estado)]


limite = 2

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

    if atual.nivel < limite:
        filhos = expande(atual)
        for filho in filhos:
            empilha(filho)
