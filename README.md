# 🛠️ RentHub - Professional Equipment Rental Platform

RentHub is a robust web application built with **Django** that enables users to rent high-quality equipment, tools, and vehicles. This project demonstrates advanced Django concepts, including complex database relationships, custom business logic, and a polished user interface.

---

## 🚀 Setup Instructions

Follow these steps to initialize the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vivitoa/renthub-django.git
   cd renthub

3. **Create and Activate Virtual Environment:**
   ```bash
   python -m venv venv
   # Activate (Windows): venv\Scripts\activate
   # Activate (Mac/Linux): source venv/bin/activate

5. **Install Dependencies & Migrate:**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

---

## 💎 Database Seeding

To prepopulate the database with verified categories and items, run the following command in your terminal:

  ```bash
  python manage.py seed
  ```

*This will automatically generate initial data and professional images for the catalog.*

---

## 📱 Key Features & Functionality

### 1. Modern Landing Page
A dynamic homepage featuring a Hero section, service highlights, and quick-action buttons.
<img width="1328" height="883" alt="image" src="https://github.com/user-attachments/assets/16431fed-cd61-4e65-ba0c-57ac455fd186" />


### 2. Catalog & Advanced Search
- **Q-Object Search:** Implements a case-insensitive search engine that scans both Titles and Descriptions.
- **Custom Filters:** Uses a custom `|currency` filter for standardized price formatting.
<img width="1299" height="887" alt="image" src="https://github.com/user-attachments/assets/3b9c2f82-7c97-41b1-9ac0-c83dd9d6b30d" />


### 3. Reservation Management
- **Many-to-Many Relationships:** Supports multiple items per single reservation.
- **UX-Enhanced Forms:** Uses `CheckboxSelectMultiple` widgets for an intuitive item selection.
- **Automated Pricing:** Features a model `@property` that calculates total rental costs based on duration and item rates.
- **Custom Validation:** Server-side logic prevents invalid dates (e.g., end date before start date).
<img width="1308" height="698" alt="image" src="https://github.com/user-attachments/assets/00940a65-bee7-4dce-b1ab-5902a9b6c896" />


### 4. Professional CRUD Operations
- **Full CRUD:** Create, Read, Update, and Delete capabilities for both Items and Bookings.
- **Security:** CSRF protection and `readonly` fields for sensitive data during updates.
- **DRY Templates:** Implements a shared `base_delete.html` template for all confirmation pages.
<img width="1386" height="891" alt="image" src="https://github.com/user-attachments/assets/a34e1e22-d11b-4a0e-bdf8-6c7a8ba335ba" />
<img width="1313" height="895" alt="image" src="https://github.com/user-attachments/assets/0bf77b77-95cb-4c6e-bfae-276dbff29463" />
<img width="1289" height="598" alt="image" src="https://github.com/user-attachments/assets/164f3391-cf1c-491d-9f04-7624b9049e6c" />


### 5. Custom Django Admin
A tailored administrative interface with optimized `list_display`, `list_filter`, and logical `fieldsets`.
<img width="1905" height="744" alt="image" src="https://github.com/user-attachments/assets/23daf934-9cd7-48a5-95a7-b7e29b8f00e5" />


---

## 🛠️ Technical Stack
- **Backend:** Django 5.x (Python)
- **Frontend:** Bootstrap 5, Django Template Language (DTL)
- **Architecture:** Model-Template-View (MTV)

---

**Developed by:** Velina Serafimova
