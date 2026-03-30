# Employee Management System

A Django-based web application for managing employees, departments, roles, and attendance.

## Requirements

- Python 3.12.0
- Django 6.0.3
- SQLite (default, no extra setup needed)

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd employee-management-system
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
cd ems_project
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

Admin panel: `http://127.0.0.1:8000/admin`

## Project Structure

```
employee-management-system/
├── ems_project/
│   ├── emp_app/          # Main app (models, views, templates)
│   │   ├── models.py     # Employee, Department, Role, Attendance
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   └── ems_project/      # Django project config
│       ├── settings.py
│       └── urls.py
├── requirements.txt
├── runtime.txt
└── README.md
```

## Models

- `Department` — name, location
- `Role` — name
- `Employee` — first/last name, department, role, salary, bonus, phone, hire date
- `Attendance` — employee, date, status

## Tech Stack

- Backend: Django 6.0.3
- Database: SQLite3
- Static files: WhiteNoise
- Server: Gunicorn (for production)
