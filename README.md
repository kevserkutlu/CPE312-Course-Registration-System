# 🎓 Course Registration System - CPE312

Bu proje, üniversite ortamında ders kayıt süreçlerini yönetmek için geliştirilmiş bir veritabanı yönetim sistemidir.

## 👥 Proje Ekibi
* **Merve Karataş** - 64220045
* **Kevser Kutlu** - 64220018
* **Arife Zeynep Muratoğlu** - 64220048

## 📂 Proje Yapısı
```
CPE312-Course-Registration-System/
├── database/
│   └── schema.sql              # Veritabanı şeması ve örnek veriler
├── docs/
│   └── Course Registration System_Proposal.pdf
├── src/
│   ├── app.py                  # Ana uygulama
│   ├── models.py               # SQLAlchemy ORM modelleri
│   ├── config/
│   │   └── database/
│   │       ├── __init__.py
│   │       └── db.py           # Veritabanı bağlantı yönetimi
│   └── README.md
├── requirements.txt            # Python bağımlılıkları
├── .gitignore
└── README.md
```

## 🛠️ Teknolojiler
* **Database:** PostgreSQL
* **Language:** Python 3.11+
* **ORM:** SQLAlchemy 2.0.45
* **Database Driver:** psycopg2-binary

## 📋 Gereksinimler
* Python 3.11 veya daha yüksek
* PostgreSQL 12 veya daha yüksek
* pip (Python paket yöneticisi)

## 🚀 Kurulum ve Çalıştırma

### 1. Projeyi Klonla
```bash
git clone https://github.com/kevserkutlu/CPE312-Course-Registration-System.git
cd CPE312-Course-Registration-System
```

### 2. Sanal Ortam Oluştur (Python Virtual Environment)
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 4. Veritabanı Konfigürasyonu
PostgreSQL'de `course_registration` adında bir veritabanı oluştur:

```sql
CREATE DATABASE course_registration;
```

**Not:** `db.py` dosyasında varsayılan bağlantı ayarları:
- Kullanıcı: `postgres`
- Şifre: `kvyu8dutx`
- Host: `127.0.0.1`
- Port: `5432`
- Veritabanı: `postgres`

Eğer farklı ayarlar kullanıyorsan, ortam değişkenlerini ayarla:
```bash
export DB_USER=your_username
export DB_PASSWORD=your_password
export DB_HOST=your_host
export DB_PORT=your_port
export DB_NAME=your_database_name
```

### 5. Uygulamayı Çalıştır
```bash
python3 app.py
```

**Çıktı:**
```
PostgreSQL bağlantısı başarıyla kuruldu! ✅
✓ Tablolar oluşturuldu
Uygulama çalışıyor...

Toplam 10 öğrenci bulundu:
  - Merve Karatas (Computer Engineering)
  - Kevser Kutlu (Software Engineering)
  ...
```

Uygulamayı durdurmak için: **Ctrl+C**

## 📊 Veritabanı Şeması

### Tablolar
- **student**: Öğrenci bilgileri
- **instructor**: Öğretim görevlisi bilgileri
- **course**: Ders bilgileri
- **enrollment**: Öğrenci-Ders kayıt bilgileri

### İlişkiler
- Bir Instructor birden fazla Course'a sahip olabilir
- Bir Student birden fazla Course'a kaydolabilir (Enrollment aracılığıyla)

## 🔧 ORM Modelleri

### Student
```python
from src.models import Student

# Öğrencileri sorgula
with db.session_scope() as session:
    students = session.query(Student).all()
```

### Instructor
```python
from src.models import Instructor

# Öğretim görevlilerini sorgula
with db.session_scope() as session:
    instructors = session.query(Instructor).all()
```

### Course
```python
from src.models import Course

# Dersleri sorgula
with db.session_scope() as session:
    courses = session.query(Course).all()
```

### Enrollment
```python
from src.models import Enrollment

# Kayıtları sorgula
with db.session_scope() as session:
    enrollments = session.query(Enrollment).all()
```

## � Örnek Kullanım

```python
from src.config.database import DatabaseManager
from src.models import Student, Course, Enrollment

# Veritabanına bağlan
db = DatabaseManager()
db.connect()

# Tüm öğrencileri listele
with db.session_scope() as session:
    students = session.query(Student).all()
    for student in students:
        print(f"{student.fname} {student.lname}")

# Yeni öğrenci ekle
with db.session_scope() as session:
    new_student = Student(
        fname="Ali",
        lname="Demir",
        department="Computer Engineering"
    )
    session.add(new_student)

# Bağlantıyı kapat
db.disconnect()
```

## 🧪 SQL Şemasını Manuel Olarak Yükleme

SQL dosyasını doğrudan çalıştırmak istersen:

```bash
psql -U postgres -h localhost -d course_registration -f database/schema.sql
```

## 📅 Önemli Tarihler
* **Teslim Tarihi:** 28.01.2026 - 17:00

## 📄 Lisans
Bu proje CPE312 dersi kapsamında hazırlanmıştır.

## 📞 İletişim
Sorularınız için lütfen proje ekibine ulaşın.