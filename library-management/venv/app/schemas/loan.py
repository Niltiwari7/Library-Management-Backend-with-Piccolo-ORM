from enum import Enum
from piccolo.table import Table
from piccolo.columns import (
    Varchar,
    ForeignKey,
    Date,
    Numeric,
    
)
from schemas.book import Book
from schemas.member import Member
from datetime import datetime
from piccolo.columns.readable import Readable
class LoanStatus(str,Enum):
    BORROWED = "borrowed"
    RETURNED = "returned"
    OVERDUE = "overdue"
    LOST = "lost"

class BookLoan(Table):
    book = ForeignKey(Book)
    member = ForeignKey(Member)
    loan_date = Date(default = datetime.now)
    due_date = Date()
    return_date = Date(null=True)
    status = Varchar(length = 20, choices=LoanStatus,default=LoanStatus.BORROWED)
    fine_amount = Numeric(digits=(5, 2), default=0)

    @classmethod
    def get_readable(cls)-> Readable:
        return Readable(
            template="%s borrowed by %s",
            columns=[cls.book.title,
                     cls.member.first_name]
        )
