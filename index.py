from models import Library
from views import Views
from connection import DataConnection

import json

response = Views.home()

while True:
    if response == 'Voltar':
        response = Views.home()

    if response == 'Sessão de clientes':
        response = Views.client()
    
    if response == 'Novo cliente':
        response = dict(Views.new_client())

        new_client = Library.Client(response)
        DataConnection.save(new_client.info(), 'client')


    if response == 'Sair':
        break