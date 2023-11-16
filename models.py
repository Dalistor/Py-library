from datetime import datetime

# classe livro
class Book():
    total = 0
    id = 0

    def __init__(self, title: str = None, author: str = None, year: int = None, price: float = None, obj: dict = None):
        if obj is not None and obj.get(title, None) is not None:
            title = obj.get(title)
            author = obj.get(author, 'No author')
            year = obj.get(year, datetime.now().year)
            price = obj.get(price, 0.0)

        elif title is not None:
            self.title = title
            self.author = author if author is not None else 'No author'
            self.year = year if year is not None else datetime.now().year
            self.price = price if price is not None else 0.0

        else:
            raise Exception('Error when creating a new book, the book has a title?')

        self.edited = False

        self.id = Book.id

        Book.total += 1
        Book.id += 1

    def edit(self, title: str = None, author: str = None, year: int = None, price: float = None, obj: dict = None):
        if obj is not None:
            title = obj.get(title, self.title)
            author = obj.get(author, self.author)
            year = obj.get(year, self.year)
            price = obj.get(price, self.price)

        self.title = title if title is not None else self.title
        self.author = author if author is not None else self.author
        self.year = year if year is not None else self.year
        self.price = price if price is not None else self.price

        self.edited = True

    def __del__(self):
        Book.total -= 1


# Book to Client: 1 - n
class Client():
    total = 0
    id = 0

    def __init__(self, name: str = None, cpf: str = None, phone: str = None, obj: dict = None):
        if obj is not None and all(getattr(obj, attr) is not None for attr in ['name', 'cpf']):
            self.name = obj.get(name)
            self.cpf = obj.get(cpf)
            self.phone = obj.get(phone, 'No phone')

        elif (all(param is not None for param in [name, cpf])):
            self.name = name
            self.cpf = cpf
            self.phone = phone if phone is not None else 'No phone'

        else:
            raise Exception('Error when creating a new client, are you sure that name and cpf were filled in?')
        
        self.books = []
        self.edited = False

        self.id = Client.id

        Client.total += 1
        Client.id += 1

    def edit(self, name: str = None, cpf: str = None, phone: str = None, obj: dict = None):
        if obj is not None:
            name = obj.get(name, self.name)
            cpf = obj.get(cpf, self.cpf)
            phone = obj.get(phone, self.phone)
        
        self.name = name if name is not None else self.name
        self.cpf = cpf if cpf is not None else self.cpf
        self.phone = phone if phone is not None else self.phone

        self.edited = True

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def __del__(self):
        Client.total -= 1

# classe cliente
class Library():
    pass
