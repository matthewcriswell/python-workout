''' book and shelf classes '''


class Book():
    ''' defines a book object '''

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class Shelf():
    ''' defines a shelf object as a collections of books '''

    def __init__(self):
        self.contents = []

    def add_book(self, *books):
        ''' add book(s) to contents '''
        for book in books:
            self.contents.append(book)

    def total_price(self):
        ''' print the total price of the bookshelf books '''
        print(round(sum(book.price for book in self.contents), 2))

    def has_book(self, title):
        ''' looks to see if the shelf has a specific book title '''
        return title in [book.title for book in self.contents]

    def __repr__(self):
        return '\n'.join(book.title for book in self.contents)


b1 = Book('burps', 'matt criswell', 9.99)
b2 = Book('fart', 'josh criswell', 19.99)
b3 = Book('butt', 'seth thompson', 8.95)
s = Shelf()
s.add_book(b1, b2, b3, b1)
