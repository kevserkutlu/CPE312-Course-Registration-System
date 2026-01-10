# db_connection.py dosyasındaki DatabaseManager sınıfını içeri aktar
from src.config.database import DatabaseManager
from src.models import Student, Instructor, Course, Enrollment

def main():
    # Sınıftan bir nesne oluştur
    db = DatabaseManager()

    # Bağlantıyı kur
    conn = db.connect()

    if conn:
        # Tabloları oluştur
        db.create_tables()
        
        print("Uygulama çalışıyor...")
        
        try:
            # Örnek: Tüm öğrencileri listele
            with db.session_scope() as session:
                students = session.query(Student).all()
                print(f"\nToplam {len(students)} öğrenci bulundu:")
                for student in students:
                    print(f"  - {student.fname} {student.lname} ({student.department})")
            
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
