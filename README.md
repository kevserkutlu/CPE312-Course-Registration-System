# 🎓 Course Registration System - CPE312# 🎓 Course Registration System - CPE312



A comprehensive fullstack university course management system with modern web UI, built with Flask backend and PostgreSQL database.A comprehensive fullstack university course management system with modern web UI, built with Flask backend and PostgreSQL database.



## 📋 System Features## 📋 System Features



This project is a comprehensive database management system developed to manage course registration processes in a university environment. The system provides management for students, instructors, courses, and enrollments.This project is a comprehensive database management system developed to manage course registration processes in a university environment. The system provides management for students, instructors, courses, and enrollments.



### ✅ Core Functionality



- **👥 Student Management** - Add, update, delete, and list students### ✅ Core Functionality

- **👨‍🏫 Instructor Management** - Add, update, delete, and list instructors  

- **📖 Course Management** - Add, update, delete, and list courses

- **📋 Enrollment Management** - Register students, drop courses, assign grades

- **📊 Reporting & Analytics** - Five different report types with detailed statistics- **👥 Student Management** - Add, update, delete, and list students## 📋 Sistem Özellikleri## 👥 Proje Ekibi

- **⚠️ Error Handling & Validation** - Comprehensive validation on all operations

- **👨‍🏫 Instructor Management** - Add, update, delete, and list instructors  

### 📊 Available Reports

- **📖 Course Management** - Add, update, delete, and list courses* **Merve Karataş** - 64220045

1. **Students Enrolled in Course** - View all students in a specific course with grades

2. **Student Course List** - View all courses a student is enrolled in- **📋 Enrollment Management** - Register students, drop courses, assign grades

3. **Instructor Workload** - See workload distribution across all instructors

4. **Department Statistics** - View student and instructor counts per department- **📊 Reporting & Analytics** - Five different report types with detailed statistics### ✅ Yapılan İşlemler* **Kevser Kutlu** - 64220018

5. **Grade Distribution** - Analyze grade distribution in a course

- **⚠️ Error Handling & Validation** - Comprehensive validation on all operations

## 👥 Project Team

- **✓ Öğrenci Yönetimi** - Ekle, güncelle, sil, listele* **Arife Zeynep Muratoğlu** - 64220048

* **Merve Karataş** - 64220045

* **Kevser Kutlu** - 64220018### 📊 Available Reports

* **Arife Zeynep Muratoğlu** - 64220048

- **✓ Öğretim Görevlisi Yönetimi** - Ekle, güncelle, sil, listele

## 📂 Project Structure

1. **Students Enrolled in Course** - View all students in a specific course with grades

```

CPE312-Course-Registration-System/2. **Student Course List** - View all courses a student is enrolled in- **✓ Ders Yönetimi** - Ekle, güncelle, sil, listele## 📂 Proje Yapısı

├── database/

│   └── schema.sql                      # Database schema and sample data3. **Instructor Workload** - See workload distribution across all instructors

├── docs/

│   └── Course Registration System_Proposal.pdf4. **Department Statistics** - View student and instructor counts per department- **✓ Ders Kayıt İşlemleri** - Kaydet, çıkar, not ver```

├── src/

│   ├── app.py                          # Legacy app entry point (example usage)5. **Grade Distribution** - Analyze grade distribution in a course

│   ├── models.py                       # SQLAlchemy ORM models

│   ├── config/- **✓ Raporlama ve Analitiği** - İstatistikler ve detaylı raporlarCPE312-Course-Registration-System/

│   │   └── database/

│   │       ├── __init__.py## 👥 Project Team

│   │       └── db.py                   # Database connection management

│   ├── services/                       # Business logic layer- **✓ Hata Yönetimi ve Validasyon** - Tüm operasyonlarda├── database/

│   │   ├── __init__.py

│   │   ├── student_service.py          # Student CRUD operations* **Merve Karataş** - 64220045

│   │   ├── instructor_service.py       # Instructor CRUD operations

│   │   ├── course_service.py           # Course CRUD operations* **Kevser Kutlu** - 64220018│   └── schema.sql              # Veritabanı şeması ve örnek veriler

│   │   ├── enrollment_service.py       # Enrollment operations

│   │   └── report_service.py           # Reporting functionality* **Arife Zeynep Muratoğlu** - 64220048

│   ├── resources/                      # API layer

│   │   ├── __init__.py## 👥 Proje Ekibi├── docs/

│   │   ├── student_resource.py

│   │   ├── instructor_resource.py## 📂 Project Structure

│   │   ├── course_resource.py

│   │   ├── enrollment_resource.py* **Merve Karataş** - 64220045│   └── Course Registration System_Proposal.pdf

│   │   └── report_resource.py

│   └── README.md```

├── templates/

│   └── index.html                      # Main web interfaceCPE312-Course-Registration-System/* **Kevser Kutlu** - 64220018├── src/

├── static/

│   ├── style.css                       # Responsive styling├── database/

│   └── script.js                       # Frontend JavaScript

├── web.py                              # Flask web application│   └── schema.sql                      # Database schema and sample data* **Arife Zeynep Muratoğlu** - 64220048│   ├── app.py                  # Ana uygulama

├── requirements.txt                    # Python dependencies

├── .gitignore├── docs/

├── run.sh                              # macOS/Linux startup script

├── run.bat                             # Windows startup script│   └── Course Registration System_Proposal.pdf│   ├── models.py               # SQLAlchemy ORM modelleri

└── README.md                           # This file

```├── src/



