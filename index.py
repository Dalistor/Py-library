from engine.models import Library
from engine.views import Views
from engine.connection import DataConnection

# Carregar informações já salvas
DataConnection.remember()

# Iniciar programa
response = Views.home()

# Controle de ações do programa
while True:
    if response == 'Voltar':
        response = Views.home()

    # Clientes

    if response == 'Sessão de clientes':
        response = Views.client()
    
    if response == 'Novo cliente':
        response = dict(Views.new_client())

        new_client = Library.Client(response)
        DataConnection.save(new_client.info(), 'client')

        response = Views.client()

    if response == 'Procurar cliente':
        key, value = Views.find_client_method()

        result = DataConnection.find('client', key, value)
        Views.find_client(result)

        response = Views.client()

    if response == 'Emprestar livro':
        lended_book = Views.lend_book()
        DataConnection.update(insert=lended_book, local='client')

        response = Views.client()

    if response == 'Retirar livro':
        unlended_book = Views.unlend_book()
        DataConnection.update(delete=unlended_book, local='client')

        response = Views.client()

    if response == 'Editar cliente':
        edit_values = Views.client_edit()
        DataConnection.edit(edit_values, 'client')

        response = Views.client()

    if response == 'Excluir cliente':
        client = Views.client_remove()
        DataConnection.remove(client, 'client')

        response = Views.client()

    # Clientes

    # Livros

    if response == 'Sessão de livros':
        response = Views.book()

    if response == 'Novo livro':
        response = dict(Views.new_book())

        new_book = Library.Book(response)
        DataConnection.save(new_book.info(), 'book')

        response = Views.book()

    if response == 'Procurar livro':
        key, value = Views.find_book_method()

        result = DataConnection.find('book', key, value)
        Views.find_book(result)

        response = Views.book()

    if response == 'Editar livro':
        edit_values = Views.book_edit()
        DataConnection.edit(edit_values, 'book')

        response = Views.book()

    if response == 'Excluir livro':
        book = Views.book_remove()
        DataConnection.remove(book, 'book')

        response = Views.book()

    # Livros

    if response == 'Sair':
        break