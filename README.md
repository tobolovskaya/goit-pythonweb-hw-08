# Contacts API

## Overview
The **Contacts API** is a RESTful web application built using **FastAPI** and **SQLAlchemy**, designed to manage contact information. This API supports CRUD operations for storing and retrieving contact data, along with advanced features such as searching and filtering by name, surname, or email and fetching contacts with upcoming birthdays.

---

## Features

- **CRUD Operations:** Create, Read, Update, and Delete contact entries.
- **Search Contacts:** Query contacts by name, surname, or email.
- **Upcoming Birthdays:** Retrieve a list of contacts with birthdays in the next 7 days.
- **PostgreSQL Integration:** Seamless interaction with a PostgreSQL database using SQLAlchemy ORM.
- **Swagger UI:** Automatically generated interactive API documentation.
- **Validation:** Input data is validated using Pydantic models.

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/contacts-api.git
   cd contacts-api
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database:**
   - Start a PostgreSQL instance (use Docker or a local installation).
   - Create a database:
     ```sql
     CREATE DATABASE contacts_db;
     ```
   - Update the connection string in `src/conf/config.py` with your database credentials.

5. **Apply Database Migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Run the Application:**
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

---

## Project Structure

```
├── src
│   ├── api
│   │   ├── contacts.py       # API routes for contacts
│   │   ├── tags.py           # API routes for tags (future feature)
│   ├── services
│   │   ├── contacts.py       # Business logic for contacts
│   │   ├── tags.py           # Business logic for tags
│   ├── repository
│   │   ├── contacts.py       # Database queries for contacts
│   │   ├── tags.py           # Database queries for tags
│   ├── database
│   │   ├── models.py         # SQLAlchemy models
│   │   ├── db.py             # Database session setup
│   ├── conf
│   │   ├── config.py         # Configuration settings
│   └── schemas.py            # Pydantic models
├── pyproject.toml             # Project dependencies and settings
├── alembic/                   # Database migration files
├── main.py                    # Entry point for FastAPI application
└── README.md                  # Project documentation
```

---

## API Endpoints

### Contacts

| Method | Endpoint                   | Description                          |
|--------|----------------------------|--------------------------------------|
| GET    | `/api/contacts/`           | Get a list of all contacts           |
| GET    | `/api/contacts/{id}`       | Get a specific contact by ID         |
| POST   | `/api/contacts/`           | Create a new contact                 |
| PUT    | `/api/contacts/{id}`       | Update an existing contact           |
| DELETE | `/api/contacts/{id}`       | Delete a contact                     |
| GET    | `/api/contacts/search`     | Search for contacts by name/email    |
| GET    | `/api/contacts/birthdays`  | Get contacts with upcoming birthdays |

---

## Configuration

The application configuration is managed using Pydantic. Update the `src/conf/config.py` file with your PostgreSQL credentials and other settings:

```python
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://user:password@localhost/contacts_db"
    class Config:
        env_file = ".env"
```

---

## Testing

Run tests using **pytest**:

```bash
pytest
```

---