## 🛠️ Technology Stack│   ├── app.py                          # Legacy app entry point## 📂 Proje Yapısı│   ├── config/



| Component | Technology |│   ├── models.py                       # SQLAlchemy ORM models

|-----------|-----------|

| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |│   ├── config/│   │   └── database/

| **Backend** | Python 3.11+, Flask |

| **ORM** | SQLAlchemy 2.0.45 |│   │   └── database/

| **Database** | PostgreSQL |

| **Architecture** | Service-Resource Pattern (3-layer architecture) |│   │       ├── __init__.py```│   │       ├── __init__.py



## 📋 Requirements│   │       └── db.py                   # Database connection management



- **Python 3.11+** - Programming language│   ├── services/                       # Business logic layerCPE312-Course-Registration-System/│   │       └── db.py           # Veritabanı bağlantı yönetimi

- **PostgreSQL 12+** - Database server

- **pip** - Python package manager│   │   ├── student_service.py



## 🚀 Installation and Running│   │   ├── instructor_service.py├── database/│   └── README.md



### Quick Start (Recommended)│   │   ├── course_service.py



#### macOS / Linux:│   │   ├── enrollment_service.py│   └── schema.sql                      # Veritabanı şeması ve örnek veriler├── requirements.txt            # Python bağımlılıkları



```bash│   │   └── report_service.py

cd CPE312-Course-Registration-System

chmod +x run.sh│   ├── resources/                      # API layer├── docs/├── .gitignore

./run.sh

```│   │   ├── student_resource.py



#### Windows:│   │   ├── instructor_resource.py│   └── Course Registration System_Proposal.pdf└── README.md



```bash│   │   ├── course_resource.py

cd CPE312-Course-Registration-System

run.bat│   │   ├── enrollment_resource.py├── src/```

```

│   │   └── report_resource.py

### Manual Setup

│   └── __init__.py│   ├── app.py                          # Ana uygulama (örnek kullanım)

1. **Clone the repository:**

├── templates/

```bash

git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git│   └── index.html                      # Main web interface│   ├── models.py                       # SQLAlchemy ORM modelleri## 🛠️ Teknolojiler

cd CPE312-Course-Registration-System

```├── static/



2. **Create virtual environment:**│   ├── style.css                       # Responsive styling│   ├── config/* **Database:** PostgreSQL



```bash│   └── script.js                       # Frontend JavaScript

# macOS / Linux

python3 -m venv .venv├── web.py                              # Flask web application│   │   └── database/* **Language:** Python 3.11+

source .venv/bin/activate

├── requirements.txt                    # Python dependencies

# Windows

python -m venv .venv├── run.sh                              # macOS/Linux startup script│   │       ├── __init__.py* **ORM:** SQLAlchemy 2.0.45

.venv\Scripts\activate

```├── run.bat                             # Windows startup script



3. **Install dependencies:**└── README.md                           # This file│   │       └── db.py                   # Veritabanı bağlantı yönetimi* **Database Driver:** psycopg2-binary



```bash```

pip install -r requirements.txt

```│   ├── services/                       # İş mantığı katmanı



4. **Database Configuration**## 🛠️ Technology Stack



Create a database named `course_registration` in PostgreSQL:│   │   ├── __init__.py## 📋 Gereksinimler



```sql| Component | Technology |

CREATE DATABASE course_registration;

```|-----------|-----------|│   │   ├── enrollment_service.py       # Kayıt işlemleri* Python 3.11 veya daha yüksek



**Note:** Default connection settings in `db.py`:| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |

- Username: `postgres`

- Password: `kvyu8dutx`| **Backend** | Python 3.11+, Flask |│   │   ├── student_service.py          # Öğrenci CRUD* PostgreSQL 12 veya daha yüksek

- Host: `127.0.0.1`

- Port: `5432`| **ORM** | SQLAlchemy 2.0.45 |

- Database: `postgres`

| **Database** | PostgreSQL |│   │   ├── instructor_service.py       # Öğretim görevlisi CRUD* pip (Python paket yöneticisi)

If you use different settings, set environment variables:

| **Architecture** | Service-Resource Pattern (3-layer architecture) |

```bash

export DB_USER=your_username│   │   ├── course_service.py           # Ders CRUD

export DB_PASSWORD=your_password

export DB_HOST=your_host## 📦 Installation

export DB_PORT=your_port

export DB_NAME=your_database_name│   │   └── report_service.py           # Raporlama## 🚀 Kurulum ve Çalıştırma

```

### Prerequisites

5. **Run the application:**

│   ├── resources/                      # API katmanı

```bash

python3 web.py- **Python 3.11+** installed

```

- **PostgreSQL** installed and running│   │   ├── __init__.py### 1. Projeyi Klonla

The application will start on `http://localhost:5001`

- **pip** (Python package manager)

Or use the startup script:

│   │   ├── enrollment_resource.py```bash

```bash

# macOS/Linux### Quick Start (Recommended)

./run.sh

│   │   ├── student_resource.pygit clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git

# Windows

run.bat#### macOS / Linux:

```

│   │   ├── instructor_resource.pycd CPE312-Course-Registration-System

To stop the application: **Press Ctrl+C**

```bash

## 🚀 How to Use the Web Interface

cd CPE312-Course-Registration-System│   │   ├── course_resource.py```

### 1. **Students Tab**

- **Add Student**: Fill in first name, last name, and department, then click "Add"chmod +x run.sh

- **List Students**: Click "Load" to see all students with delete options

- **Edit Student**: Click the edit button next to a student to modify information./run.sh│   │   └── report_resource.py



### 2. **Instructors Tab**```

