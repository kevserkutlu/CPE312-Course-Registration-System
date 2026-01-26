# 🎓 Course Registration System - CPE312# 🎓 Course Registration System - CPE312# 🎓 Course Registration System - CPE312



A comprehensive fullstack university course management system with modern web UI, built with Flask backend and PostgreSQL database.



## 📋 System FeaturesBu proje, üniversite ortamında ders kayıt süreçlerini yönetmek için geliştirilmiş bir veritabanı yönetim sistemidir. Sistem öğrenciler, öğretim görevlileri, dersler ve kayıtların yönetimini sağlar.Bu proje, üniversite ortamında ders kayıt süreçlerini yönetmek için geliştirilmiş bir veritabanı yönetim sistemidir.



### ✅ Core Functionality



- **👥 Student Management** - Add, update, delete, and list students## 📋 Sistem Özellikleri## 👥 Proje Ekibi

- **👨‍🏫 Instructor Management** - Add, update, delete, and list instructors  

- **📖 Course Management** - Add, update, delete, and list courses* **Merve Karataş** - 64220045

- **📋 Enrollment Management** - Register students, drop courses, assign grades

- **📊 Reporting & Analytics** - Five different report types with detailed statistics### ✅ Yapılan İşlemler* **Kevser Kutlu** - 64220018

- **⚠️ Error Handling & Validation** - Comprehensive validation on all operations

- **✓ Öğrenci Yönetimi** - Ekle, güncelle, sil, listele* **Arife Zeynep Muratoğlu** - 64220048

### 📊 Available Reports

- **✓ Öğretim Görevlisi Yönetimi** - Ekle, güncelle, sil, listele

1. **Students Enrolled in Course** - View all students in a specific course with grades

2. **Student Course List** - View all courses a student is enrolled in- **✓ Ders Yönetimi** - Ekle, güncelle, sil, listele## 📂 Proje Yapısı

3. **Instructor Workload** - See workload distribution across all instructors

4. **Department Statistics** - View student and instructor counts per department- **✓ Ders Kayıt İşlemleri** - Kaydet, çıkar, not ver```

5. **Grade Distribution** - Analyze grade distribution in a course

- **✓ Raporlama ve Analitiği** - İstatistikler ve detaylı raporlarCPE312-Course-Registration-System/

## 👥 Project Team

- **✓ Hata Yönetimi ve Validasyon** - Tüm operasyonlarda├── database/

* **Merve Karataş** - 64220045

* **Kevser Kutlu** - 64220018│   └── schema.sql              # Veritabanı şeması ve örnek veriler

* **Arife Zeynep Muratoğlu** - 64220048

## 👥 Proje Ekibi├── docs/

## 📂 Project Structure

* **Merve Karataş** - 64220045│   └── Course Registration System_Proposal.pdf

```

