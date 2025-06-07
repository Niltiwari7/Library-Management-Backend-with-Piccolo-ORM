from piccolo.table import Table
from schemas.loan import BookLoan
from piccolo.columns import (
    ForeignKey,
    Numeric,
    Timestamp,
    Boolean
)
from datetime import datetime
from piccolo.columns.readable import Readable
class Fine(Table):
    loan = ForeignKey(BookLoan)
    amount = Numeric(digits = (5,2))
    issued_date = Timestamp(default=datetime.now)
    paid_date = Timestamp(null = True)
    is_paid = Boolean(default = False)
    

    @classmethod
    def get_readable(cls)->Readable:
        return Readable(
            template = "Fine of %s",
            columns = [cls.amount]
        )