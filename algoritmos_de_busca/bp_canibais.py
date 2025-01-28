def bp(exibe, estado_inicial, objetivo, expande, iguais, visitados):
    fronteira = []

    def adc_na_fronteira(estado):
        fronteira.append(estado)

    def vazia():
        return fronteira == []

    def rmv_da_fronteira():
        return fronteira.pop()

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
        visitados[atual.ce][atual.me][atual.barco] = 1
        exibe(atual)
        if objetivo(atual):
            print("Solução encontrada!")
            mostrar_caminho(atual)
            break

        filhos = expande(atual)
        for filho in filhos:
            if visitados[filho.ce][filho.me][filho.barco]:
                adc_na_fronteira(filho)
                visitados[filho.ce][filho.me][filho.barco] = 1
