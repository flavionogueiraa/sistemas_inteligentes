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
