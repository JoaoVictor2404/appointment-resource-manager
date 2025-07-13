# Appointment and Resource Management System

A **robust**, **secure**, and **scalable** REST API built with FastAPI for scheduling appointments and managing resources—perfect for tech companies, clinics or hospitals.

---

## 🚀 Features

* ✅ **JWT Authentication** & user registration
* 🔒 **Role-based data isolation**: users only see their own appointments
* 🗓️ **CRUD** for Resources (rooms, equipment, etc.) and Appointments
* 📧 **Email reminders** via background tasks
* ⚙️ **Pagination** & filtering on list endpoints
* 🐳 **Docker** support for containerized deployment
* ✅ **Automated tests** with pytest
* 🔄 **CI/CD** pipeline with GitHub Actions

---

## 📂 Project Structure

```
appointment-resource-manager/
├── README.md
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/ci.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── auth.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── notifications.py
│   └── routers/
│       ├── users.py
│       ├── resources.py
│       └── appointments.py
└── tests/
    ├── conftest.py
    ├── test_auth.py
    ├── test_crud.py
    └── test_appointments.py
```

---

## 🛠️ Tech Stack

* **FastAPI** – high-performance Python web framework
* **SQLAlchemy** + **SQLite** – ORM and file-based database (easy to swap for Postgres/MySQL)
* **Pydantic** – data validation
* **python-jose** & **PassLib** – JWT + password hashing
* **FastAPI-Mail** – email notifications
* **Docker** – containerization
* **GitHub Actions** – CI: install, lint, test

---

## 🔧 Prerequisites

* Python 3.11+
* Docker & Docker Compose (optional, for container mode)

---

## ⚙️ Installation & Local Development

1. **Clone the repo**

   ```bash
   git clone https://github.com/JoaoVictor2404/appointment-resource-manager.git
   cd appointment-resource-manager
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

4. **Run the server**

   ```bash
   uvicorn app.main:app --reload
   ```

   * The API will be available at: `http://127.0.0.1:8000`
   * Interactive docs: `http://127.0.0.1:8000/docs`

---

## 🐳 Docker

Build and run in a container:

```bash
docker build -t appointment-manager .
docker run -d -p 8000:80 appointment-manager
```

---

## 🧪 Testing

Run the full test suite with pytest:

```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## 📑 API Overview

All endpoints (except `/users/` and `/token`) require an **Authorization: Bearer <token>** header.

### Authentication

* **POST** `/users/`
  Register a new user

  ```json
  { "email": "user@example.com", "password": "secret" }
  ```

* **POST** `/token`
  Login and receive JWT

  * form-data:

    * `username`: user’s email
    * `password`: user’s password
  * Response:

    ```json
    { "access_token": "<jwt>", "token_type": "bearer" }
    ```

### Resources

* **POST** `/resources/`
  Create a new resource

  ```json
  { "name": "Room A", "type": "Room" }
  ```

* **GET** `/resources/?skip=0&limit=10`
  List resources (paginated)

### Appointments

* **POST** `/appointments/`
  Create a new appointment (sends reminder email)

  ```json
  {
    "title": "Team Meeting",
    "start": "2025-08-01T10:00:00",
    "end":   "2025-08-01T11:00:00",
    "resource_id": 1
  }
  ```

* **GET** `/appointments/?skip=0&limit=10`
  List your appointments (paginated)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes & push
4. Open a Pull Request

Please follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) and add tests for new functionality.

---

## 📄 License

This project is released under the **MIT License**.
Feel free to use, adapt and extend!
