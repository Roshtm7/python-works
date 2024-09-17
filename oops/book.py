class Book:
    title:str
    author:str
    price:int
    language:str

    # __init__ is used to initialise instance variable
    def __init__(self,title,author,price,language):
        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def display_book(self):
        print(self.title,self.author,self.price,self.language)

    # __str__ is used to string representation of that object
    def __str__(self):
        return self.author

book_instance = Book("pirates","henry",354,"english")
book_instance.display_book()
print(book_instance)
