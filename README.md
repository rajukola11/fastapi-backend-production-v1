# FastAPI Production Backend

A production-ready backend built with **FastAPI**, following clean architecture principles and best practices for authentication, authorization, database migrations, testing, and deployment readiness.

This project is designed as a **real-world backend reference**, not a tutorial demo.

---

## 🚀 Features

- JWT-based Authentication (Login & Register)
- Role-Based Access Control (RBAC)
  - Admin / Manager / Member
- Secure password hashing using Argon2
- PostgreSQL database with SQLAlchemy ORM
- Database migrations using Alembic
- Custom middleware (request timing)
- Background tasks for non-critical async work
- Automated testing with Pytest
- Environment-based configuration
- Docker-ready setup

---

## 🛠 Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.12
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Auth**: JWT (python-jose)
- **Security**: Passlib (Argon2)
- **Testing**: Pytest, HTTPX
- **Config**: Pydantic Settings
- **Server**: Uvicorn
- **Containerization**: Docker

---


### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate


🗄 Database & Migrations
Initialize database

Make sure PostgreSQL is running and database exists.

Run migrations
alembic upgrade head

Create a new migration
alembic revision --autogenerate -m "migration message"

▶️ Run the Application
Development
uvicorn main:app --reload

Production (basic)
uvicorn main:app --host 0.0.0.0 --port 8000


API will be available at:

http://127.0.0.1:8000


Swagger Docs:

http://127.0.0.1:8000/docs



🧪 Running Tests
pytest


Tests include:

Authentication flow

JWT token validation

Role-based access control

Protected routes