- **Add Instructor**: Fill in first name, last name, and department, then click "Add"

- **List Instructors**: Click "Load" to see all instructors│   └── README.md### 2. Sanal Ortam Oluştur (Python Virtual Environment)

- **Edit Instructor**: Click the edit button to modify instructor information

#### Windows:

### 3. **Courses Tab**

- **Add Course**: Enter course name and instructor ID, then click "Add"├── requirements.txt                    # Python bağımlılıkları```bash

- **List Courses**: Click "Load" to see all courses

- **Edit Course**: Click the edit button to modify course information```cmd



### 4. **Enrollments Tab**cd CPE312-Course-Registration-System├── .gitignore# macOS / Linux

- **Enroll Student**: Enter student ID and course ID, click "Enroll"

- **Drop Course**: Enter student ID and course ID, click "Drop"run.bat

- **Assign Grade**: Enter student and course IDs, select a grade, click "Assign"

- **View Courses**: Enter student ID to see their enrolled courses```└── README.mdpython3 -m venv .venv



### 5. **Reports Tab**

- **Students per Course**: View all students in a specific course

- **Courses per Student**: View all courses a student is enrolled in### Manual Setup```source .venv/bin/activate

- **Instructor Workload**: See all instructors and their teaching load

- **Department Statistics**: View statistics by department

- **Grade Distribution**: Analyze grade distribution in a course

1. **Clone the repository:**

## 🏗️ Architecture

```bash

### Service-Resource Pattern (3-Layer Architecture)

git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git## 🛠️ Teknolojiler# Windows

```

┌─────────────────────────────────────────┐cd CPE312-Course-Registration-System

│         Web Interface (HTML/CSS/JS)     │

│           (Presentation Layer)          │```* **Database:** PostgreSQLpython -m venv .venv

└─────────────────────────────────────────┘

                    ↓

┌─────────────────────────────────────────┐

│      Flask Routes & Resources           │2. **Create virtual environment:*** **Language:** Python 3.11+.venv\Scripts\activate

│           (API Layer)                   │

│  - StudentResource                      │```bash

│  - InstructorResource                   │

│  - CourseResource                       │python3 -m venv .venv* **ORM:** SQLAlchemy 2.0.45```

│  - EnrollmentResource                   │

│  - ReportResource                       │source .venv/bin/activate  # macOS/Linux

└─────────────────────────────────────────┘

                    ↓# or* **Database Driver:** psycopg2-binary

┌─────────────────────────────────────────┐

│         Services (Business Logic)       │.venv\Scripts\activate  # Windows

│           (Service Layer)               │

│  - StudentService                       │```### 3. Bağımlılıkları Yükle

│  - InstructorService                    │

│  - CourseService                        │

│  - EnrollmentService                    │

│  - ReportService                        │3. **Install dependencies:**## 📋 Gereksinimler```bash

└─────────────────────────────────────────┘

                    ↓```bash

┌─────────────────────────────────────────┐

│    SQLAlchemy ORM & Models              │pip install -r requirements.txt* Python 3.11 veya daha yüksekpip install -r requirements.txt

│           (Data Layer)                  │

│  - Student                              │```

│  - Instructor                           │

│  - Course                               │* PostgreSQL 12 veya daha yüksek```

│  - Enrollment                           │

└─────────────────────────────────────────┘4. **Run the application:**

                    ↓

┌─────────────────────────────────────────┐```bash* pip (Python paket yöneticisi)

│          PostgreSQL Database            │

│        (Persistence Layer)              │python3 web.py

└─────────────────────────────────────────┘

``````### 4. Veritabanı Konfigürasyonu



This architecture ensures:

- **Separation of Concerns** - Each layer has a specific responsibility

- **Maintainability** - Code is organized and easy to modify5. **Open in browser:**## 🚀 Kurulum ve ÇalıştırmaPostgreSQL'de `course_registration` adında bir veritabanı oluştur:

- **Scalability** - Easy to add new features

- **Testability** - Each layer can be tested independently```



## 🔌 API Endpointshttp://localhost:5001



### Students```



- `GET /api/students` - Get all students### 1. Projeyi Klonla```sql

- `POST /api/students` - Create a new student

- `GET /api/students/<id>` - Get a specific student## 🚀 How to Use

- `PUT /api/students/<id>` - Update a student

- `DELETE /api/students/<id>` - Delete a student```bashCREATE DATABASE course_registration;



### Instructors### 1. **Students Tab**



- `GET /api/instructors` - Get all instructors- **Add Student**: Fill in first name, last name, and department, then click "Add"git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git```

- `POST /api/instructors` - Create a new instructor

- `GET /api/instructors/<id>` - Get a specific instructor- **List Students**: Click "Load" to see all students with delete options

- `PUT /api/instructors/<id>` - Update an instructor

- `DELETE /api/instructors/<id>` - Delete an instructorcd CPE312-Course-Registration-System



### Courses### 2. **Instructors Tab**



- `GET /api/courses` - Get all courses- **Add Instructor**: Fill in first name, last name, and department, then click "Add"```**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:

- `POST /api/courses` - Create a new course

- `GET /api/courses/<id>` - Get a specific course- **List Instructors**: Click "Load" to see all instructors

- `PUT /api/courses/<id>` - Update a course

- `DELETE /api/courses/<id>` - Delete a course- Kullanıcı: `postgres`



### Enrollments### 3. **Courses Tab**



- `POST /api/enrollments` - Enroll a student in a course- **Add Course**: Enter course name and instructor ID, then click "Add"### 2. Sanal Ortam Oluştur (Python Virtual Environment)- Şifre: `kvyu8dutx`

- `POST /api/enrollments/drop` - Drop a student from a course

- `POST /api/enrollments/grade` - Assign a grade to an enrollment- **List Courses**: Click "Load" to see all courses

- `GET /api/enrollments/student/<id>` - Get courses for a student

- `GET /api/enrollments/course/<id>` - Get students in a course```bash- Host: `127.0.0.1`



