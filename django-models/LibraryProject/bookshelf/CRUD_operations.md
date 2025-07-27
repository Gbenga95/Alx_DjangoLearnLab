# Create a Book instance

from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Output:
# <Book: 1984> (after adding __str__ method in the model)

# Retrieve the Book instance

book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)

# Output:
# 1984 George Orwell 1949

# Update the Book instance

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Output:
# Updated book title saved successfully.

# Delete the Book instance

book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
Book.objects.all()

# Output:
# <QuerySet []>  (No books found)
