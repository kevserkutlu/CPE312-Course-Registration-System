"""
Enrollment Resource - REST API Endpoints
"""
from src.config.database import DatabaseManager
from src.services import EnrollmentService


class EnrollmentResource:
    """Enrollment işlemleri için API endpoints'i sağlar"""
    
    def __init__(self, db: DatabaseManager):
        """
        Args:
            db: DatabaseManager nesnesi
        """
        self.db = db
    
    def enroll_student(self, student_id: int, course_id: int) -> dict:
        """
        Öğrenciyi derse kaydeder
        
        Args:
            student_id: Öğrenci ID'si
            course_id: Ders ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        with self.db.session_scope() as session:
            service = EnrollmentService(session)
            result = service.enroll_student(student_id, course_id)
            return self._format_response(result)
    
    def drop_course(self, student_id: int, course_id: int) -> dict:
        """
        Öğrenciyi dersten çıkarır
        
        Args:
            student_id: Öğrenci ID'si
            course_id: Ders ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        with self.db.session_scope() as session:
            service = EnrollmentService(session)
            result = service.drop_course(student_id, course_id)
            return self._format_response(result)
    
    def assign_grade(self, student_id: int, course_id: int, grade: str) -> dict:
        """
        Öğrenciye not verir
        
        Args:
            student_id: Öğrenci ID'si
            course_id: Ders ID'si
            grade: Not (AA, BA, BB, CB, CC vb.)
            
        Returns:
            dict: İşlem sonucu
        """
        with self.db.session_scope() as session:
            service = EnrollmentService(session)
            result = service.assign_grade(student_id, course_id, grade)
            return self._format_response(result)
    
    def get_student_courses(self, student_id: int) -> dict:
        """
        Öğrencinin kayıtlı olduğu dersleri listeler
        
        Args:
            student_id: Öğrenci ID'si
            
        Returns:
            dict: Derslerin listesi
        """
        with self.db.session_scope() as session:
            service = EnrollmentService(session)
            result = service.get_student_courses(student_id)
            return self._format_response(result)
    
    def get_course_students(self, course_id: int) -> dict:
        """
        Derse kayıtlı öğrencileri listeler
        
        Args:
            course_id: Ders ID'si
            
        Returns:
            dict: Öğrencilerin listesi
        """
        with self.db.session_scope() as session:
            service = EnrollmentService(session)
            result = service.get_course_students(course_id)
            return self._format_response(result)
    
    def get_enrollment_info(self, enrollment_id: int) -> dict:
        """
        Kayıt detaylarını getirir
        
        Args:
            enrollment_id: Kayıt ID'si
            
        Returns:
            dict: Kayıt bilgileri
        """
        with self.db.session_scope() as session:
            service = EnrollmentService(session)
            result = service.get_enrollment_info(enrollment_id)
            return self._format_response(result)
    
    @staticmethod
    def _format_response(service_result: dict) -> dict:
        """
        Service'den gelen sonucu API response formatına dönüştürür
        
        Args:
            service_result: Service'den gelen sonuç
            
        Returns:
            dict: Formatlanmış response
        """
        response = {
            'success': service_result.get('success', False),
            'message': service_result.get('message', ''),
        }
        
        # Enrollment nesnesi varsa, sözlüğe dönüştür
        if service_result.get('enrollment'):
            response['enrollment'] = {
                'enrollment_id': service_result['enrollment'].enrollment_id,
                'student_id': service_result['enrollment'].student_id,
                'course_id': service_result['enrollment'].course_id,
                'grade': service_result['enrollment'].grade
            }
        
        # Data varsa ekle
        if 'data' in service_result:
            response['data'] = service_result['data']
        
        return response
