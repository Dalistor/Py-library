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

    if response == 'Sessão de clientes':
        response = Views.client()
    
    if response == 'Novo cliente':
        response = dict(Views.new_client())

        new_client = Library.Client(response)
        DataConnection.save(new_client.info(), 'client')

        response = Views.client()

    if response == 'Procurar cliente':
        key, value = Views.find_client_method()

        result = DataConnection.find_entity('client', key, value)
        Views.find_client(result)

        response = Views.client()

    if response == 'Sair':
        break