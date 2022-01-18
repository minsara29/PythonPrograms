from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlAlchemy_schema import Author, Book, BookAuthor
from marshmallow_sqlalchemy.fields import Nested

class AuthorSchema(SQLAlchemySchema):
    class Meta:
        model = Author
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    name = auto_field()
    books = auto_field()


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True

    id = auto_field()
    title = auto_field()
    author_id = auto_field()

class BookAuthorSchema(SQLAlchemySchema):
    class Meta:
        model = BookAuthor
        load_instance = True  # Optional: deserialize to model instances

    author = Nested(AuthorSchema, many=True)

    id = auto_field()
    name = auto_field()
    author = auto_field()