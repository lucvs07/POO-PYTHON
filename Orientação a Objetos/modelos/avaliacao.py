'''
Definindo a classe Avaliação
Atributos :
- Cliente
- Nota
'''

class Avaliacao :
    def __init__(self, cliente, nota):
        self._cliente = cliente.title()
        self._nota = nota