### Reports### 4. **Enrollments Tab**



- `GET /api/reports/students-per-course/<id>` - Students in a course- **Enroll Student**: Enter student ID and course ID, click "Enroll"# macOS / Linux- Port: `5432`

- `GET /api/reports/courses-per-student/<id>` - Courses for a student

- `GET /api/reports/instructor-workload` - Instructor workload- **Drop Course**: Enter student ID and course ID, click "Drop"

- `GET /api/reports/department-statistics` - Department statistics

- `GET /api/reports/grade-distribution/<id>` - Grade distribution- **Assign Grade**: Enter student and course IDs, select a grade, click "Assign"python3 -m venv .venv- Veritabanı: `postgres`



## 📊 Database Schema- **View Courses**: Enter student ID to see their enrolled courses



### Student Tablesource .venv/bin/activate



| Column | Type | Constraint |### 5. **Reports Tab**

|--------|------|-----------|

| student_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |- **Students per Course**: View all students in a specific courseEğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:

| fname | VARCHAR(100) | NOT NULL |

| lname | VARCHAR(100) | NOT NULL |- **Courses per Student**: View all courses a student is enrolled in

| department | VARCHAR(100) | NOT NULL |

- **Instructor Workload**: See all instructors and their teaching load# Windows```bash

### Instructor Table

- **Department Statistics**: View statistics by department

| Column | Type | Constraint |

|--------|------|-----------|- **Grade Distribution**: Analyze grade distribution in a coursepython -m venv .venvexport DB_USER=your_username

| instructor_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |

| fname | VARCHAR(100) | NOT NULL |

| lname | VARCHAR(100) | NOT NULL |

| department | VARCHAR(100) | NOT NULL |## 🏗️ Architecture.venv\Scripts\activateexport DB_PASSWORD=your_password



### Course Table



| Column | Type | Constraint |### Service-Resource Pattern (3-Layer Architecture)```export DB_HOST=your_host

|--------|------|-----------|

| course_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |

| course_name | VARCHAR(150) | NOT NULL |

| instructor_id | INTEGER | FOREIGN KEY |```export DB_PORT=your_port



### Enrollment Table┌─────────────────────────────────────────┐



| Column | Type | Constraint |│         Web Interface (HTML/CSS/JS)     │### 3. Bağımlılıkları Yükleexport DB_NAME=your_database_name

|--------|------|-----------|

| enrollment_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |│           (Presentation Layer)          │

| student_id | INTEGER | FOREIGN KEY |

| course_id | INTEGER | FOREIGN KEY |└────────────────────────────────────────┘```bash```

| grade | VARCHAR(2) | NULLABLE |

                    ↓

### Relationships

┌─────────────────────────────────────────┐pip install -r requirements.txt

- One Instructor can have many Courses

- One Student can enroll in many Courses (via Enrollment table)│      Flask Routes & Resources           │

- The Enrollment table provides a Many-to-Many relationship between Students and Courses

│           (API Layer)                   │```### 5. Uygulamayı Çalıştır

### SQL Schema with Sample Data

│  - StudentResource                      │

```sql

CREATE TABLE student (│  - InstructorResource                   │```bash

    student_id SERIAL PRIMARY KEY,

    fname VARCHAR(50),│  - CourseResource                       │

    lname VARCHAR(50),

    department VARCHAR(50)│  - EnrollmentResource                   │### 4. Veritabanı Konfigürasyonupython3 app.py

);

│  - ReportResource                       │

CREATE TABLE instructor (

    instructor_id SERIAL PRIMARY KEY,└────────────────────────────────────────┘PostgreSQL'de `course_registration` adında bir veritabanı oluştur:```

    fname VARCHAR(50),

    lname VARCHAR(50),                    ↓

    department VARCHAR(50)

);┌─────────────────────────────────────────┐



