
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Expected Output:
plaintext
(1, {'bookshelf.Book': 1})


The book instance has been successfully deleted.
