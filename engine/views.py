import os

def page_config(page_title: str = None):
    os.system('cls')

    if page_title is not None:
        print(f'{page_title}\n')


def page_choose(*args, title: str = None):
    page_config(page_title=title)

    responses = list(args)

    for index, value in enumerate(responses):
        print(f'{index + 1} - {value}')

    response = int(input('\nResposta: ')) - 1

    return responses[response]

def page_choose_with_codevalue(*args, title: str = None):
    page_config(page_title=title)

    code_responses = [val for _, val in list(args)]
    responses = [val for val, _ in list(args)]

    for index, value in enumerate(responses):
        print(f'{index + 1} - {value}')

    response = int(input('\nResposta: ')) - 1

    return code_responses[response]

def page_questions(*args, title: str = None):
    page_config(page_title=title)

    responses = []
    for value, code_value, required in list(args):
        response = input(f'{value}: ')
        
        while True:
            if response:
                responses.append((code_value, response))
                break

            elif required:
                response = input(f'Esse campo é obrigatório, insira o(a) {str(value).lower()}: ')

            else:
                break

    return responses

def print_results(results: dict, title: str = None):
    page_config(page_title=title)

    for dict in results:
        for index, (key, value) in enumerate(dict.items()):
            if key == 'name':
                key = 'Nome'
            elif key == 'cpf':
                key = 'CPF'
            elif key == 'phone':
                key = 'Telefone'
            elif key == 'title':
                key = 'Título'
            elif key == 'author':
                key = 'Autor'
            elif key == 'Year':
                key = 'Ano'
            elif key == 'price':
                key = 'Preço'

            print(f'{index + 1} - {key}: {value}')
        
        print('#############')

    input('\nPrecione enter para voltar')

class Views:
    def home():
        return page_choose('Sessão de clientes', 'Sessão de livros', 'Sair', title='Página inicial')

    def client():
        return page_choose('Novo cliente', 'Procurar cliente', 'Editar cliente', 'Excluir cliente', 'Voltar', title='Sessão de clientes')
    
    def new_client():
        return page_questions(('Nome', 'name', True), ('CPF', 'cpf', True), ('Telefone', 'phone', False))
    
    def find_client_method():
        field = page_choose_with_codevalue(('Nome', 'name'), ('CPF', 'cpf'), ('Telefone', 'phone') , title='Escolha o método de pesquisa')
        value = input('\nInsira o valor: ')

        return field, value
    
    def find_client(results: dict):
        return print_results(results)
    
    def client_edit():
        field = page_questions(('ID', 'id', True), ('Nome', 'name', False), ('CPF', 'cpf', False), ('Telefone', 'phone', False), title='Preencha os campos para editar o valor (pegue o ID do cliente na sessão de procurar clientes)')

        return field
    
    def client_remove():
        page_config(page_title='Insira o id do cliente que deseja deletar')
        
        return int(input('ID: '))