CREATE TABLE course (│         Services (Business Logic)       │

    course_id SERIAL PRIMARY KEY,

    course_name VARCHAR(100),│           (Service Layer)               │```sql**Çıktı:**

    instructor_id INT REFERENCES instructor(instructor_id)

);│  - StudentService                       │



CREATE TABLE enrollment (│  - InstructorService                    │CREATE DATABASE course_registration;```

    enrollment_id SERIAL PRIMARY KEY,

    student_id INT REFERENCES student(student_id),│  - CourseService                        │

    course_id INT REFERENCES course(course_id),

    grade VARCHAR(2)│  - EnrollmentService                    │```PostgreSQL bağlantısı başarıyla kuruldu! ✅

);

```│  - ReportService                        │



## 🔧 ORM Models└────────────────────────────────────────┘✓ Tablolar oluşturuldu



### Student Model                    ↓



```python┌─────────────────────────────────────────┐**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:Uygulama çalışıyor...

from src.models import Student

│    SQLAlchemy ORM & Models              │

# Query all students

with db.session_scope() as session:│           (Data Layer)                  │- Kullanıcı: `postgres`

    students = session.query(Student).all()

    for student in students:│  - Student                              │

        print(f"{student.fname} {student.lname}")

│  - Instructor                           │- Şifre: `kvyu8dutx`Toplam 10 öğrenci bulundu:

# Add a new student

with db.session_scope() as session:│  - Course                               │

    new_student = Student(

        fname="Ali",│  - Enrollment                           │- Host: `127.0.0.1`  - Merve Karatas (Computer Engineering)

        lname="Demir",

        department="Computer Engineering"└────────────────────────────────────────┘

    )

    session.add(new_student)                    ↓- Port: `5432`  - Kevser Kutlu (Software Engineering)

```

┌─────────────────────────────────────────┐

### Instructor Model

│          PostgreSQL Database            │- Veritabanı: `postgres`  ...

```python

from src.models import Instructor│        (Persistence Layer)              │



# Query all instructors└────────────────────────────────────────┘```

with db.session_scope() as session:

    instructors = session.query(Instructor).all()```

    for instructor in instructors:

        print(f"{instructor.fname} {instructor.lname}")Eğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:

```

## 🔌 API Endpoints

### Course Model

```bashUygulamayı durdurmak için: **Ctrl+C**

```python

from src.models import Course### Students



# Query all courses- `GET /api/students` - Get all studentsexport DB_USER=your_username

with db.session_scope() as session:

    courses = session.query(Course).all()- `POST /api/students` - Create a new student

    for course in courses:

        print(f"{course.course_name}")- `GET /api/students/<id>` - Get a specific studentexport DB_PASSWORD=your_password## 📊 Veritabanı Şeması

```

- `PUT /api/students/<id>` - Update a student

### Enrollment Model

- `DELETE /api/students/<id>` - Delete a studentexport DB_HOST=your_host

```python

from src.models import Enrollment



# Query all enrollments### Instructorsexport DB_PORT=your_port### Tablolar

with db.session_scope() as session:

    enrollments = session.query(Enrollment).all()- `GET /api/instructors` - Get all instructors

    for enrollment in enrollments:

        print(f"{enrollment.student_id} enrolled in {enrollment.course_id}")- `POST /api/instructors` - Create a new instructorexport DB_NAME=your_database_name- **student**: Öğrenci bilgileri

```

- `GET /api/instructors/<id>` - Get a specific instructor

## 🧪 Service Layer Examples

- `PUT /api/instructors/<id>` - Update an instructor```- **instructor**: Öğretim görevlisi bilgileri

### StudentService

- `DELETE /api/instructors/<id>` - Delete an instructor

Performs student management operations:

- `create_student(fname, lname, department)` - Add new student- **course**: Ders bilgileri

- `update_student(student_id, fname, lname, department)` - Update student

- `delete_student(student_id)` - Delete student### Courses

- `get_student(student_id)` - Get specific student

- `get_all_students()` - Get all students- `GET /api/courses` - Get all courses### 5. Uygulamayı Çalıştır- **enrollment**: Öğrenci-Ders kayıt bilgileri

- `get_students_by_department(department)` - Get students by department

- `POST /api/courses` - Create a new course

### InstructorService

- `GET /api/courses/<id>` - Get a specific course```bash

Performs instructor management operations:

- `create_instructor(fname, lname, department)` - Add new instructor- `PUT /api/courses/<id>` - Update a course

- `update_instructor(instructor_id, fname, lname, department)` - Update instructor

- `delete_instructor(instructor_id)` - Delete instructor- `DELETE /api/courses/<id>` - Delete a coursepython3 app.py### İlişkiler

- `get_instructor(instructor_id)` - Get specific instructor

- `get_all_instructors()` - Get all instructors

- `get_instructors_by_department(department)` - Get instructors by department

### Enrollments```- Bir Instructor birden fazla Course'a sahip olabilir

### CourseService

- `POST /api/enrollments` - Enroll a student in a course

Performs course management operations:

- `create_course(course_name, instructor_id)` - Add new course- `POST /api/enrollments/drop` - Drop a student from a course- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)

- `update_course(course_id, course_name, instructor_id)` - Update course

- `delete_course(course_id)` - Delete course- `POST /api/enrollments/grade` - Assign a grade to an enrollment

- `get_course(course_id)` - Get specific course

- `get_all_courses()` - Get all courses- `GET /api/enrollments/student/<id>` - Get courses for a student## 📊 Veritabanı Şeması

- `get_instructor_courses(instructor_id)` - Get courses by instructor

- `GET /api/enrollments/course/<id>` - Get students in a course

### EnrollmentService

## 🔧 ORM Modelleri

Manages course enrollment operations:

- `enroll_student(student_id, course_id)` - Enroll student in course### Reports

- `drop_course(student_id, course_id)` - Drop student from course

- `assign_grade(student_id, course_id, grade)` - Assign grade (AA, BA, BB, CB, CC, DC, DD, FD, FF)- `GET /api/reports/students-per-course/<id>` - Students in a course### Tablolar

- `get_student_courses(student_id)` - Get student's courses

- `get_course_students(course_id)` - Get course's students- `GET /api/reports/courses-per-student/<id>` - Courses for a student

- `get_enrollment_info(enrollment_id)` - Get enrollment details

- `GET /api/reports/instructor-workload` - Instructor workload### Student

### ReportService

- `GET /api/reports/department-statistics` - Department statistics

Performs reporting and analysis operations:

- `get_students_per_course(course_id)` - List students enrolled in a course- `GET /api/reports/grade-distribution/<id>` - Grade distribution#### Student (Öğrenci)```python

- `get_courses_per_student(student_id)` - List student's courses

