from datetime import datetime

class Library():
    # classe livro
    class Book():
        total = 0
        id = 0
        books = {}

        # criar, editar, excluir e achar livros
        def __init__(self, new: dict = None, find: dict = None):
            '''
            Construtor do livro

            new: aceita um dicionário com os seguintes valores = title: str, author: str, year: int, price: float. o title é obrigatório preencher. Ele cria e retorna uma instância do objeto.
            find: aceita um dicionario com os seguintes valores = title: str, author: str, year: list, price: list, id: int. Ele retorna as instancias que se enquadram nos requisitos (o year e price aceitam uma lista com os valores minimos e máximos [min, max]).
            '''

            if new is not None and new.get('title', None) is not None:
                self.title = new.get('title')
                self.author = new.get('author', 'No author')
                self.year = new.get('year', datetime.now().year)
                self.price = new.get('price', 0.0)

                self.edited = False
                self.id = Library.Book.id

                Library.Book.total += 1
                Library.Book.id += 1

                Library.Book.books[self.title] = self

                return self

            elif new is not None:
                raise Exception('Error when creating a new book, the book has a title?')


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
        id = 0

        def __init__(self, new: dict = None, find: dict = None):
            '''
            Construtor do cliente

            new: aceita um dicionário com os seguintes valores = name: str, cpf: str, phone: str (name e cpf são campos obrigatórios). Retorna a nova instância.
            find: aceita um dicionário com os seguintes valores = name: str, cpf: str, phone: str. Ele retorna os as instâncias que se encaixam dentro dos padrões do dicionário fornecido.
            '''

            if new is not None and all(getattr(new, attr) is not None for attr in ['name', 'cpf']):
                self.name = new.get('name')
                self.cpf = new.get('cpf')
                self.phone = new.get('phone', 'No phone')

                self.books = []
                self.edited = False

                self.id = Library.Client.id

                Library.Client.total += 1
                Library.Client.id += 1

            elif new is not None:
                raise Exception('Error when creating a new client, are you sure that name and cpf were filled in?')
            

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