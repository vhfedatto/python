class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def incluir(self, chave):
        self.raiz = self._incluir(self.raiz, chave)

    def _incluir(self, no, chave):
        if no is None:
            return No(chave)

        if chave < no.chave:
            no.esquerda = self._incluir(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._incluir(no.direita, chave)

        return no

    def localizar(self, chave):
        return self._localizar(self.raiz, chave)

    def _localizar(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._localizar(no.esquerda, chave)
        else:
            return self._localizar(no.direita, chave)

    def visualizar(self):
        self._visualizar(self.raiz)

    def _visualizar(self, no):
        if no is not None:
            self._visualizar(no.esquerda)
            print(no.chave, end=" ")
            self._visualizar(no.direita)

    def pre_order_traversal(self):
        self._pre_order_traversal(self.raiz)
        print()

    def _pre_order_traversal(self, no):
        if no:
            print(no.chave, end=' ')
            self._pre_order_traversal(no.esquerda)
            self._pre_order_traversal(no.direita)

    def in_order_traversal(self):
        self._in_order_traversal(self.raiz)
        print()

    def _in_order_traversal(self, no):
        if no:
            self._in_order_traversal(no.esquerda)
            print(no.chave, end=' ')
            self._in_order_traversal(no.direita)

    def post_order_traversal(self):
        self._post_order_traversal(self.raiz)
        print()

    def _post_order_traversal(self, no):
        if no:
            self._post_order_traversal(no.esquerda)
            self._post_order_traversal(no.direita)
            print(no.chave, end=' ')