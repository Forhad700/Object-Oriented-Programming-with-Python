class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year


author_instance = Author("J.K. Rowling", "British")
book_instance = Book("Harry Potter and the Sorcerer's Stone", author_instance, 1997)

print("Author Name: ", author_instance.name)
print("Nationality: ", author_instance.nationality)
print("Book Title: ", book_instance.title)
print("Publication Year: ", book_instance.publication_year)