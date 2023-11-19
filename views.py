import os

def page_config(page_title: str = None):
    os.system('cls')

    if page_title is not None:
        print(f'{page_title}\n')


def page_choose(*args, title: str = None):
    page_config(page_title=title)

    for index, value in enumerate(list(args)):
        print(f'{index + 1} - {value}')

    response = int(input('\nResposta: ')) - 1

    return list(args)[response]

def page_questions(*args, title: str = None):
    page_config(page_title=title)

    responses = []
    for index, value in enumerate(list(args)):
        response = input(f'{index + 1} - {value}: ')
        
        if response is not None or response != '':
            responses.append(response)

    return response

class Views:
    def home():
        return page_choose('Sessão de clientes', 'Sessão de livros', 'Sair', title='Página inicial')

    def client():
        return page_choose('Novo cliente', 'Procurar cliente', 'Editar cliente', 'Excluir cliente', 'Voltar', title='Sessão de clientes')
    
    def new_client():
        return page_questions('pergunta 1', 'pergunta 2')