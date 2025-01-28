class Solucao:
    lista = []

    exibe: callable

    estado_inicial: callable

    objetivo: callable

    expande: callable

    def enfileira(self, estado):
        self.lista.append(estado)

    def vazia(self):
        return self.lista == []

    def desenfileira(self):
        return self.lista.pop(0)

    def mostrar_caminho(self, estado):
        if estado is None:
            return

        self.mostrar_caminho(estado.pai)
        self.exibe(estado)

    def resolver(self):
        self.enfileira(self.estado_inicial())
        while not self.vazia():
            atual = self.desenfileira()
            if self.objetivo(atual):
                self.mostrar_caminho(atual)
                break

            filhos = self.expande(atual)
            for filho in filhos:
                self.enfileira(filho)

    def __init__(self, exibe, estado_inicial, objetivo, expande):
        self.exibe = exibe
        self.estado_inicial = estado_inicial
        self.objetivo = objetivo
        self.expande = expande
