"""
Instructor Service - Öğretim Görevlisi Yönetimi
"""
from sqlalchemy.orm import Session
from src.models import Instructor


class InstructorService:
    """Öğretim görevlisi işlemlerini yönetir"""
    
    def __init__(self, db_session: Session):
        """
        Args:
            db_session: SQLAlchemy session nesnesi
        """
        self.session = db_session
    
    def create_instructor(self, fname: str, lname: str, department: str) -> dict:
        """
        Yeni öğretim görevlisi ekler
        
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
                return {'success': False, 'message': 'Ad boş olamaz', 'instructor': None}
            if not lname or not lname.strip():
                return {'success': False, 'message': 'Soyadı boş olamaz', 'instructor': None}
            if not department or not department.strip():
                return {'success': False, 'message': 'Bölüm boş olamaz', 'instructor': None}
            
            instructor = Instructor(
                fname=fname.strip(),
                lname=lname.strip(),
                department=department.strip()
            )
            
            self.session.add(instructor)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{instructor.fname} {instructor.lname} başarıyla eklendi (ID: {instructor.instructor_id})',
                'instructor': instructor
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Öğretim görevlisi eklenirken hata: {str(e)}', 'instructor': None}
    
    def update_instructor(self, instructor_id: int, fname: str = None, lname: str = None, department: str = None) -> dict:
        """
        Öğretim görevlisi bilgilerini günceller
        
        Args:
            instructor_id: Öğretim görevlisi ID'si
            fname: Yeni ad (opsiyonel)
            lname: Yeni soyadı (opsiyonel)
            department: Yeni bölüm (opsiyonel)
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            instructor = self.session.query(Instructor).filter_by(instructor_id=instructor_id).first()
            
            if not instructor:
                return {'success': False, 'message': f'Öğretim görevlisi ID {instructor_id} bulunamadı', 'instructor': None}
            
            if fname and fname.strip():
                instructor.fname = fname.strip()
            if lname and lname.strip():
                instructor.lname = lname.strip()
            if department and department.strip():
                instructor.department = department.strip()
            
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{instructor.fname} {instructor.lname} başarıyla güncellendi',
                'instructor': instructor
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Güncellenirken hata: {str(e)}', 'instructor': None}
    
    def delete_instructor(self, instructor_id: int) -> dict:
        """
        Öğretim görevlisi siler
        
        Args:
            instructor_id: Silinecek öğretim görevlisi ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            instructor = self.session.query(Instructor).filter_by(instructor_id=instructor_id).first()
            
            if not instructor:
                return {'success': False, 'message': f'Öğretim görevlisi ID {instructor_id} bulunamadı', 'instructor': None}
            
            instructor_name = f'{instructor.fname} {instructor.lname}'
            
            self.session.delete(instructor)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{instructor_name} başarıyla silindi',
                'instructor': None
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Silinirken hata: {str(e)}', 'instructor': None}
    
    def get_instructor(self, instructor_id: int) -> dict:
        """
        Tek bir öğretim görevlisi getirir
        
        Args:
            instructor_id: Öğretim görevlisi ID'si
            
        Returns:
            dict: Öğretim görevlisi bilgileri
        """
        try:
            instructor = self.session.query(Instructor).filter_by(instructor_id=instructor_id).first()
            
            if not instructor:
                return {'success': False, 'message': f'Öğretim görevlisi ID {instructor_id} bulunamadı', 'instructor': None}
            
            return {
                'success': True,
                'message': 'Öğretim görevlisi bulundu',
                'instructor': instructor
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'instructor': None}
    
    def get_all_instructors(self) -> dict:
        """
        Tüm öğretim görevlilerini getirir
        
        Returns:
            dict: Öğretim görevlilerinin listesi
        """
        try:
            instructors = self.session.query(Instructor).all()
            
            return {
                'success': True,
                'message': f'{len(instructors)} öğretim görevlisi bulundu',
                'instructors': instructors
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'instructors': []}
    
    def get_instructors_by_department(self, department: str) -> dict:
        """
        Bölüme göre öğretim görevlilerini getirir
        
        Args:
            department: Bölüm adı
            
        Returns:
            dict: Öğretim görevlilerinin listesi
        """
        try:
            instructors = self.session.query(Instructor).filter_by(department=department).all()
            
            return {
                'success': True,
                'message': f'{department} bölümünde {len(instructors)} öğretim görevlisi bulundu',
                'instructors': instructors
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'instructors': []}
