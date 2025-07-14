# Delete the Book instance

book = Book.objects.get(id=1)
book.delete()

# Confirm deletion
Book.objects.all()

# Output:
# <QuerySet []>  (No books found)
