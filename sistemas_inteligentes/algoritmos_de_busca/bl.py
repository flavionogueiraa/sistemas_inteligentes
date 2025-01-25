def bl(exibe, estado_inicial, objetivo, expande):
    lista = []

    def enfileira(estado):
        lista.append(estado)

    def vazia():
        return lista == []

    def desenfileira():
        return lista.pop(0)

    def mostrar_caminho(estado):
        if estado is None:
            return

        mostrar_caminho(estado.pai)
        exibe(estado)

    enfileira(estado_inicial())
    while not vazia():
        atual = desenfileira()
        exibe(atual)
        if objetivo(atual):
            print("Solução encontrada!")
            mostrar_caminho(atual)
            break

        filhos = expande(atual)
        for filho in filhos:
            enfileira(filho)
