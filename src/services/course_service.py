"""
Course Service - Ders Yönetimi
"""
from sqlalchemy.orm import Session
from src.models import Course, Instructor


class CourseService:
    """Ders işlemlerini yönetir"""
    
    def __init__(self, db_session: Session):
        """
        Args:
            db_session: SQLAlchemy session nesnesi
        """
        self.session = db_session
    
    def create_course(self, course_name: str, instructor_id: int) -> dict:
        """
        Yeni ders ekler
        
        Args:
            course_name: Ders adı
            instructor_id: Öğretim görevlisi ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            # Doğrulama
            if not course_name or not course_name.strip():
                return {'success': False, 'message': 'Ders adı boş olamaz', 'course': None}
            
            # Öğretim görevlisini kontrol et
            instructor = self.session.query(Instructor).filter_by(instructor_id=instructor_id).first()
            if not instructor:
                return {'success': False, 'message': f'Öğretim görevlisi ID {instructor_id} bulunamadı', 'course': None}
            
            course = Course(
                course_name=course_name.strip(),
                instructor_id=instructor_id
            )
            
            self.session.add(course)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{course.course_name} başarıyla eklendi (ID: {course.course_id})',
                'course': course
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Ders eklenirken hata: {str(e)}', 'course': None}
    
    def update_course(self, course_id: int, course_name: str = None, instructor_id: int = None) -> dict:
        """
        Ders bilgilerini günceller
        
        Args:
            course_id: Ders ID'si
            course_name: Yeni ders adı (opsiyonel)
            instructor_id: Yeni öğretim görevlisi ID'si (opsiyonel)
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            
            if not course:
                return {'success': False, 'message': f'Ders ID {course_id} bulunamadı', 'course': None}
            
            if course_name and course_name.strip():
                course.course_name = course_name.strip()
            
            if instructor_id:
                instructor = self.session.query(Instructor).filter_by(instructor_id=instructor_id).first()
                if not instructor:
                    return {'success': False, 'message': f'Öğretim görevlisi ID {instructor_id} bulunamadı', 'course': None}
                course.instructor_id = instructor_id
            
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{course.course_name} başarıyla güncellendi',
                'course': course
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Güncellenirken hata: {str(e)}', 'course': None}
    
    def delete_course(self, course_id: int) -> dict:
        """
        Ders siler
        
        Args:
            course_id: Silinecek ders ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            
            if not course:
                return {'success': False, 'message': f'Ders ID {course_id} bulunamadı', 'course': None}
            
            course_name = course.course_name
            
            self.session.delete(course)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{course_name} başarıyla silindi',
                'course': None
            }
        
        except Exception as e:
            self.session.rollback()
            return {'success': False, 'message': f'Silinirken hata: {str(e)}', 'course': None}
    
    def get_course(self, course_id: int) -> dict:
        """
        Tek bir ders getirir
        
        Args:
            course_id: Ders ID'si
            
        Returns:
            dict: Ders bilgileri
        """
        try:
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            
            if not course:
                return {'success': False, 'message': f'Ders ID {course_id} bulunamadı', 'course': None}
            
            return {
                'success': True,
                'message': 'Ders bulundu',
                'course': course
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'course': None}
    
    def get_all_courses(self) -> dict:
        """
        Tüm dersleri getirir
        
        Returns:
            dict: Derslerin listesi
        """
        try:
            courses = self.session.query(Course).all()
            
            return {
                'success': True,
                'message': f'{len(courses)} ders bulundu',
                'courses': courses
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'courses': []}
    
    def get_instructor_courses(self, instructor_id: int) -> dict:
        """
        Öğretim görevlisinin derslerini getirir
        
        Args:
            instructor_id: Öğretim görevlisi ID'si
            
        Returns:
            dict: Derslerin listesi
        """
        try:
            instructor = self.session.query(Instructor).filter_by(instructor_id=instructor_id).first()
            
            if not instructor:
                return {'success': False, 'message': f'Öğretim görevlisi ID {instructor_id} bulunamadı', 'courses': []}
            
            courses = self.session.query(Course).filter_by(instructor_id=instructor_id).all()
            
            return {
                'success': True,
                'message': f'{instructor.fname} {instructor.lname} için {len(courses)} ders bulundu',
                'courses': courses
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'courses': []}