CPE312-Course-Registration-System/* **Kevser Kutlu** - 64220018├── src/

├── database/

│   └── schema.sql                      # Database schema and sample data* **Arife Zeynep Muratoğlu** - 64220048│   ├── app.py                  # Ana uygulama

├── docs/

│   └── Course Registration System_Proposal.pdf│   ├── models.py               # SQLAlchemy ORM modelleri

├── src/

│   ├── app.py                          # Legacy app entry point## 📂 Proje Yapısı│   ├── config/

│   ├── models.py                       # SQLAlchemy ORM models

│   ├── config/│   │   └── database/

│   │   └── database/

│   │       ├── __init__.py```│   │       ├── __init__.py

│   │       └── db.py                   # Database connection management

│   ├── services/                       # Business logic layerCPE312-Course-Registration-System/│   │       └── db.py           # Veritabanı bağlantı yönetimi

│   │   ├── student_service.py

│   │   ├── instructor_service.py├── database/│   └── README.md

│   │   ├── course_service.py

│   │   ├── enrollment_service.py│   └── schema.sql                      # Veritabanı şeması ve örnek veriler├── requirements.txt            # Python bağımlılıkları

│   │   └── report_service.py

│   ├── resources/                      # API layer├── docs/├── .gitignore

│   │   ├── student_resource.py

│   │   ├── instructor_resource.py│   └── Course Registration System_Proposal.pdf└── README.md

│   │   ├── course_resource.py

│   │   ├── enrollment_resource.py├── src/```

│   │   └── report_resource.py

│   └── __init__.py│   ├── app.py                          # Ana uygulama (örnek kullanım)

├── templates/

│   └── index.html                      # Main web interface│   ├── models.py                       # SQLAlchemy ORM modelleri## 🛠️ Teknolojiler

├── static/

│   ├── style.css                       # Responsive styling│   ├── config/* **Database:** PostgreSQL

│   └── script.js                       # Frontend JavaScript

├── web.py                              # Flask web application│   │   └── database/* **Language:** Python 3.11+

├── requirements.txt                    # Python dependencies

├── run.sh                              # macOS/Linux startup script│   │       ├── __init__.py* **ORM:** SQLAlchemy 2.0.45

├── run.bat                             # Windows startup script

└── README.md                           # This file│   │       └── db.py                   # Veritabanı bağlantı yönetimi* **Database Driver:** psycopg2-binary

```

│   ├── services/                       # İş mantığı katmanı

## 🛠️ Technology Stack

│   │   ├── __init__.py## 📋 Gereksinimler

| Component | Technology |

|-----------|-----------|│   │   ├── enrollment_service.py       # Kayıt işlemleri* Python 3.11 veya daha yüksek

| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |

| **Backend** | Python 3.11+, Flask |│   │   ├── student_service.py          # Öğrenci CRUD* PostgreSQL 12 veya daha yüksek

| **ORM** | SQLAlchemy 2.0.45 |

| **Database** | PostgreSQL |│   │   ├── instructor_service.py       # Öğretim görevlisi CRUD* pip (Python paket yöneticisi)

| **Architecture** | Service-Resource Pattern (3-layer architecture) |

│   │   ├── course_service.py           # Ders CRUD

## 📦 Installation

│   │   └── report_service.py           # Raporlama## 🚀 Kurulum ve Çalıştırma

### Prerequisites

│   ├── resources/                      # API katmanı

- **Python 3.11+** installed

- **PostgreSQL** installed and running│   │   ├── __init__.py### 1. Projeyi Klonla

- **pip** (Python package manager)

│   │   ├── enrollment_resource.py```bash

### Quick Start (Recommended)

│   │   ├── student_resource.pygit clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git

#### macOS / Linux:

│   │   ├── instructor_resource.pycd CPE312-Course-Registration-System

```bash

cd CPE312-Course-Registration-System│   │   ├── course_resource.py```

chmod +x run.sh

./run.sh│   │   └── report_resource.py

```

│   └── README.md### 2. Sanal Ortam Oluştur (Python Virtual Environment)

#### Windows:

├── requirements.txt                    # Python bağımlılıkları```bash

```cmd

cd CPE312-Course-Registration-System├── .gitignore# macOS / Linux

run.bat

```└── README.mdpython3 -m venv .venv



### Manual Setup```source .venv/bin/activate



1. **Clone the repository:**

```bash

git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git## 🛠️ Teknolojiler# Windows

cd CPE312-Course-Registration-System

```* **Database:** PostgreSQLpython -m venv .venv



2. **Create virtual environment:*** **Language:** Python 3.11+.venv\Scripts\activate

```bash

python3 -m venv .venv* **ORM:** SQLAlchemy 2.0.45```

source .venv/bin/activate  # macOS/Linux

# or* **Database Driver:** psycopg2-binary

.venv\Scripts\activate  # Windows

```### 3. Bağımlılıkları Yükle



3. **Install dependencies:**## 📋 Gereksinimler```bash

```bash

pip install -r requirements.txt* Python 3.11 veya daha yüksekpip install -r requirements.txt

```

* PostgreSQL 12 veya daha yüksek```

4. **Run the application:**

```bash* pip (Python paket yöneticisi)

python3 web.py

```### 4. Veritabanı Konfigürasyonu



5. **Open in browser:**## 🚀 Kurulum ve ÇalıştırmaPostgreSQL'de `course_registration` adında bir veritabanı oluştur:

```

http://localhost:5001

```

### 1. Projeyi Klonla```sql

## 🚀 How to Use

```bashCREATE DATABASE course_registration;

### 1. **Students Tab**

- **Add Student**: Fill in first name, last name, and department, then click "Add"git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git```

- **List Students**: Click "Load" to see all students with delete options

cd CPE312-Course-Registration-System

### 2. **Instructors Tab**

- **Add Instructor**: Fill in first name, last name, and department, then click "Add"```**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:

- **List Instructors**: Click "Load" to see all instructors

- Kullanıcı: `postgres`

### 3. **Courses Tab**

- **Add Course**: Enter course name and instructor ID, then click "Add"### 2. Sanal Ortam Oluştur (Python Virtual Environment)- Şifre: `kvyu8dutx`

- **List Courses**: Click "Load" to see all courses

```bash- Host: `127.0.0.1`

### 4. **Enrollments Tab**

- **Enroll Student**: Enter student ID and course ID, click "Enroll"# macOS / Linux- Port: `5432`

- **Drop Course**: Enter student ID and course ID, click "Drop"

- **Assign Grade**: Enter student and course IDs, select a grade, click "Assign"python3 -m venv .venv- Veritabanı: `postgres`

- **View Courses**: Enter student ID to see their enrolled courses

source .venv/bin/activate

### 5. **Reports Tab**

- **Students per Course**: View all students in a specific courseEğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:

- **Courses per Student**: View all courses a student is enrolled in

- **Instructor Workload**: See all instructors and their teaching load# Windows```bash

- **Department Statistics**: View statistics by department

- **Grade Distribution**: Analyze grade distribution in a coursepython -m venv .venvexport DB_USER=your_username



## 🏗️ Architecture.venv\Scripts\activateexport DB_PASSWORD=your_password



### Service-Resource Pattern (3-Layer Architecture)```export DB_HOST=your_host



```export DB_PORT=your_port

┌─────────────────────────────────────────┐

│         Web Interface (HTML/CSS/JS)     │### 3. Bağımlılıkları Yükleexport DB_NAME=your_database_name

│           (Presentation Layer)          │

└────────────────────────────────────────┘```bash```

                    ↓

┌─────────────────────────────────────────┐pip install -r requirements.txt

│      Flask Routes & Resources           │

│           (API Layer)                   │```### 5. Uygulamayı Çalıştır

│  - StudentResource                      │

│  - InstructorResource                   │```bash

│  - CourseResource                       │

│  - EnrollmentResource                   │### 4. Veritabanı Konfigürasyonupython3 app.py

│  - ReportResource                       │

└────────────────────────────────────────┘PostgreSQL'de `course_registration` adında bir veritabanı oluştur:```

                    ↓

┌─────────────────────────────────────────┐

│         Services (Business Logic)       │

│           (Service Layer)               │```sql**Çıktı:**

│  - StudentService                       │

│  - InstructorService                    │CREATE DATABASE course_registration;```

│  - CourseService                        │

│  - EnrollmentService                    │```PostgreSQL bağlantısı başarıyla kuruldu! ✅

│  - ReportService                        │

└────────────────────────────────────────┘✓ Tablolar oluşturuldu

                    ↓

┌─────────────────────────────────────────┐**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:Uygulama çalışıyor...

│    SQLAlchemy ORM & Models              │

│           (Data Layer)                  │- Kullanıcı: `postgres`

│  - Student                              │

│  - Instructor                           │- Şifre: `kvyu8dutx`Toplam 10 öğrenci bulundu:

│  - Course                               │

│  - Enrollment                           │- Host: `127.0.0.1`  - Merve Karatas (Computer Engineering)

└────────────────────────────────────────┘

                    ↓- Port: `5432`  - Kevser Kutlu (Software Engineering)

┌─────────────────────────────────────────┐

│          PostgreSQL Database            │- Veritabanı: `postgres`  ...

│        (Persistence Layer)              │

└────────────────────────────────────────┘```

```

Eğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:

## 🔌 API Endpoints

```bashUygulamayı durdurmak için: **Ctrl+C**

### Students

- `GET /api/students` - Get all studentsexport DB_USER=your_username

- `POST /api/students` - Create a new student

- `GET /api/students/<id>` - Get a specific studentexport DB_PASSWORD=your_password## 📊 Veritabanı Şeması

- `PUT /api/students/<id>` - Update a student

- `DELETE /api/students/<id>` - Delete a studentexport DB_HOST=your_host



### Instructorsexport DB_PORT=your_port### Tablolar

- `GET /api/instructors` - Get all instructors

- `POST /api/instructors` - Create a new instructorexport DB_NAME=your_database_name- **student**: Öğrenci bilgileri

- `GET /api/instructors/<id>` - Get a specific instructor

- `PUT /api/instructors/<id>` - Update an instructor```- **instructor**: Öğretim görevlisi bilgileri

- `DELETE /api/instructors/<id>` - Delete an instructor

- **course**: Ders bilgileri

### Courses

- `GET /api/courses` - Get all courses### 5. Uygulamayı Çalıştır- **enrollment**: Öğrenci-Ders kayıt bilgileri

- `POST /api/courses` - Create a new course

- `GET /api/courses/<id>` - Get a specific course```bash

- `PUT /api/courses/<id>` - Update a course

- `DELETE /api/courses/<id>` - Delete a coursepython3 app.py### İlişkiler



### Enrollments```- Bir Instructor birden fazla Course'a sahip olabilir

- `POST /api/enrollments` - Enroll a student in a course

- `POST /api/enrollments/drop` - Drop a student from a course- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)

- `POST /api/enrollments/grade` - Assign a grade to an enrollment

- `GET /api/enrollments/student/<id>` - Get courses for a student## 📊 Veritabanı Şeması

- `GET /api/enrollments/course/<id>` - Get students in a course

## 🔧 ORM Modelleri

### Reports

- `GET /api/reports/students-per-course/<id>` - Students in a course### Tablolar

- `GET /api/reports/courses-per-student/<id>` - Courses for a student

- `GET /api/reports/instructor-workload` - Instructor workload### Student

- `GET /api/reports/department-statistics` - Department statistics

- `GET /api/reports/grade-distribution/<id>` - Grade distribution#### Student (Öğrenci)```python



## 📊 Database Schema```sqlfrom src.models import Student



### Student TableCREATE TABLE student (

| Column | Type | Constraint |

|--------|------|-----------|    student_id SERIAL PRIMARY KEY,# Öğrencileri sorgula

| student_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |

| fname | VARCHAR(100) | NOT NULL |    fname VARCHAR(50),with db.session_scope() as session:

| lname | VARCHAR(100) | NOT NULL |

| department | VARCHAR(100) | NOT NULL |    lname VARCHAR(50),    students = session.query(Student).all()



### Instructor Table    department VARCHAR(50)```

| Column | Type | Constraint |

|--------|------|-----------|);

| instructor_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |

| fname | VARCHAR(100) | NOT NULL |```### Instructor

| lname | VARCHAR(100) | NOT NULL |

| department | VARCHAR(100) | NOT NULL |```python



### Course Table#### Instructor (Öğretim Görevlisi)from src.models import Instructor

| Column | Type | Constraint |

|--------|------|-----------|```sql

| course_id | INTEGER | PRIMARY KEY, AUTO_INCREMENT |

| course_name | VARCHAR(150) | NOT NULL |CREATE TABLE instructor (# Öğretim görevlilerini sorgula

| instructor_id | INTEGER | FOREIGN KEY |

    instructor_id SERIAL PRIMARY KEY,with db.session_scope() as session:

### Enrollment Table

| Column | Type | Constraint |    fname VARCHAR(50),    instructors = session.query(Instructor).all()

|--------|------|-----------|

| student_id | INTEGER | FOREIGN KEY, PRIMARY KEY (part) |    lname VARCHAR(50),```

| course_id | INTEGER | FOREIGN KEY, PRIMARY KEY (part) |

| grade | VARCHAR(2) | NULLABLE |    department VARCHAR(50)



## 🎨 UI Features);### Course



- **Responsive Design** - Works on desktop, tablet, and mobile``````python

- **Modern Gradient Theme** - Purple to blue gradient background

- **Tab Navigation** - Easy switching between featuresfrom src.models import Course

- **Real-time Validation** - Input validation with error messages

- **Success/Error Notifications** - Clear feedback on operations#### Course (Ders)

- **Dark Text on Light Background** - Optimal readability

- **Smooth Animations** - Professional transitions and effects```sql# Dersleri sorgula

- **English Interface** - Fully internationalized UI

CREATE TABLE course (with db.session_scope() as session:

## 📝 Sample Data

    course_id SERIAL PRIMARY KEY,    courses = session.query(Course).all()

The system includes sample data in the database for testing:

    course_name VARCHAR(100),```

```sql

-- Sample Students    instructor_id INT REFERENCES instructor(instructor_id)

INSERT INTO students (fname, lname, department) 

VALUES ('John', 'Doe', 'Computer Science'););### Enrollment



-- Sample Instructors``````python

INSERT INTO instructors (fname, lname, department) 

VALUES ('Dr. Jane', 'Smith', 'Computer Science');from src.models import Enrollment



-- Sample Courses#### Enrollment (Kayıt)

INSERT INTO courses (course_name, instructor_id) 

VALUES ('Database Systems', 1);```sql# Kayıtları sorgula



-- Sample EnrollmentsCREATE TABLE enrollment (with db.session_scope() as session:

INSERT INTO enrollments (student_id, course_id, grade) 

VALUES (1, 1, 'AA');    enrollment_id SERIAL PRIMARY KEY,    enrollments = session.query(Enrollment).all()

```

    student_id INT REFERENCES student(student_id),```

## 🐛 Troubleshooting

    course_id INT REFERENCES course(course_id),

### PostgreSQL Connection Error

```    grade VARCHAR(2)## � Örnek Kullanım

Error: "could not connect to database"

```);

**Solution**: Make sure PostgreSQL is running

```bash``````python

# macOS with Homebrew

brew services start postgresqlfrom src.config.database import DatabaseManager



# Linux### İlişkilerfrom src.models import Student, Course, Enrollment

sudo systemctl start postgresql

- Bir Instructor birden fazla Course'a sahip olabilir

# Windows

# Start PostgreSQL from Services or use pgAdmin- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)# Veritabanına bağlan

```

- Enrollment tablosu Student ve Course arasında Many-to-Many ilişki sağlardb = DatabaseManager()

### Port 5001 Already in Use

The application uses port 5001 by default. If it's in use:db.connect()

```bash

# macOS/Linux - Find and kill the process## 🔧 Servis Katmanı (Services)

lsof -i :5001

kill -9 <PID># Tüm öğrencileri listele



# Windows - Use Task Manager or PowerShell### StudentServicewith db.session_scope() as session:

netstat -ano | findstr :5001

taskkill /PID <PID> /FÖğrenci yönetimi işlemlerini gerçekleştirir:    students = session.query(Student).all()

```

- `create_student(fname, lname, department)` - Yeni öğrenci ekle    for student in students:

### Module Not Found Error

Ensure all dependencies are installed:- `update_student(student_id, fname, lname, department)` - Öğrenci güncelle        print(f"{student.fname} {student.lname}")

```bash

pip install -r requirements.txt- `delete_student(student_id)` - Öğrenci sil

```

- `get_student(student_id)` - Tek öğrenci getir# Yeni öğrenci ekle

### Virtual Environment Issues

If the virtual environment is corrupted:- `get_all_students()` - Tüm öğrencileri listelewith db.session_scope() as session:

```bash

rm -rf .venv  # macOS/Linux- `get_students_by_department(department)` - Bölüme göre listele    new_student = Student(

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
