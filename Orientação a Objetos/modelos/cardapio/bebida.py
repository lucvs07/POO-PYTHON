# Importando a classe ItemCardapio
from modelos.cardapio.item_cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        # Recuperando atributos da classe ItemCardapio
        super().__init__(nome,preco)
        self.tamanho = tamanho
    
    def __str__(self) -> str:
        return self._nome
    
    def aplicar_desconto(self):
        # Desconto de 5% no preço da bebida
        self._preco -= (self._preco*0.05)