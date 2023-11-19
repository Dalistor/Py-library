from models import Library
from views import Views

response = Views.home()

while True:
    if response == 'Voltar':
        response = Views.home()

    if response == 'Sessão de clientes':
        response = Views.client()
    
    if response == 'Novo cliente':
        response = Views.new_client()
        
    if response == 'Sair':
        break