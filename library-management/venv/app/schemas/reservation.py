from piccolo.table import Table
from piccolo.columns import (
    Varchar,
    ForeignKey,
    Timestamp
)
from datetime import datetime
from schemas.book import Book
from schemas.member import Member
from piccolo.columns.readable import Readable
class Reservation(Table):
    book = ForeignKey(Book)
    member = ForeignKey(Member)
    reservation_date = Timestamp(default = datetime.now)
    expiry_date = Timestamp()
    status = Varchar(length = 20, choices=["pending","fullfilled","cancelled"],default="pending")

    @classmethod
    def get_readable(cls)-> Readable:
        return Readable(
            template = "%s reserved by %s",
            columns=[cls.book.title,cls.member.first_name]
        )
    
