# Electronics-Repair-Service-System
# 🛠️ Repair Service Management System

• A full-stack **Django-based web application** to manage internal and external service requests for electronics repair such as **Energizer**, **Gate Motor Controllers**, and **Power Adapters**.  

• The system stores data in a **SQLite database** and also syncs with **Google Sheets** for tracking and analytics.

---

## 🧱 Project Structure
```
repair_service/
│
├── core/ – Main Django app with business logic
│ ├── admin.py – Django admin configuration
│ ├── apps.py – App settings
│ ├── forms.py – User & service request forms
│ ├── models.py – Database models
│ ├── sheets_sync.py – Google Sheets integration
│ ├── urls.py – URL routing
│ ├── views.py – App logic
│ ├── templates/core/ – HTML templates
│ └── migrations/ – Database migration files
│
├── manage.py – Django management script
├── db.sqlite3 – SQLite database
├── credentials.json – Google Sheets API credentials
└── requirements.txt – Python dependencies

```
## 🚀 How to Run
### Prerequisites
```
• Python 3.x
• pip
• Django
• Pillow (pip install Pillow)
```

## ⚙️ Setup Instructions

### Step 1: Clone the project or extract ZIP
```
unzip repair_service.zip
cd repair_service
```

### Step 2: Create a virtual environment
```
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### Step 3: Install dependencies
```
pip install -r requirements.txt
pip install django google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

### Step 4:Configure Google Sheets API
```
Go to Google Cloud Console
Enable Google Sheets API and Google Drive API
Download credentials.json and place it in the root folder (repair_service/)
```

### Step 5:Apply database migrations
```
python manage.py migrate
```

### Step 6:Create an admin user
```
python manage.py createsuperuser
Visit in your browser:(for admin panel):
http://127.0.0.1:8000/admin
```

### Step 7:Start the development server
```
python manage.py runserver
Visit in your browser:
http://127.0.0.1:8000/
```

### Step 8:🧪 Test the Application
```
Public Endpoints
/ – Home page
/register/ – Register a new account
/login/ – Login page

Internal Users
/dashboard_internal/ – View and update service requests
/update_status/ – Change request status

External Users
/dashboard_external/ – View submitted requests
/service_request/ – Submit a new request

Admin Panel
/admin/ – Django admin interface
```
