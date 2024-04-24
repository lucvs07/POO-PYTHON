# Importando a classe ItemCardapio
from modelos.cardapio.item_cardapio import ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # Recuperando os atributos da classe ItemCardapio
        super().__init__(nome,preco)
        self.descricao = descricao

    def __str__(self) -> str:
        return self._nome
    
    def aplicar_desconto(self):
        # Desconto de 8% no preço do prato
        self._preco -= (self._preco*0.08)