- `get_instructor_workload()` - Get instructors' teaching load

- `get_department_statistics()` - Get department statistics

- `get_grade_distribution(course_id)` - Get grade distribution in a course## 📊 Database Schema```sqlfrom src.models import Student



## 💡 Usage Examples



### Example 1: Add New Student### Student TableCREATE TABLE student (

```python

from src.config.database import DatabaseManager| Column | Type | Constraint |

from src.resources import StudentResource

|--------|------|-----------|    student_id SERIAL PRIMARY KEY,# Öğrencileri sorgula

db = DatabaseManager()

db.connect()| student_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |



student_resource = StudentResource(db)| fname | VARCHAR(100) | NOT NULL |    fname VARCHAR(50),with db.session_scope() as session:

result = student_resource.create_student('Ali', 'Demir', 'Computer Engineering')

| lname | VARCHAR(100) | NOT NULL |

print(result['message'])  # Student successfully added (ID: 11)

db.disconnect()| department | VARCHAR(100) | NOT NULL |    lname VARCHAR(50),    students = session.query(Student).all()

```



### Example 2: Enroll Student in Course

```python### Instructor Table    department VARCHAR(50)```

from src.config.database import DatabaseManager

from src.resources import EnrollmentResource| Column | Type | Constraint |



db = DatabaseManager()|--------|------|-----------|);

db.connect()

| instructor_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |

enrollment_resource = EnrollmentResource(db)

result = enrollment_resource.enroll_student(student_id=1, course_id=1)| fname | VARCHAR(100) | NOT NULL |```### Instructor



print(result['message'])  # Student successfully enrolled| lname | VARCHAR(100) | NOT NULL |

db.disconnect()

```| department | VARCHAR(100) | NOT NULL |```python



### Example 3: Assign Grade

```python

result = enrollment_resource.assign_grade(student_id=1, course_id=1, grade='AA')### Course Table#### Instructor (Öğretim Görevlisi)from src.models import Instructor

print(result['message'])  # Grade successfully assigned

```| Column | Type | Constraint |



### Example 4: List Student's Courses|--------|------|-----------|```sql

```python

from src.resources import ReportResource| course_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |



report_resource = ReportResource(db)| course_name | VARCHAR(150) | NOT NULL |CREATE TABLE instructor (# Öğretim görevlilerini sorgula

result = report_resource.get_courses_per_student(student_id=1)

| instructor_id | INTEGER | FOREIGN KEY |

print(result['message'])  # Student enrolled in 3 courses

for course in result['data']['courses']:    instructor_id SERIAL PRIMARY KEY,with db.session_scope() as session:

    print(f"  - {course['course_name']}: {course['grade']}")

```### Enrollment Table



### Example 5: Get Course Statistics| Column | Type | Constraint |    fname VARCHAR(50),    instructors = session.query(Instructor).all()

```python

result = report_resource.get_students_per_course(course_id=1)|--------|------|-----------|

print(result['message'])  # X students enrolled in Database Systems

| student_id | INTEGER | FOREIGN KEY, PRIMARY KEY (part) |    lname VARCHAR(50),```

for student in result['data']['students']:

    print(f"  - {student['name']}: {student['grade']}")| course_id | INTEGER | FOREIGN KEY, PRIMARY KEY (part) |

```

| grade | VARCHAR(2) | NULLABLE |    department VARCHAR(50)

### Example 6: Get Instructor Workload

```python

result = report_resource.get_instructor_workload()

## 🎨 UI Features);### Course

for workload in result['data']:

    print(f"{workload['name']}: {workload['total_courses']} courses, {workload['total_students']} students")

```

- **Responsive Design** - Works on desktop, tablet, and mobile``````python

## 🎨 UI Features

- **Modern Gradient Theme** - Purple to blue gradient background

- **Responsive Design** - Works on desktop, tablet, and mobile

- **Modern Gradient Theme** - Purple to blue gradient background- **Tab Navigation** - Easy switching between featuresfrom src.models import Course

- **Tab Navigation** - Easy switching between features

- **Real-time Validation** - Input validation with error messages- **Real-time Validation** - Input validation with error messages

- **Success/Error Notifications** - Clear feedback on operations

- **Dark Text on Light Background** - Optimal readability- **Success/Error Notifications** - Clear feedback on operations#### Course (Ders)

- **Smooth Animations** - Professional transitions and effects

- **English Interface** - Fully internationalized UI- **Dark Text on Light Background** - Optimal readability



## 📝 Sample Data- **Smooth Animations** - Professional transitions and effects```sql# Dersleri sorgula



The system includes sample data in the database for testing:- **English Interface** - Fully internationalized UI



```sqlCREATE TABLE course (with db.session_scope() as session:

-- Sample Students

INSERT INTO student (fname, lname, department) ## 📝 Sample Data

VALUES ('Merve', 'Karatas', 'Computer Engineering');

    course_id SERIAL PRIMARY KEY,    courses = session.query(Course).all()

INSERT INTO student (fname, lname, department) 

VALUES ('Kevser', 'Kutlu', 'Software Engineering');The system includes sample data in the database for testing:



-- Sample Instructors    course_name VARCHAR(100),```

INSERT INTO instructor (fname, lname, department) 

