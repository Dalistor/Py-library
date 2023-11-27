from datetime import datetime

class Library():
    
    # classe livro
    class Book():
        total = 0
        books = {}

        _id = 0

        # criar, editar, excluir e achar livros
        def __init__(self, new: dict = None):
            '''
            Construtor do livro

            new: aceita um dicionário com os seguintes valores = title: str, author: str, year: int, price: float. o title é obrigatório preencher. Ele cria e retorna uma instância do objeto.
            '''

            if new is not None and new.get('title', None) is not None:
                self.title = new.get('title')
                self.author = new.get('author', 'No author')
                self.year = new.get('year', datetime.now().year)
                self.price = new.get('price', 0.0)

                self.edited = False
                self.id = Library.Book._id

                Library.Book.total += 1
                Library.Book._id += 1

                Library.Book.books[self.title] = self

            elif new is not None:
                raise Exception('Error when creating a new book, the book has a title?')
            
        def info(self):
            '''
            Retorna dados da instância
            '''

            values = {
                'title': self.title,
                'author': self.author,
                'year': self.year,
                'price': self.price,
                'id': self.id
            }

            return values
        
        def id_exist(id: int):
            keys = [filter(lambda key: id in key[1], Library.Book.books.items())]

            return True if len(keys) > 0 else False

        def find(values: dict = None):
            '''
            retorna intâncias de livros de acordo com o dicionário fornecido.

            values: aceita um dicionario com os seguintes valores = title: str, author: str, year: list, price: list, id: int. Ele retorna as instancias que se enquadram nos requisitos (o year e price aceitam uma lista com os valores minimos e máximos [min, max]).
            '''
            results = []
            if values is not None:
                for key in values:
                    if (key, values[key]) in Library.Book.books.items():
                        results.append(values[key])

            return results


        def edit(self, values: dict = None):
            '''
            Editor de livros

            values: aceita um dicionário com os seguintes valores = title: str, author: str, year: int, price: float. Ele irá substituir os valores originais pelo do dicionario fornecido.
            '''

            if values is not None:
                self.title = values.get('title', self.title)
                self.author = values.get('author', self.author)
                self.year = values.get('year', self.year)
                self.price = values.get('price', self.price)

                self.edited = True

        def __del__(self):
            Library.Book.total -= 1


    # Book to Client: 1 - n
    class Client():
        total = 0
        clients = {}

        _id = 0

        def __init__(self, new: dict = None):
            '''
            Construtor do cliente

            new: aceita um dicionário com os seguintes valores = name: str, cpf: str, phone: str (name e cpf são campos obrigatórios). Retorna a nova instância.
            '''

            if new is not None and all(new.get(attr) is not None for attr in ['name', 'cpf']):
                self.name = new.get('name')
                self.cpf = new.get('cpf')
                self.phone = new.get('phone', 'No phone')

                self.books = []
                self.edited = False

                self.id = Library.Client._id

                Library.Client.total += 1
                Library.Client._id += 1

                Library.Client.clients[self.name] = self

            elif new is not None:
                raise Exception('Error when creating a new client, are you sure that name and cpf were filled in?')
            
        def info(self):
            '''
            Retorna dados da instância
            '''

            values = {
                'name': self.name,
                'cpf': self.cpf,
                'phone': self.phone,
                'borrowed_book': self.books,
                'id': self.id
            }

            return values
        
        def id_exist(id: int):
            keys = [filter(lambda key: id in key[1], Library.Client.clients.items())]

            return True if len(keys) > 0 else False

        def find(values: dict = None):
            '''
            Retorna instâncias de clientes de acordo com o dicionário fornecido.

            values: aceita um dicionário com os seguintes valores = name: str, cpf: str, phone: str
            '''

            results = []
            if values is not None:
                for key in values:
                    if (key, values[key]) in Library.Client.clients.items():
                        results.append(values[key])

            return results

        def edit(self,  value: dict = None):
            '''
            Editor de clientes

            value: aceita um dicionário com os valores = name: str, cpf: str, phone: str. Ele retorna as instâncias que se encaixam dentro dos padrões do dicionário fornecido.
            '''

            if value is not None:
                name = value.get(name, self.name)
                cpf = value.get(cpf, self.cpf)
                phone = value.get(phone, self.phone)
            
            self.name = name if name is not None else self.name
            self.cpf = cpf if cpf is not None else self.cpf
            self.phone = phone if phone is not None else self.phone

            self.edited = True

        def add_book(self, book: 'Library.Book'):
            '''
            Associa um livro no cliente.

            book: aceita uma instancia do Book.
            '''

            self.books.append(book)

        def remove_book(self, book: 'Library.Book'):
            '''
            Desassocia um livro no cliente.

            book: aceita uma instancia do Book.
            '''

            self.books.remove(book)

        def __del__(self):
            Library.Client.total -= 1