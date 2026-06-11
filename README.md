# PaperLessGov - Digital File & Approval Management System

A complete, secure, and transparent e-governance system for digital file tracking and approval workflow management with comprehensive audit trails.

## 🌟 Key Features

### 1. **Complete Workflow Management**
- Multi-stage approval workflow (Draft → Pending Review → Under Review → Approved/Rejected)
- Role-based access control (Creators, Reviewers, Approvers, Admins)
- Automatic stage transitions with audit logging
- File assignment and reassignment tracking

### 2. **Comprehensive Audit Trail** ⭐ (Core Feature)
- **Every action is logged automatically** with:
  - User who performed the action
  - IP address and session tracking
  - Timestamp with microsecond precision
  - Before/after state for all changes
  - Request ID for complete traceability
- Immutable audit logs (read-only in admin)
- Full transparency for accountability
- Exportable audit reports

### 3. **File Management**
- Unique tracking IDs with date prefixes
- File attachments with version control
- Confidentiality levels (Public, Internal, Confidential, Secret)
- Priority levels (Low, Medium, High, Urgent)
- Due date tracking with overdue alerts
- Tag and keyword-based search

### 4. **Real-time Notifications**
- Automated notifications for:
  - File assignments
  - Stage changes
  - Approvals and rejections
  - Due date reminders
- In-app notification center

### 5. **Comments & Collaboration**
- Threaded comments on files
- Internal vs public comments
- Comment type classification (notes, reviews, approvals, rejections)
- Full audit trail for all comments

### 6. **Security Features**
- IP address logging for all actions
- Session tracking
- User agent recording
- Role-based permissions
- Department-level access control

## 📋 System Requirements

- Python 3.9+
- Django 5.0+
- SQLite (default) or PostgreSQL/MySQL

## 🚀 Installation & Setup

### Step 1: Navigate to Project Directory
```bash
cd d:\Projects\paperlessgov
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 6: Create Initial Data
```bash
python manage.py shell
```

Then in the shell:
```python
from filesys.models import Department
from django.contrib.auth.models import User

# Create sample departments
dept1 = Department.objects.create(
    code='FIN',
    name='Finance Department',
    description='Handles all financial matters'
)

dept2 = Department.objects.create(
    code='HR',
    name='Human Resources',
    description='Employee and personnel management'
)

print("Departments created successfully!")
exit()
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## 🎯 Quick Start Guide

### 1. Access the Application
- **Web Interface**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### 2. Create a Department (via Admin Panel)
1. Login to admin panel
2. Go to "Departments" under "FILESYS"
3. Create departments and assign heads

### 3. Create Your First File
1. Click "New File" on dashboard
2. Fill in file details:
   - Title
   - Category
   - Subject
   - Description
   - Department
   - Priority
   - Due date (optional)
3. Click "Create File"

### 4. Workflow Stages

#### Stage 1: Draft
- File is created and being edited
- Only creator can modify
- Actions: Submit for Review

#### Stage 2: Pending Review
- File submitted for review
- Department head assigns reviewer
- Actions: Assign to reviewer, Start Review

#### Stage 3: Under Review
- Assigned reviewer reviews the file
- Can add comments and attachments
- Actions: Approve or Reject

#### Stage 4: Approved/Rejected
- File is closed
- No further modifications possible
- Full audit trail available

### 5. View Audit Trail
Every file has a complete audit trail showing:
- Who created the file
- When it was submitted
- Who reviewed it
- When it was approved/rejected
- All comments and attachments
- IP addresses and timestamps

## 📊 Database Schema

### Core Models

1. **Department** - Government departments
2. **DigitalFile** - Main file model with workflow tracking
3. **FileAttachment** - File attachments with versioning
4. **Comment** - Threaded comments on files
5. **AuditLog** - ⭐ Complete audit trail of all actions
6. **Notification** - User notifications
7. **SystemSettings** - Global configuration

## 🔐 Security Features

### Audit Trail Integrity
- Audit logs are **immutable** (cannot be edited or deleted)
- Every action is logged with:
  - User information
  - IP address
  - Session key
  - User agent
  - Request ID
  - Timestamp
  - Previous and new states

### Access Control
- Login required for all views
- Role-based permissions (creator, assignee, department head, admin)
- Department-level access control
- Confidentiality levels on files and attachments

## 🎨 UI Features

- Modern dark theme interface
- Responsive design (mobile-friendly)
- Real-time statistics dashboard
- Color-coded workflow stages
- Priority indicators
- Overdue file alerts
- Filterable file lists
- Pagination support

## 📝 API Endpoints (AJAX)

- `/ajax/stats/` - File statistics
- `/ajax/notification/read/` - Mark notification as read

## 🧪 Testing

Run the test suite:
```bash
python manage.py test filesys
```

## 📁 Project Structure

```
paperlessgov/
├── filesys/                  # Main application
│   ├── models.py            # Database models with AuditLog
│   ├── views.py             # Workflow views
│   ├── urls.py              # URL configuration
│   ├── admin.py             # Admin configuration
│   └── templates/filesys/   # HTML templates
├── paperlessgov/            # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL config
│   └── wsgi.py              # WSGI config
├── media/                   # Uploaded files
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

## 🔧 Customization

### Adding New Workflow Stages
Edit `filesys/models.py` in the `DigitalFile` model:

```python
class DigitalFile(models.Model):
    STAGE_CUSTOM = 'custom_stage'

    WORKFLOW_STAGES = [
        # ... existing stages ...
        (STAGE_CUSTOM, 'Custom Stage'),
    ]
```

### Modifying Audit Log Actions
Edit `filesys/models.py` in the `AuditLog` model:

```python
ACTION_CHOICES = [
    # ... existing actions ...
    ('custom_action', 'Custom Action'),
]
```

## 🐛 Troubleshooting

### Issue: "No module named 'filesys'"
**Solution**: Ensure `filesys` is in `INSTALLED_APPS` in `settings.py`

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic`

### Issue: TemplateDoesNotExist error
**Solution**: Ensure templates directory structure is correct:
```
filesys/
└── templates/
    └── filesys/
        ├── base.html
        ├── dashboard.html
        └── ...
```

## 📞 Support

For issues and questions:
1. Check the audit logs in the admin panel
2. Review Django logs in the terminal
3. Check browser console for JavaScript errors

## 📜 License

This project is created for e-governance purposes and follows government transparency standards.

## ✨ Acknowledgments

- Built with Django 5.0
- Bootstrap 5 for UI
- Designed for transparency and accountability in government operations
