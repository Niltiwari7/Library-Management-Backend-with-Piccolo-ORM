from piccolo.table import Table
from piccolo.columns import (
    Varchar,
    Text,
    Date,
    Boolean
)
from piccolo.columns.readable import Readable
from datetime import datetime
class Member(Table):
    first_name = Varchar(length = 100)
    last_name = Varchar(length=100)
    email = Varchar(length=255,unique=True)
    phone = Varchar(length = 10)
    address = Text()    
    membership_date = Date(default = datetime.now)
    is_active = Boolean(default = True)

    @classmethod
    def get_readable(cls)->Readable:
        return Readable(template="%s %s", columns=[cls.first_name,cls.last_name])