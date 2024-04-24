import os;

# Dicionário para armazenar os restaurantes
restaurantes = [{'nome':'Toku', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Achapa', 'categoria':'Breakfast', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}];

def limpar_tela():
    '''
        Função para limpar o terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear');

def exibir_nome_do_programa():
    '''
        Função para Exibir o nome do programa
    '''
    print ("""

╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
       """);

def exibir_opcoes():
    '''
        Função para exibir as opções que o programa oferece
    '''
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Alterar estado dos restaurantes')
    print('4. Sair\n');

def finalizar_app():
    '''
        Função para limpar o terminal e encerrar o programa
    '''
    limpar_tela();
    print('Encerrando...');

def voltar_tela_principal():
    '''
        Função para retornar a tela principal (inicial) do programa
    '''
    input('Pressione enter para voltar ao menu principal...');
    main();

def opcao_invalida():
    '''
        Função para exibir ao usuário que a opção escolhida está inválida
    '''
    print('Opção inválida!\n');
    voltar_tela_principal();

def cadastrar_restaurante():
    '''
        Função para cadastrar um novo restaurante

        Inputs:
        - Nome do Restaurante
        - Categoria

        Outputs:
        - Adiciona ao dicionário (restaurantes) um novo restaurante com os seguintes dados : nome e categoria
    '''
    limpar_tela();
    print('Cadastro de restaurantes\n');
    nome_do_restaurante = input('Digite o nome do restaurante: ');
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ');

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False};
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n');
    voltar_tela_principal();

def listar_restaurantes():
    '''
        Função para listar os restaurantes disponíveis no dicionário (restaurantes)
    '''
    limpar_tela();
    print('Lista de restaurantes\n');
    if len(restaurantes) > 0:
        print(f"{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status")
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome'];
            categoria = restaurante['categoria'];
            status = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status} ');
    else:
        print('Nenhum restaurante cadastrado.');
    print('');
    voltar_tela_principal();

def alternar_estado_restaurante():
    '''
        Função para alternar o estado do restaurante entre desativado e ativado

        Inputs:
        - Nome do Restaurante

        Outputs:
        - Alterar o estado do restaurante entre desativado ou ativado
    '''
    print('Alterando estado do restaurante\n');

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_tela_principal();

def escolher_opcao():
    '''
        Função para escolher uma opção das disponíveis no programa

        Input:
        - Opção que foi escolhida

        Output:
        - O usuário é direcionado para a opção que foi escolhida
    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '));

        if opcao_escolhida == 1:
            cadastrar_restaurante();
        elif opcao_escolhida == 2:
            listar_restaurantes();
        elif opcao_escolhida == 3:
            alternar_estado_restaurante();
        elif opcao_escolhida == 4:
            finalizar_app();
        else:
            opcao_invalida();
    except: 
        opcao_invalida();



def main():
    '''
        Função para definir o estado principal do programa
    '''

    limpar_tela();
    exibir_nome_do_programa();
    exibir_opcoes();
    escolher_opcao();

if __name__ == "__main__":
    main();