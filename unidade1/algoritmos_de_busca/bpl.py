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
