"""
Course Resource - Course API Endpoints
"""
from src.config.database import DatabaseManager
from src.services import CourseService


class CourseResource:
    """Ders işlemleri için API endpoints'i sağlar"""
    
    def __init__(self, db: DatabaseManager):
        """
        Args:
            db: DatabaseManager nesnesi
        """
        self.db = db
    
    def create_course(self, course_name: str, instructor_id: int) -> dict:
        """Yeni ders ekler"""
        with self.db.session_scope() as session:
            service = CourseService(session)
            result = service.create_course(course_name, instructor_id)
            return self._format_response(result, 'course')
    
    def update_course(self, course_id: int, course_name: str = None, instructor_id: int = None) -> dict:
        """Ders bilgilerini günceller"""
        with self.db.session_scope() as session:
            service = CourseService(session)
            result = service.update_course(course_id, course_name, instructor_id)
            return self._format_response(result, 'course')
    
    def delete_course(self, course_id: int) -> dict:
        """Ders siler"""
        with self.db.session_scope() as session:
            service = CourseService(session)
            result = service.delete_course(course_id)
            return self._format_response(result, 'course')
    
    def get_course(self, course_id: int) -> dict:
        """Ders bilgilerini getirir"""
        with self.db.session_scope() as session:
            service = CourseService(session)
            result = service.get_course(course_id)
            return self._format_response(result, 'course')
    
    def get_all_courses(self) -> dict:
        """Tüm dersleri getirir"""
        with self.db.session_scope() as session:
            service = CourseService(session)
            result = service.get_all_courses()
            return self._format_list_response(result, 'courses')
    
    def get_instructor_courses(self, instructor_id: int) -> dict:
        """Öğretim görevlisinin derslerini getirir"""
        with self.db.session_scope() as session:
            service = CourseService(session)
            result = service.get_instructor_courses(instructor_id)
            return self._format_list_response(result, 'courses')
    
    @staticmethod
    def _format_response(service_result: dict, key: str) -> dict:
        """Service sonucunu format et"""
        response = {
            'success': service_result.get('success', False),
            'message': service_result.get('message', ''),
        }
        
        if service_result.get(key):
            response[key] = service_result[key].to_dict()
        
        return response
    
    @staticmethod
    def _format_list_response(service_result: dict, key: str) -> dict:
        """Service liste sonucunu format et"""
        response = {
            'success': service_result.get('success', False),
            'message': service_result.get('message', ''),
        }
        
        if service_result.get(key):
            response[key] = [item.to_dict() for item in service_result[key]]
        
        return response
