# 🎓 Course Registration System - CPE312# 🎓 Course Registration System - CPE312



Bu proje, üniversite ortamında ders kayıt süreçlerini yönetmek için geliştirilmiş bir veritabanı yönetim sistemidir. Sistem öğrenciler, öğretim görevlileri, dersler ve kayıtların yönetimini sağlar.Bu proje, üniversite ortamında ders kayıt süreçlerini yönetmek için geliştirilmiş bir veritabanı yönetim sistemidir.



## 📋 Sistem Özellikleri## 👥 Proje Ekibi

* **Merve Karataş** - 64220045

### ✅ Yapılan İşlemler* **Kevser Kutlu** - 64220018

- **✓ Öğrenci Yönetimi** - Ekle, güncelle, sil, listele* **Arife Zeynep Muratoğlu** - 64220048

- **✓ Öğretim Görevlisi Yönetimi** - Ekle, güncelle, sil, listele

- **✓ Ders Yönetimi** - Ekle, güncelle, sil, listele## 📂 Proje Yapısı

- **✓ Ders Kayıt İşlemleri** - Kaydet, çıkar, not ver```

- **✓ Raporlama ve Analitiği** - İstatistikler ve detaylı raporlarCPE312-Course-Registration-System/

- **✓ Hata Yönetimi ve Validasyon** - Tüm operasyonlarda├── database/

│   └── schema.sql              # Veritabanı şeması ve örnek veriler

## 👥 Proje Ekibi├── docs/

* **Merve Karataş** - 64220045│   └── Course Registration System_Proposal.pdf

* **Kevser Kutlu** - 64220018├── src/

* **Arife Zeynep Muratoğlu** - 64220048│   ├── app.py                  # Ana uygulama

│   ├── models.py               # SQLAlchemy ORM modelleri

## 📂 Proje Yapısı│   ├── config/

│   │   └── database/

```│   │       ├── __init__.py

CPE312-Course-Registration-System/│   │       └── db.py           # Veritabanı bağlantı yönetimi

├── database/│   └── README.md

│   └── schema.sql                      # Veritabanı şeması ve örnek veriler├── requirements.txt            # Python bağımlılıkları

├── docs/├── .gitignore

│   └── Course Registration System_Proposal.pdf└── README.md

├── src/```

│   ├── app.py                          # Ana uygulama (örnek kullanım)

│   ├── models.py                       # SQLAlchemy ORM modelleri## 🛠️ Teknolojiler

│   ├── config/* **Database:** PostgreSQL

│   │   └── database/* **Language:** Python 3.11+

│   │       ├── __init__.py* **ORM:** SQLAlchemy 2.0.45

│   │       └── db.py                   # Veritabanı bağlantı yönetimi* **Database Driver:** psycopg2-binary

│   ├── services/                       # İş mantığı katmanı

│   │   ├── __init__.py## 📋 Gereksinimler

│   │   ├── enrollment_service.py       # Kayıt işlemleri* Python 3.11 veya daha yüksek

│   │   ├── student_service.py          # Öğrenci CRUD* PostgreSQL 12 veya daha yüksek

│   │   ├── instructor_service.py       # Öğretim görevlisi CRUD* pip (Python paket yöneticisi)

│   │   ├── course_service.py           # Ders CRUD

│   │   └── report_service.py           # Raporlama## 🚀 Kurulum ve Çalıştırma

│   ├── resources/                      # API katmanı

│   │   ├── __init__.py### 1. Projeyi Klonla

│   │   ├── enrollment_resource.py```bash

│   │   ├── student_resource.pygit clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git

│   │   ├── instructor_resource.pycd CPE312-Course-Registration-System

│   │   ├── course_resource.py```

│   │   └── report_resource.py

│   └── README.md### 2. Sanal Ortam Oluştur (Python Virtual Environment)

├── requirements.txt                    # Python bağımlılıkları```bash

├── .gitignore# macOS / Linux

└── README.mdpython3 -m venv .venv

```source .venv/bin/activate



## 🛠️ Teknolojiler# Windows

* **Database:** PostgreSQLpython -m venv .venv

* **Language:** Python 3.11+.venv\Scripts\activate

* **ORM:** SQLAlchemy 2.0.45```

* **Database Driver:** psycopg2-binary

### 3. Bağımlılıkları Yükle

## 📋 Gereksinimler```bash

* Python 3.11 veya daha yüksekpip install -r requirements.txt

* PostgreSQL 12 veya daha yüksek```

* pip (Python paket yöneticisi)

### 4. Veritabanı Konfigürasyonu

## 🚀 Kurulum ve ÇalıştırmaPostgreSQL'de `course_registration` adında bir veritabanı oluştur:



### 1. Projeyi Klonla```sql

```bashCREATE DATABASE course_registration;

git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git```

cd CPE312-Course-Registration-System

```**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:

- Kullanıcı: `postgres`

### 2. Sanal Ortam Oluştur (Python Virtual Environment)- Şifre: `kvyu8dutx`

```bash- Host: `127.0.0.1`

# macOS / Linux- Port: `5432`

python3 -m venv .venv- Veritabanı: `postgres`

source .venv/bin/activate

Eğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:

# Windows```bash

python -m venv .venvexport DB_USER=your_username

.venv\Scripts\activateexport DB_PASSWORD=your_password

```export DB_HOST=your_host

export DB_PORT=your_port

### 3. Bağımlılıkları Yükleexport DB_NAME=your_database_name

```bash```

pip install -r requirements.txt

```### 5. Uygulamayı Çalıştır

```bash

### 4. Veritabanı Konfigürasyonupython3 app.py

PostgreSQL'de `course_registration` adında bir veritabanı oluştur:```



```sql**Çıktı:**

CREATE DATABASE course_registration;```

```PostgreSQL bağlantısı başarıyla kuruldu! ✅

✓ Tablolar oluşturuldu

**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:Uygulama çalışıyor...

- Kullanıcı: `postgres`

- Şifre: `kvyu8dutx`Toplam 10 öğrenci bulundu:

- Host: `127.0.0.1`  - Merve Karatas (Computer Engineering)

- Port: `5432`  - Kevser Kutlu (Software Engineering)

- Veritabanı: `postgres`  ...

```

Eğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:

```bashUygulamayı durdurmak için: **Ctrl+C**

export DB_USER=your_username

export DB_PASSWORD=your_password## 📊 Veritabanı Şeması

export DB_HOST=your_host

export DB_PORT=your_port### Tablolar

export DB_NAME=your_database_name- **student**: Öğrenci bilgileri

```- **instructor**: Öğretim görevlisi bilgileri

- **course**: Ders bilgileri

### 5. Uygulamayı Çalıştır- **enrollment**: Öğrenci-Ders kayıt bilgileri

```bash

python3 app.py### İlişkiler

```- Bir Instructor birden fazla Course'a sahip olabilir

- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)

## 📊 Veritabanı Şeması

## 🔧 ORM Modelleri

### Tablolar

### Student

#### Student (Öğrenci)```python

```sqlfrom src.models import Student

CREATE TABLE student (

    student_id SERIAL PRIMARY KEY,# Öğrencileri sorgula

    fname VARCHAR(50),with db.session_scope() as session:

    lname VARCHAR(50),    students = session.query(Student).all()

    department VARCHAR(50)```

);

```### Instructor

```python

#### Instructor (Öğretim Görevlisi)from src.models import Instructor

```sql

CREATE TABLE instructor (# Öğretim görevlilerini sorgula

    instructor_id SERIAL PRIMARY KEY,with db.session_scope() as session:

    fname VARCHAR(50),    instructors = session.query(Instructor).all()

    lname VARCHAR(50),```

    department VARCHAR(50)

);### Course

``````python

from src.models import Course

#### Course (Ders)

```sql# Dersleri sorgula

CREATE TABLE course (with db.session_scope() as session:

    course_id SERIAL PRIMARY KEY,    courses = session.query(Course).all()

    course_name VARCHAR(100),```

    instructor_id INT REFERENCES instructor(instructor_id)

);### Enrollment

``````python

from src.models import Enrollment

#### Enrollment (Kayıt)

```sql# Kayıtları sorgula

CREATE TABLE enrollment (with db.session_scope() as session:

    enrollment_id SERIAL PRIMARY KEY,    enrollments = session.query(Enrollment).all()

    student_id INT REFERENCES student(student_id),```

    course_id INT REFERENCES course(course_id),

    grade VARCHAR(2)## � Örnek Kullanım

);

``````python

from src.config.database import DatabaseManager

### İlişkilerfrom src.models import Student, Course, Enrollment

- Bir Instructor birden fazla Course'a sahip olabilir

- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)# Veritabanına bağlan

- Enrollment tablosu Student ve Course arasında Many-to-Many ilişki sağlardb = DatabaseManager()

db.connect()

## 🔧 Servis Katmanı (Services)

# Tüm öğrencileri listele

### StudentServicewith db.session_scope() as session:

Öğrenci yönetimi işlemlerini gerçekleştirir:    students = session.query(Student).all()

- `create_student(fname, lname, department)` - Yeni öğrenci ekle    for student in students:

- `update_student(student_id, fname, lname, department)` - Öğrenci güncelle        print(f"{student.fname} {student.lname}")

- `delete_student(student_id)` - Öğrenci sil

- `get_student(student_id)` - Tek öğrenci getir# Yeni öğrenci ekle

- `get_all_students()` - Tüm öğrencileri listelewith db.session_scope() as session:

- `get_students_by_department(department)` - Bölüme göre listele    new_student = Student(

        fname="Ali",

### InstructorService        lname="Demir",

Öğretim görevlisi yönetimi işlemlerini gerçekleştirir:        department="Computer Engineering"

- `create_instructor(fname, lname, department)` - Yeni öğretim görevlisi ekle    )

- `update_instructor(instructor_id, fname, lname, department)` - Güncelle    session.add(new_student)

- `delete_instructor(instructor_id)` - Sil

- `get_instructor(instructor_id)` - Getir# Bağlantıyı kapat

- `get_all_instructors()` - Tüm öğretim görevlilerini listeledb.disconnect()

- `get_instructors_by_department(department)` - Bölüme göre listele```



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
