# Artikate Backend Assessment

## Overview
This project is a Django REST Framework backend developed as part of the Artikate Backend Assessment.

The project demonstrates:
- Query optimization using Django ORM
- Asynchronous background jobs using Celery + Redis
- Multi-tenant data isolation
- REST APIs
- Unit tests
- Docker support

---

## Technology Stack
- Python 3.14
- Django 5.x
- Django REST Framework
- Celery
- Redis
- SQLite
- Docker
- drf-yasg (Swagger)

---

## Project Structure
```
artikate_assessment/
│
├── artikate/
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── ...
│
├── jobs/
├── orders/
├── tenants/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd artikate_assessment
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

## Database

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

Server

```
http://127.0.0.1:8000
```

---

## Docker

Start Redis

```bash
docker compose up
```

---

## Run Celery

```bash
celery -A artikate worker -l info
```

---

## Run Tests

All tests

```bash
python manage.py test
```

Specific test

```bash
python manage.py test tests.test_section1
```

---

## Swagger

```
http://127.0.0.1:8000/swagger/
```

---

## API Endpoints

### Orders

GET

```
/api/orders/summary/
```

### Jobs

POST

```
/api/jobs/send-email/
```

### Tenants

GET

```
/api/tenants/current/
```

---

## Features

✔ ORM Optimization

✔ Celery Background Tasks

✔ Redis Queue

✔ Retry Mechanism

✔ Multi Tenant Isolation

✔ Docker Support

✔ Unit Testing

✔ Swagger Documentation
