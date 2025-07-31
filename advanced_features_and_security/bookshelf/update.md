# Update the Book instance

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

# Output:
# Updated book title saved successfully.
