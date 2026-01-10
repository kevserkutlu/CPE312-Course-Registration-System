# db_connection.py dosyasındaki DatabaseManager sınıfını içeri aktar
from src.config.database import DatabaseManager
from src.models import Student, Instructor, Course, Enrollment
from src.resources import EnrollmentResource

def main():
    # Sınıftan bir nesne oluştur
    db = DatabaseManager()

    # Bağlantıyı kur
    conn = db.connect()

    if conn:
        # Tabloları oluştur
        db.create_tables()
        
        print("Uygulama çalışıyor...")
        print("=" * 60)
        
        # EnrollmentResource'u başlat
        enrollment_resource = EnrollmentResource(db)
        
        # Örnek: Öğrencileri listele
        with db.session_scope() as session:
            students = session.query(Student).all()
            print(f"\n✓ Toplam {len(students)} öğrenci bulundu")
        
        # Örnek: Dersler
        with db.session_scope() as session:
            courses = session.query(Course).all()
            print(f"✓ Toplam {len(courses)} ders bulundu")
        
        print("\n" + "=" * 60)
        print("ENROLLMENT ÖRNEKLERI")
        print("=" * 60)
        
        # Örnek 1: Öğrenciyi derse kaydet
        print("\n1️⃣  Öğrenciyi derse kaydedelim...")
        result = enrollment_resource.enroll_student(student_id=1, course_id=1)
        print(f"   {result['message']}")
        
        # Örnek 2: Tekrar kaydetmeyi dene (zaten kayıtlı olmalı)
        print("\n2️⃣  Aynı öğrenciyi aynı derse tekrar kaydedelim...")
        result = enrollment_resource.enroll_student(student_id=1, course_id=1)
        print(f"   {result['message']}")
        
        # Örnek 3: Öğrenciye not ver
        print("\n3️⃣  Öğrenciye not verelim...")
        result = enrollment_resource.assign_grade(student_id=1, course_id=1, grade='AA')
        print(f"   {result['message']}")
        
        # Örnek 4: Öğrencinin derslerini listele
        print("\n4️⃣  Öğrencinin derslerini listeleyelim...")
        result = enrollment_resource.get_student_courses(student_id=1)
        print(f"   {result['message']}")
        if result['data']:
            for course_info in result['data']:
                print(f"      - {course_info['course_name']} ({course_info['instructor_name']}) - Not: {course_info['grade']}")
        
        # Örnek 5: Derse kayıtlı öğrencileri listele
        print("\n5️⃣  Derse kayıtlı öğrencileri listeleyelim...")
        result = enrollment_resource.get_course_students(course_id=1)
        print(f"   {result['message']}")
        if result['data']:
            for student_info in result['data']:
                print(f"      - {student_info['student_name']} ({student_info['department']}) - Not: {student_info['grade']}")
        
        # Örnek 6: Öğrenciyi dersten çıkar
        print("\n6️⃣  Başka bir öğrenciyi derse kaydedelim...")
        result = enrollment_resource.enroll_student(student_id=2, course_id=2)
        print(f"   {result['message']}")
        
        print("\n7️⃣  Öğrenciyi dersten çıkaralım...")
        result = enrollment_resource.drop_course(student_id=2, course_id=2)
        print(f"   {result['message']}")
        
        print("\n" + "=" * 60)
        
        try:
            # Uygulamayı çalıştır - Ctrl+C ile kapatana kadar
            while True:
                pass
        except KeyboardInterrupt:
            print("\nUygulama kapatılıyor...")
        finally:
            # İşlem bittiğinde bağlantıyı kapat
            db.disconnect()

if __name__ == "__main__":
    main()

