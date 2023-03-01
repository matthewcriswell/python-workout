''' book and shelf classes '''


class BookshelfOutOfCapacity(Exception):
    pass


class Book():
    ''' defines a book object '''

    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf():
    ''' defines a shelf object as a collections of books '''

    def __init__(self, width=70):
        self.contents = []
        self.width = width
        self.capacity = width

    def add_book(self, *books):
        ''' add book(s) to contents '''
        for book in books:
            if self.capacity - book.width < 0:
                raise BookshelfOutOfCapacity(
                    f'Not enough space on shelf to add {book.title}')
            self.contents.append(book)
            self.capacity -= book.width

    def total_price(self):
        ''' print the total price of the bookshelf books '''
        print(round(sum(book.price for book in self.contents), 2))

    def has_book(self, title):
        ''' looks to see if the shelf has a specific book title '''
        return title in [book.title for book in self.contents]

    def __repr__(self):
        return '\n'.join(book.title for book in self.contents)


b1 = Book('burps', 'matt criswell', 9.99, 2)
b2 = Book('fart', 'josh criswell', 19.99, 3)
b3 = Book('butt', 'seth thompson', 8.95, 10)
s = Shelf()
s.add_book(b1, b2, b3, b1)
