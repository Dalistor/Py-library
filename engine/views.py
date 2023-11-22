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

class Views:
    def home():
        return page_choose('Sessão de clientes', 'Sessão de livros', 'Sair', title='Página inicial')

    def client():
        return page_choose('Novo cliente', 'Procurar cliente', 'Editar cliente', 'Excluir cliente', 'Voltar', title='Sessão de clientes')
    
    def new_client():
        return page_questions(('Nome', 'name', True), ('CPF', 'cpf', True), ('Telefone', 'phone', False))