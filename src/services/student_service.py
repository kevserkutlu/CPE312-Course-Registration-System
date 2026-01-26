"""
Student Service - Öğrenci Yönetimi
"""
from sqlalchemy.orm import Session
from src.models import Student


class StudentService:
    """Öğrenci işlemlerini yönetir"""
    
    def __init__(self, db_session: Session):
        """
        Args:
            db_session: SQLAlchemy session nesnesi
        """
        self.session = db_session
    
    def create_student(self, fname: str, lname: str, department: str) -> dict:
        """
        Yeni öğrenci ekler
        
        Args:
            fname: Ad
            lname: Soyadı
            department: Bölüm
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            # Doğrulama
            if not fname or not fname.strip():
                return {'success': False, 'message': 'Ad boş olamaz', 'student': None}
            if not lname or not lname.strip():
                return {'success': False, 'message': 'Soyadı boş olamaz', 'student': None}
            if not department or not department.strip():
                return {'success': False, 'message': 'Bölüm boş olamaz', 'student': None}
            
            student = Student(
                fname=fname.strip(),
                lname=lname.strip(),
                department=department.strip()
            )
            
            self.session.add(student)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} başarıyla eklendi (ID: {student.student_id})',
                'student': student
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Öğrenci eklenirken hata: {str(e)}', 'student': None}
    
    def update_student(self, student_id: int, fname: str = None, lname: str = None, department: str = None) -> dict:
        """
        Öğrenci bilgilerini günceller
        
        Args:
            student_id: Öğrenci ID'si
            fname: Yeni ad (opsiyonel)
            lname: Yeni soyadı (opsiyonel)
            department: Yeni bölüm (opsiyonel)
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            if not student:
                return {'success': False, 'message': f'Öğrenci ID {student_id} bulunamadı', 'student': None}
            
            if fname and fname.strip():
                student.fname = fname.strip()
            if lname and lname.strip():
                student.lname = lname.strip()
            if department and department.strip():
                student.department = department.strip()
            
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} başarıyla güncellendi',
                'student': student
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Güncellenirken hata: {str(e)}', 'student': None}
    
    def delete_student(self, student_id: int) -> dict:
        """
        Öğrenci siler
        
        Args:
            student_id: Silinecek öğrenci ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            if not student:
                return {'success': False, 'message': f'Öğrenci ID {student_id} bulunamadı', 'student': None}
            
            student_name = f'{student.fname} {student.lname}'
            
            self.session.delete(student)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{student_name} başarıyla silindi',
                'student': None
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Silinirken hata: {str(e)}', 'student': None}
    
    def get_student(self, student_id: int) -> dict:
        """
        Tek bir öğrenci getirir
        
        Args:
            student_id: Öğrenci ID'si
            
        Returns:
            dict: Öğrenci bilgileri
        """
        try:
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            if not student:
                return {'success': False, 'message': f'Öğrenci ID {student_id} bulunamadı', 'student': None}
            
            return {
                'success': True,
                'message': 'Öğrenci bulundu',
                'student': student
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'student': None}
    
    def get_all_students(self) -> dict:
        """
        Tüm öğrencileri getirir
        
        Returns:
            dict: Öğrencilerin listesi
        """
        try:
            students = self.session.query(Student).all()
            
            return {
                'success': True,
                'message': f'{len(students)} öğrenci bulundu',
                'students': students
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'students': []}
    
    def get_students_by_department(self, department: str) -> dict:
        """
        Bölüme göre öğrencileri getirir
        
        Args:
            department: Bölüm adı
            
        Returns:
            dict: Öğrencilerin listesi
        """
        try:
            students = self.session.query(Student).filter_by(department=department).all()
            
            return {
                'success': True,
                'message': f'{department} bölümünde {len(students)} öğrenci bulundu',
                'students': students
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'students': []}
