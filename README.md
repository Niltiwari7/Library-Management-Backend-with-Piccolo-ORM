# Library-Management-Backend-with-Piccolo-ORM

```
library-management/
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── run.py                  # Application entry point
│
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py             # FastAPI app instance and routes
│   │
│   ├── core/               # Core application components
│   │   ├── __init__.py
│   │   ├── config.py       # Application configuration
│   │   ├── security.py     # Security utilities
│   │   └── exceptions.py   # Custom exceptions
│   │
│   ├── db/                 # Database related files
│   │   ├── __init__.py
│   │   ├── models.py       # Database models (Piccolo tables)
│   │   ├── migrations/     # Piccolo migrations
│   │   └── session.py      # Database session handling
│   │
│   ├── api/                # API endpoints organized by domain
│   │   ├── __init__.py
│   │   ├── base.py         # Base router with common dependencies
│   │   ├── users.py        # User management endpoints
│   │   ├── books.py        # Book management endpoints
│   │   ├── members.py      # Member management endpoints
│   │   ├── loans.py        # Loan management endpoints
│   │   ├── fines.py        # Fine management endpoints
│   │   └── reservations.py # Reservation management endpoints
│   │
│   ├── schemas/            # Pydantic models/schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── book.py
│   │   ├── member.py
│   │   ├── loan.py
│   │   ├── fine.py
│   │   └── reservation.py
│   │
│   ├── services/           # Business logic layer
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── book_service.py
│   │   ├── member_service.py
│   │   ├── loan_service.py
│   │   ├── fine_service.py
│   │   └── reservation_service.py
│   │
│   └── utils/              # Utility functions
│       ├── __init__.py
│       ├── pagination.py
│       ├── logging.py
│       └── helpers.py
│
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Pytest fixtures
│   ├── test_models.py
│   ├── test_users.py
│   ├── test_books.py
│   ├── test_members.py
│   ├── test_loans.py
│   └── test_reservations.py
│
└── scripts/                # Utility scripts
    ├── __init__.py
    ├── create_admin.py     # Script to create admin user
    └── db_seed.py         # Database seeding script
```