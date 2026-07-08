# Design Document

## Architecture
The application follows a modular Django architecture.

```
                Client
                   │
        Django REST Framework
                   │
     ┌─────────────┼─────────────┐
     │             │             │
 Orders App     Jobs App     Tenants App
     │             │             │
     └─────────────┼─────────────┘
                   │
               SQLite Database
                   │
                Celery Worker
                   │
                 Redis Queue
```

---

## Orders Module

Responsible for:
- Order management
- Query optimization
- ORM improvements

Optimization techniques
- select_related()
- prefetch_related()
- aggregate()

---

## Jobs Module

Responsible for
- Sending emails
- Background processing
- Retry mechanism

Flow

```
Client
   │
POST /send-email
   │
Celery Queue
   │
Redis
   │
Celery Worker
   │
Send Email
```

---

## Tenant Module
Responsible for

- Tenant identification
- Tenant isolation
- Middleware
- Context storage

Each request stores current tenant.

Queries automatically filter by tenant.

---

## Database

SQLite was used for development.

Models

Tenant

```
id
name
```

Customer

```
id
name
tenant
```

Order

```
id
customer
tenant
total_amount
status
created_at
```

---

## Testing

Three assessment sections are tested independently.

- Query optimization
- Celery
- Tenant isolation

---

## Docker

Docker Compose contains

- Redis

Application connects using

```
redis://redis:6379/0
```

where

```
redis
```

is the Docker service name.

---

## Security

- Django ORM prevents SQL Injection.
- Tenant middleware isolates data.
- REST API validation through serializers.

---

## Future Improvements

- PostgreSQL
- JWT Authentication
- Celery Beat
- Monitoring
- Kubernetes Deployment
