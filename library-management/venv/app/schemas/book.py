from datetime import datetime
from piccolo.columns import (
    Date,
    Integer,
    Text,
    Timestamp,
    Varchar
)
from piccolo.columns.readable import Readable
from piccolo.table import Table

class Book(Table):
    title = Varchar(length=255)
    author = Varchar(length=255)
    isbn = Varchar(length = 13, unique=True)
    published_date = Date()
    genre = Varchar(length = 100)
    description = Text()
    total_copies = Integer(default=1)
    available_copise = Integer(default=1)
    cover_image_url = Varchar(length = 255, null = True)
    created_at = Timestamp(default=datetime.now)

    @classmethod
    def get_readable(cls)->Readable:
        return Readable(template = '%s by %s', columns=[cls.title, cls.author])