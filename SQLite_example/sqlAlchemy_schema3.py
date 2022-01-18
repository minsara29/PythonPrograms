from sqlAlchemy_schema import Author, Book, session, BookAuthor
from sqlAlchemy_schema2 import AuthorSchema


author = Author(name="Kannan")
author_schema = AuthorSchema()
book_author_schema = BookAuthor(author=author)
book = Book(title="Fight Club2", author=author)
session.add(author)
session.add(book)
session.add(book_author_schema)
session.commit()

dump_data = author_schema.dump(author)
print(dump_data)
# {'id': 1, 'name': 'Chuck Paluhniuk', 'books': [1]}

load_data = author_schema.load(dump_data, session=session)
print(load_data)
# <Author(name='Chuck Paluhniuk')>

# dump_data = author_schema.dump(author)