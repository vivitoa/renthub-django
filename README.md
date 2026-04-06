# RentHub - Professional Equipment Rental Platform

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0-092E20.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791.svg)
![DRF](https://img.shields.io/badge/DRF-3.x-red.svg)
![Celery](https://img.shields.io/badge/Celery-5.x-37814A.svg)

RentHub is a full-stack web application built with **Django** that enables users to browse, rent, and manage high-quality equipment. The project demonstrates advanced Django concepts including custom authentication, REST API, asynchronous tasks, and deployment.

**Live Demo:** [renthub-django-production.up.railway.app](https://renthub-django-production.up.railway.app)

---

## Table of Contents
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Project Structure](#project-structure)
- [REST API](#rest-api)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Running Tests](#running-tests)
- [Deployment](#deployment)

---

## Features

### Authentication & User Management
- Custom user model with email-based authentication (`AbstractBaseUser`)
- User registration, login, logout
- Profile management with profile picture upload (`ImageField`)
- Automatic profile creation via `post_save` signal
- Welcome email sent on registration

### Catalog
- Full CRUD for rental items (create, read, update, delete)
- Item image upload
- Search by name and description (Q objects)
- Category filtering
- Custom template filter for currency formatting

### Reservations (Bookings)
- Many-to-many relationship between reservations and items
- Automatic total price calculation via model `@property`
- Custom form validation (end date must be after start date)
- Reservation confirmation email sent asynchronously via Celery
- Users can only view and edit their own reservations

### Wishlist
- Each user has an auto-created wishlist (via `post_save` signal)
- Toggle items in/out of wishlist from item detail page
- Wishlist count shown on profile page

### Reviews
- Users can add reviews to items
- Only review owners can edit or delete their review
- Nested display on item detail page

### Access Control
- `LoginRequiredMixin` on all protected views
- Custom `CheckUserIsOwner` and `CheckUserIsItemOwner` mixins
- Two user groups in admin: **Renters** and **Owners** with distinct permissions

### REST API (Django REST Framework)
- Full CRUD API for Items and Reservations
- Custom `IsOwnerOrReadOnly` permission class
- Session authentication
- Default permission: `IsAuthenticatedOrReadOnly`

### Async Tasks (Celery + Redis)
- Celery worker with Redis as message broker
- `django-celery-results` for task result storage in the database
- Async email sending on reservation creation

### Admin Panel
- Custom `UserAdmin` with `AppUserCreationForm` and `AppUserChangeForm`
- Registered models: `AppUser`, `Profile`, `Item`, `Review`, `Reservation`, `Wishlist`
- Custom `list_display`, `list_filter`, `search_fields` on all models

### Security & Deployment
- Environment variables via `python-dotenv`
- Separate `settings_production.py` for production deployment
- WhiteNoise for static file serving
- `dj-database-url` for `DATABASE_URL` parsing
- Gunicorn as WSGI server
- HTTPS via Railway proxy (`SECURE_PROXY_SSL_HEADER`)

---

## Technical Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 (Python 3.12) |
| Frontend | Bootstrap 5.3, Django Template Language |
| Database | PostgreSQL 16+ |
| REST API | Django REST Framework |
| Async Tasks | Celery 5.x + Redis |
| Task Results | django-celery-results |
| Static Files | WhiteNoise |
| Deployment | Railway (Gunicorn) |
| Image Handling | Pillow |

---

## Project Structure

```
renthub-django/
├── accounts/                   # Custom user model, profile, authentication
│   ├── managers.py             # AppUserManager (email-based auth)
│   ├── models.py               # AppUser, Profile
│   ├── signals.py              # Auto-create profile + send welcome email
│   ├── forms.py                # Registration and profile edit forms
│   ├── views.py                # Register, profile detail/edit/delete
│   └── admin.py                # Custom UserAdmin
├── catalog/                    # Items and reviews
│   ├── models.py               # Item, Review
│   ├── api_views.py            # DRF API views for items
│   ├── serializers.py          # ItemSerializer, ReviewSerializer
│   └── management/commands/seed.py
├── bookings/                   # Reservations
│   ├── models.py               # Reservation (ManyToMany with Item)
│   ├── tasks.py                # Celery task: send confirmation email
│   ├── api_views.py            # DRF API views for reservations
│   └── serializers.py          # ReservationSerializer
├── wishlist/                   # User wishlists
│   ├── models.py               # Wishlist (ManyToMany with Item)
│   └── signals.py              # Auto-create wishlist on user registration
├── common/                     # Shared utilities
│   ├── mixins.py               # CheckUserIsOwner, CheckUserIsItemOwner
│   ├── permissions.py          # IsOwnerOrReadOnly (DRF)
│   └── templatetags/           # custom_tags (currency filter)
└── renthub/                    # Project configuration
    ├── settings.py
    ├── settings_production.py
    ├── celery.py
    └── api_urls.py
```

---

## REST API

Base URL: `/api/`

| Endpoint | Method | Auth Required | Description |
|---|---|---|---|
| `/api/items/` | GET | No | List all items |
| `/api/items/` | POST | Yes | Create item |
| `/api/items/<id>/` | GET | No | Item detail |
| `/api/items/<id>/` | PUT/PATCH | Owner only | Update item |
| `/api/items/<id>/` | DELETE | Owner only | Delete item |
| `/api/reservations/` | GET | Yes | List user's reservations |
| `/api/reservations/` | POST | Yes | Create reservation |
| `/api/reservations/<id>/` | GET | Yes | Reservation detail |
| `/api/reservations/<id>/` | PUT/PATCH | Owner only | Update reservation |
| `/api/reservations/<id>/` | DELETE | Owner only | Delete reservation |

---

## Setup Instructions

**1. Clone the repository:**
```bash
git clone https://github.com/vivitoa/renthub-django.git
cd renthub-django
```

**2. Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables:**

Create a `.env` file in the project root (see [Environment Variables](#environment-variables)).

**5. Create the PostgreSQL database:**
```bash
psql -U postgres -c "CREATE DATABASE renthub_db;"
```

**6. Run migrations:**
```bash
python manage.py migrate
```

**7. Seed the database:**
```bash
python manage.py seed
```

**8. Create a superuser:**
```bash
python manage.py createsuperuser
```

**9. Start Redis (required for Celery):**
```bash
redis-server
```

**10. Start Celery worker (in a separate terminal):**
```bash
celery -A renthub worker -l info
```

**11. Start the development server:**
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DB_NAME=renthub_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
COMPANY_EMAIL=noreply@renthub.com
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
CELERY_BROKER_URL=redis://localhost:6379/0
```

> The `.env` file is listed in `.gitignore` and will not be committed to version control.

---

## Running Tests

```bash
python manage.py test
```

The test suite includes 22 tests covering:
- Model creation and validation
- Signal handlers (profile and wishlist auto-creation)
- View access control (login required, ownership checks)
- Form validation
- Celery task invocation (mocked with `unittest.mock.patch`)

---

## Deployment

The application is deployed on **Railway** with:
- **PostgreSQL** and **Redis** as Railway services
- **Gunicorn** as the WSGI server
- **WhiteNoise** for static file serving
- **dj-database-url** for database configuration from `DATABASE_URL`

Environment variables required in Railway:

| Variable | Value |
|---|---|
| `DJANGO_SETTINGS_MODULE` | `renthub.settings_production` |
| `SECRET_KEY` | your production secret key |
| `DATABASE_URL` | auto-provided by Railway Postgres |
| `REDIS_URL` | auto-provided by Railway Redis |
| `ALLOWED_HOSTS` | your Railway domain |
| `CSRF_TRUSTED_ORIGINS` | `https://your-railway-domain` |

---

> Developed as an **Individual Project** for the *Django Advanced Course* @ [SoftUni](https://softuni.bg)
