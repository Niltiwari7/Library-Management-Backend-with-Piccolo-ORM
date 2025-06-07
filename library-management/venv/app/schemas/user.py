from enum import Enum
from piccolo.columns import (
    UUID,
    Boolean,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    Text,
    Timestamp,
    Varchar,
)

from piccolo.columns.readable import Readable
from piccolo.table import Table
from datetime import datetime

class User(Table):
    username = Varchar(length = 100, unique=True)
    email = Varchar(length=255 , unique=True)
    password = Varchar(length = 255)
    is_active = Boolean(default=True)
    is_admin = Boolean(default=False)
    created_at = Timestamp(default=datetime.now)

    @classmethod
    def get_readable(cls)->Readable:
        return Readable(template='%s', columns=[cls.username])