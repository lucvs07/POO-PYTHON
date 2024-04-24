# Importando a classes
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Criando Instâncias
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_toku = Restaurante('Toku', 'Japonesa')
restaurante_bk = Restaurante('Burguer King', 'Fast Food')
restaurante_achapa = Restaurante('Achapa', 'Breakfast')

# Alternando o estado de alguns restaurantes
restaurante_achapa.alternar_estado()
restaurante_toku.alternar_estado()

# Avaliando Restaurantes
restaurante_toku.receber_avaliacao('Lucas', 5)
restaurante_toku.receber_avaliacao('Giulia', 3.5)
restaurante_achapa.receber_avaliacao('Aline', 4.5)

#Inserindo Prato e Bebida
bebida_suco = Bebida('Suco de Uva', 4.50, 'Grande')
prato_pao = Prato('Pão de Queijo', 3.50, 'Queijo Cremoso')

#Inserindo Desconto
bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()

# Inserindo Prato e Bebida ao Cardápio
restaurante_achapa.adicionar_no_cardapio(bebida_suco)
restaurante_achapa.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_achapa.exibir_cardapio
if __name__ == '__main__':
    main()