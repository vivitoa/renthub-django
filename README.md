# 🛠️ RentHub - Professional Equipment Rental Platform

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-092E20.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791.svg)

RentHub is a robust web application built with **Django** that enables users to rent high-quality equipment, tools, and vehicles. This project demonstrates advanced Django concepts, including complex database relationships, custom business logic, and a polished user interface.

---

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Database Seeding](#database-seeding)
- [Key Features & Functionality](#key-features--functionality)
- [Project Structure](#project-structure)
- [Technical Stack](#technical-stack)

---

<a name="prerequisites"></a>
## ⚙️ Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.11** or higher installed
- **pip** (Python package installer) available
- **Git** installed on your local machine
- **PostgreSQL** installed and running locally

---

<a name="setup-instructions"></a>
## 🚀 Setup Instructions

Follow these steps to initialize the project locally:

**1. Clone the Repository:**

```bash
git clone https://github.com/vivitoa/renthub-django.git
cd renthub
```

**2. Create and Activate Virtual Environment:**

```bash
python -m venv venv
```

```bash
# Activate (Windows):
venv\Scripts\activate

# Activate (Mac/Linux):
source venv/bin/activate
```

**3. Install Dependencies:**

```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables:**

Create a `.env` file in the root of the project (see [Environment Variables](#-environment-variables) below).

**5. Create the PostgreSQL Database:**

```bash
# Connect to PostgreSQL and create the database
psql -U postgres -c "CREATE DATABASE renthub_db;"
```

**6. Run Migrations & Start the Server:**

```bash
python manage.py migrate
python manage.py runserver
```

**7. (Optional) Create a Superuser to access the Admin Panel:**

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password. Then log in at:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


---

<a name="environment-variables"></a>
## 🔐 Environment Variables

The application uses **PostgreSQL** as its database. A `.env` file is required if your local PostgreSQL credentials differ from the defaults.

> ✅ **Out-of-the-box:** The project runs without a `.env` file if your local PostgreSQL uses the default `postgres` user and `password` as the password. Simply ensure the database `renthub_db` exists (see Step 5 above).

If your credentials differ, create a `.env` file in the project root:

```env
DB_NAME=renthub_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

> ⚠️ The `.env` file is listed in `.gitignore` and will **not** be committed to version control.

The application loads these values via `python-dotenv` at startup and passes them to the Django database configuration in `settings.py`.

---

<a name="database-seeding"></a>
## 💎 Database Seeding

To prepopulate the database with verified categories and items, run the following custom management command in your terminal:

```bash
python manage.py seed
```

This will automatically generate initial data and professional images for the catalog, allowing you to test the platform instantly.

---

<a name="key-features--functionality"></a>
## 📱 Key Features & Functionality

### 1. Modern Landing Page

A dynamic homepage featuring a Hero section, service highlights, and quick-action buttons.

![Landing Page](https://github.com/user-attachments/assets/16431fed-cd61-4e65-ba0c-57ac455fd186)

### 2. Catalog & Advanced Search

- **Q-Object Search:** Implements a case-insensitive search engine that scans both Titles and Descriptions.
- **Custom Filters:** Uses a custom `|currency` filter for standardized price formatting.

![Catalog](https://github.com/user-attachments/assets/3b9c2f82-7c97-41b1-9ac0-c83dd9d6b30d)

### 3. Reservation Management

- **Many-to-Many Relationships:** Supports multiple items per single reservation.
- **UX-Enhanced Forms:** Uses `CheckboxSelectMultiple` widgets for an intuitive item selection.
- **Automated Pricing:** Features a model `@property` that calculates total rental costs based on duration and item rates.
- **Custom Validation:** Server-side logic prevents invalid dates (e.g., end date before start date).

![Reservations](https://github.com/user-attachments/assets/00940a65-bee7-4dce-b1ab-5902a9b6c896)

### 4. Professional CRUD Operations

- **Full CRUD:** Create, Read, Update, and Delete capabilities for both Items and Bookings.
- **Security:** CSRF protection and readonly fields for sensitive data during updates.
- **DRY Templates:** Implements a shared `base_delete.html` template for all confirmation pages.

![CRUD 1](https://github.com/user-attachments/assets/a34e1e22-d11b-4a0e-bdf8-6c7a8ba335ba)
![CRUD 2](https://github.com/user-attachments/assets/0bf77b77-95cb-4c6e-bfae-276dbff29463)
![CRUD 3](https://github.com/user-attachments/assets/164f3391-cf1c-491d-9f04-7624b9049e6c)

### 5. Custom Django Admin

A tailored administrative interface with optimized `list_display`, `list_filter`, and logical fieldsets.

![Admin](https://github.com/user-attachments/assets/23daf934-9cd7-48a5-95a7-b7e29b8f00e5)

---

<a name="project-structure"></a>
## 📁 Project Structure

The architecture is divided into three main, modular Django apps to ensure separation of concerns:

- **`common/`** — Handles the landing page, custom tags, and abstract models.
- **`catalog/`** — Manages the items, categories, search functionality, and database seeding logic.
- **`bookings/`** — Manages the reservation process, form validations, and complex pricing logic.

---

<a name="technical-stack"></a>
## 🛠️ Technical Stack

| Layer        | Technology                            |
|--------------|---------------------------------------|
| Backend      | Django 5.x (Python 3.11+)             |
| Frontend     | Bootstrap 5.3, Django Template Language |
| Architecture | Model-Template-View (MTV)             |
| Database     | PostgreSQL 16+                        |

---

> Developed as an **Individual Project** for the *Django Basics Course* @ [SoftUni](https://softuni.bg)

