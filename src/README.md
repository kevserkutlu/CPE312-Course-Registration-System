# 💻 Source Code

The application's business logic and core functionality are located in this folder.

### 🧩 Structure

* **`models.py`**: SQLAlchemy ORM models defining the database structure (Student, Instructor, Course, Enrollment).

* **`config/database/db.py`**: Database connection management, session handling, and table creation.

* **`services/`**: Business logic layer containing:
  * `student_service.py` - Student CRUD operations
  * `instructor_service.py` - Instructor CRUD operations
  * `course_service.py` - Course CRUD operations
  * `enrollment_service.py` - Enrollment management and reporting
  * `report_service.py` - Advanced reporting and analytics

* **`resources/`**: API resource layer wrapping services:
  * `student_resource.py` - Student API endpoints
  * `instructor_resource.py` - Instructor API endpoints
  * `course_resource.py` - Course API endpoints
  * `enrollment_resource.py` - Enrollment API endpoints
  * `report_resource.py` - Report API endpoints

### 🚀 Architecture

The application follows a **Service-Resource Pattern** (3-layer architecture):

```
Web Interface (HTML/CSS/JS)
    ↓
Flask Routes → Resources (API Layer)
    ↓
Services (Business Logic)
    ↓
SQLAlchemy Models (Data Layer)
    ↓
PostgreSQL Database
```

### 🔧 How to Use

Import and use the services or resources in your application:

```python
from src.resources import StudentResource
from src.config.database import DatabaseManager

db = DatabaseManager()
db.connect()
student_resource = StudentResource(db)

# Create a student
result = student_resource.create_student('John', 'Doe', 'Computer Science')
print(result['message'])

db.disconnect()
```

### 📦 Dependencies

All dependencies are listed in the root `requirements.txt`:
- Flask
- SQLAlchemy
- psycopg2-binary

