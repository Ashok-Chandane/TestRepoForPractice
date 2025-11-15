'''
Exercise 1:
Print the book’s title.

Add a new key "genre" with value "Fantasy".

Change the "year" to 1951.

Print the updated dictionary.
'''

book = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
}

print(f"Title of Book is {book.get('title')} ")
book.update(genre="Fantasy")
book.update(year=1951)
print(book)