VALUES ('Dr. Jane', 'Smith', 'Computer Science');```sql



INSERT INTO instructor (fname, lname, department) -- Sample Students    instructor_id INT REFERENCES instructor(instructor_id)

VALUES ('Prof. John', 'Doe', 'Engineering');

INSERT INTO students (fname, lname, department) 

-- Sample Courses

INSERT INTO course (course_name, instructor_id) VALUES ('John', 'Doe', 'Computer Science'););### Enrollment

VALUES ('Database Systems', 1);



INSERT INTO course (course_name, instructor_id) 

VALUES ('Web Development', 2);-- Sample Instructors``````python



-- Sample EnrollmentsINSERT INTO instructors (fname, lname, department) 

INSERT INTO enrollment (student_id, course_id, grade) 

VALUES (1, 1, 'AA');VALUES ('Dr. Jane', 'Smith', 'Computer Science');from src.models import Enrollment



INSERT INTO enrollment (student_id, course_id, grade) 

VALUES (2, 2, 'BA');

```-- Sample Courses#### Enrollment (Kayıt)



## 🧪 Manual Schema LoadingINSERT INTO courses (course_name, instructor_id) 



To load the SQL schema directly:VALUES ('Database Systems', 1);```sql# Kayıtları sorgula



```bash

psql -U postgres -h localhost -d course_registration -f database/schema.sql

```-- Sample EnrollmentsCREATE TABLE enrollment (with db.session_scope() as session:



## 🐛 TroubleshootingINSERT INTO enrollments (student_id, course_id, grade) 



### PostgreSQL Connection ErrorVALUES (1, 1, 'AA');    enrollment_id SERIAL PRIMARY KEY,    enrollments = session.query(Enrollment).all()



Error: "could not connect to database"```



**Solution**: Make sure PostgreSQL is running    student_id INT REFERENCES student(student_id),```



```bash## 🐛 Troubleshooting

# macOS with Homebrew

brew services start postgresql    course_id INT REFERENCES course(course_id),



# Linux### PostgreSQL Connection Error

sudo systemctl start postgresql

```    grade VARCHAR(2)## � Örnek Kullanım

# Windows

# Start PostgreSQL from Services or use pgAdminError: "could not connect to database"

```

```);

### Port 5001 Already in Use

**Solution**: Make sure PostgreSQL is running

The application uses port 5001 by default. If it's in use:

```bash``````python

```bash

# macOS/Linux - Find and kill the process# macOS with Homebrew

lsof -i :5001

kill -9 <PID>brew services start postgresqlfrom src.config.database import DatabaseManager



# Windows - Use Task Manager or PowerShell

netstat -ano | findstr :5001

taskkill /PID <PID> /F# Linux### İlişkilerfrom src.models import Student, Course, Enrollment

```

sudo systemctl start postgresql

### Module Not Found Error

- Bir Instructor birden fazla Course'a sahip olabilir

Ensure all dependencies are installed:

# Windows

```bash

pip install -r requirements.txt# Start PostgreSQL from Services or use pgAdmin- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)# Veritabanına bağlan

```

```

### Virtual Environment Issues

- Enrollment tablosu Student ve Course arasında Many-to-Many ilişki sağlardb = DatabaseManager()

If the virtual environment is corrupted:

### Port 5001 Already in Use

```bash

rm -rf .venv  # macOS/LinuxThe application uses port 5001 by default. If it's in use:db.connect()

rmdir /s .venv  # Windows

```bash

python3 -m venv .venv

source .venv/bin/activate  # macOS/Linux# macOS/Linux - Find and kill the process## 🔧 Servis Katmanı (Services)

# or

.venv\Scripts\activate  # Windowslsof -i :5001



pip install -r requirements.txtkill -9 <PID># Tüm öğrencileri listele

```



### Flask Application Not Starting

# Windows - Use Task Manager or PowerShell### StudentServicewith db.session_scope() as session:

If `python3 web.py` doesn't work:

netstat -ano | findstr :5001

```bash

# Check Python versiontaskkill /PID <PID> /FÖğrenci yönetimi işlemlerini gerçekleştirir:    students = session.query(Student).all()

python3 --version  # Should be 3.11 or higher

```

# Use the startup script instead

./run.sh  # macOS/Linux- `create_student(fname, lname, department)` - Yeni öğrenci ekle    for student in students:

run.bat   # Windows

```### Module Not Found Error



## 📄 LicenseEnsure all dependencies are installed:- `update_student(student_id, fname, lname, department)` - Öğrenci güncelle        print(f"{student.fname} {student.lname}")



This project is developed for CPE312 Database Systems course at the university.```bash



## 📞 Supportpip install -r requirements.txt- `delete_student(student_id)` - Öğrenci sil



For issues or questions, please contact the development team:```



- Merve Karataş (64220045)- `get_student(student_id)` - Tek öğrenci getir# Yeni öğrenci ekle

- Kevser Kutlu (64220018)

- Arife Zeynep Muratoğlu (64220048)### Virtual Environment Issues



---If the virtual environment is corrupted:- `get_all_students()` - Tüm öğrencileri listelewith db.session_scope() as session:



**Version**: 1.0.0  ```bash

**Last Updated**: January 27, 2026  

**Status**: ✅ Production Readyrm -rf .venv  # macOS/Linux- `get_students_by_department(department)` - Bölüme göre listele    new_student = Student(


python3 -m venv .venv

source .venv/bin/activate        fname="Ali",

pip install -r requirements.txt

