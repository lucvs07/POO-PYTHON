# Importar a classe Avaliação
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
'''
Definindo a classe Restaurante
Atributos :
- Nome
- Categoria
- Ativo
'''
class Restaurante:
    # Lista(array) Restaurantes -> Armazena os restaurantes criados
    restaurantes = []

    '''
    Método Init -> Construtor
    Parâmetros :
    - Self -> Indicar o objeto que está sendo criado
    - Nome -> Indicar o nome do objeto
    - Categoria -> Indicar a categoria do objeto
    '''
    def __init__(self, nome, categoria):
        self._nome = nome.title() # .title() -> Transforma a string no formato com todas as primeiras letras sendo maiúsculla
        self._categoria = categoria.upper() # .upper() -> Transforma a string no formato com todas as letras em maiúscula
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        # Adicionar o objeto criado a lista (array) restaurantes
        Restaurante.restaurantes.append(self)

    '''
    Método Str -> Transforma em String
    Parâmetros:
    - Self -> Indicar o objeto que está chamando a função
    '''
    def __str__(self):
        return f'{self._nome} | {self._categoria} '
    
    '''
    Método de Classe lista_restaurantes()

    Output :
    - lista os restaurantes da lista(array) restaurantes no formato :
        Nome | Categoria | Ativo
    '''
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        '''
        Retorna uma string que representa o status do restaurante.
        Input :
        - self._ativo -> Status se o restaurante está ativado (true) ou desativado (false)
        Output :
        - return: Pode ser '✅' se o restaurante está ativo ou '❎' se o restaurante estive desativado.
        '''
        return '✅' if self._ativo else '❎'
    
    '''
    Método de Objeto - Alternar_estado()
    Alterna o estado _ativo entre ativado(true) e desativado(false)
    Input:
    - Valor do atributo _ativo do objeto que está sendo chamado
    Output:
    - Alterna o estado _ativo entre ativado(true) e desativado(false)
    '''
    def alternar_estado(self):
        self._ativo = not self._ativo

    '''
    Método Rebecer_avaliacao(self, cliente, nota)
    Recebe a avaliação para um restaurante
    Input :
    - Self (Objeto)
    - Cliente
    - Nota
    '''
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5 : 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        
    '''
    Método Media_avaliacoes(self)
    Calcular a média das notas do objeto que está sendo referenciado
    Input :
    - Self (Objeto)
    Output :
    - Média das Avaliações | Exemplo : 9.1
    '''
    @property
    def media_avaliacoes(self):
        if not self._avaliacao :
            return '-'
        # Soma de todas as notas da avaliação
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # Quantidade de notas 
        quantidade_de_notas = len(self._avaliacao)
        # Calculando a média e arrendondando para apenas uma casa decimal
        media = round(soma_das_notas/quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        # True : se for uma instância derivada da classe pai ItemCardapio ou derivadas(filhas): Prato, Bebida
        if isinstance (item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        '''
        Metódo de Propriedade - Exibir Cardápio
        Exibe o cardápio em formato de lista
        '''
        print(f'Cardápio do Restaurante: {self._nome}\n')
        # Percore a lista de acordo com a variavél contadora i e o item da lista cardapio, começando do 1
        for i, item in enumerate(self._cardapio, start=1):
            # Se o item possuir o atribuito 'descrição' a mensagem será referente a um prato
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${round(item._preco,2)} | Descrição: {item.descricao}'
                print(mensagem_prato)
            # Senão, a mensagem será referente a uma bebida
            else :
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${round(item._preco,2)} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            