
from mongoengine import Document, StringField, ListField, ReferenceField

# Model for the "authors" collection
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# Model for the "quotes" collection
class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)