```### InstructorService        lname="Demir",



## 📄 LicenseÖğretim görevlisi yönetimi işlemlerini gerçekleştirir:        department="Computer Engineering"



This project is developed for CPE312 Database Systems course at the university.- `create_instructor(fname, lname, department)` - Yeni öğretim görevlisi ekle    )



## 📞 Support- `update_instructor(instructor_id, fname, lname, department)` - Güncelle    session.add(new_student)



For issues or questions, please contact the development team:- `delete_instructor(instructor_id)` - Sil

- Merve Karataş (64220045)

- Kevser Kutlu (64220018)- `get_instructor(instructor_id)` - Getir# Bağlantıyı kapat

- Arife Zeynep Muratoğlu (64220048)

- `get_all_instructors()` - Tüm öğretim görevlilerini listeledb.disconnect()

---

- `get_instructors_by_department(department)` - Bölüme göre listele```

**Version**: 1.0.0  

**Last Updated**: January 27, 2026  

**Status**: ✅ Production Ready

### CourseService## 🧪 SQL Şemasını Manuel Olarak Yükleme

Ders yönetimi işlemlerini gerçekleştirir:

- `create_course(course_name, instructor_id)` - Yeni ders ekleSQL dosyasını doğrudan çalıştırmak istersen:

- `update_course(course_id, course_name, instructor_id)` - Ders güncelle

- `delete_course(course_id)` - Ders sil```bash

- `get_course(course_id)` - Tek ders getirpsql -U postgres -h localhost -d course_registration -f database/schema.sql

- `get_all_courses()` - Tüm dersleri listele```

- `get_instructor_courses(instructor_id)` - Öğretim görevlisinin derslerini listele

## 📅 Önemli Tarihler

### EnrollmentService* **Teslim Tarihi:** 28.01.2026 - 17:00

Ders kayıt işlemlerini yönetir:

- `enroll_student(student_id, course_id)` - Öğrenciyi derse kaydet## 📄 Lisans

- `drop_course(student_id, course_id)` - Öğrenciyi dersten çıkarBu proje CPE312 dersi kapsamında hazırlanmıştır.

- `assign_grade(student_id, course_id, grade)` - Not ver (AA, BA, BB, CB, CC, DC, DD, FD, FF)

- `get_student_courses(student_id)` - Öğrencinin derslerini listele## 📞 İletişim

- `get_course_students(course_id)` - Dersin öğrencilerini listeleSorularınız için lütfen proje ekibine ulaşın.
- `get_enrollment_info(enrollment_id)` - Kayıt detaylarını getir

### ReportService
Raporlama ve analiz işlemlerini gerçekleştirir:
- `get_students_per_course(course_id)` - Derse kayıtlı öğrencileri listele
- `get_courses_per_student(student_id)` - Öğrencinin derslerini listele
- `get_instructor_workload()` - Öğretim görevlilerinin ders yükü
- `get_department_statistics()` - Bölüm istatistikleri
- `get_grade_distribution(course_id)` - Derste verilen notların dağılımı

## 💡 Kullanım Örnekleri

### Örnek 1: Yeni Öğrenci Ekle
```python
from src.config.database import DatabaseManager
from src.resources import StudentResource

db = DatabaseManager()
db.connect()

student_resource = StudentResource(db)
result = student_resource.create_student('Ali', 'Demir', 'Computer Engineering')

print(result['message'])  # Ali Demir başarıyla eklendi (ID: 11)
db.disconnect()
```

### Örnek 2: Öğrenciyi Derse Kaydet
```python
from src.config.database import DatabaseManager
from src.resources import EnrollmentResource

db = DatabaseManager()
db.connect()

enrollment_resource = EnrollmentResource(db)
result = enrollment_resource.enroll_student(student_id=1, course_id=1)

print(result['message'])  # Öğrenci başarıyla derse kaydedildi
db.disconnect()
```

### Örnek 3: Not Ver
```python
result = enrollment_resource.assign_grade(student_id=1, course_id=1, grade='AA')
print(result['message'])  # Merve Karatas için Database Systems notı AA -> AA olarak güncellendi
```

### Örnek 4: Öğrencinin Derslerini Listele
```python
from src.resources import ReportResource

report_resource = ReportResource(db)
result = report_resource.get_courses_per_student(student_id=1)

print(result['message'])  # Merve Karatas 3 derse kayıtlı
for course in result['data']['courses']:
    print(f"  - {course['course_name']}: {course['grade']}")
```

### Örnek 5: Ders İstatistikleri
```python
result = report_resource.get_students_per_course(course_id=1)
print(result['message'])  # Database Systems dersine X öğrenci kayıtlı

for student in result['data']['students']:
    print(f"  - {student['name']}: {student['grade']}")
```

### Örnek 6: Öğretim Görevlisi İş Yükü
```python
result = report_resource.get_instructor_workload()

for workload in result['data']:
    print(f"{workload['name']}: {workload['total_courses']} ders, {workload['total_students']} öğrenci")
```

## 🧪 SQL Şemasını Manuel Olarak Yükleme

SQL dosyasını doğrudan çalıştırmak istersen:

```bash
psql -U postgres -h localhost -d course_registration -f database/schema.sql
```

## 📝 Hata Yönetimi

Tüm servisler yapılandırılmış sonuç döner:

```python
{
    'success': True/False,
    'message': 'Açıklayıcı mesaj',
    'data': {} veya []  # İlgili veri (varsa)
}
```

Örneğin:
```python
result = student_resource.get_student(999)  # Var olmayan öğrenci
print(result['success'])  # False
print(result['message'])  # Öğrenci ID 999 bulunamadı
```

## 📅 Önemli Tarihler
* **Teslim Tarihi:** 28.01.2026 - 17:00

## 📄 Lisans
Bu proje CPE312 dersi kapsamında hazırlanmıştır.

## 📞 İletişim
Sorularınız için lütfen proje ekibine ulaşın.
