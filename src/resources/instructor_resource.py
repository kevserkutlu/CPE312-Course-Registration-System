"""
Instructor Resource - Instructor API Endpoints
"""
from src.config.database import DatabaseManager
from src.services import InstructorService


class InstructorResource:
    """Öğretim görevlisi işlemleri için API endpoints'i sağlar"""
    
    def __init__(self, db: DatabaseManager):
        """
        Args:
            db: DatabaseManager nesnesi
        """
        self.db = db
    
    def create_instructor(self, fname: str, lname: str, department: str) -> dict:
        """Yeni öğretim görevlisi ekler"""
        with self.db.session_scope() as session:
            service = InstructorService(session)
            result = service.create_instructor(fname, lname, department)
            return self._format_response(result, 'instructor')
    
    def update_instructor(self, instructor_id: int, fname: str = None, lname: str = None, department: str = None) -> dict:
        """Öğretim görevlisi bilgilerini günceller"""
        with self.db.session_scope() as session:
            service = InstructorService(session)
            result = service.update_instructor(instructor_id, fname, lname, department)
            return self._format_response(result, 'instructor')
    
    def delete_instructor(self, instructor_id: int) -> dict:
        """Öğretim görevlisi siler"""
        with self.db.session_scope() as session:
            service = InstructorService(session)
            result = service.delete_instructor(instructor_id)
            return self._format_response(result, 'instructor')
    
    def get_instructor(self, instructor_id: int) -> dict:
        """Öğretim görevlisi bilgilerini getirir"""
        with self.db.session_scope() as session:
            service = InstructorService(session)
            result = service.get_instructor(instructor_id)
            return self._format_response(result, 'instructor')
    
    def get_all_instructors(self) -> dict:
        """Tüm öğretim görevlilerini getirir"""
        with self.db.session_scope() as session:
            service = InstructorService(session)
            result = service.get_all_instructors()
            return self._format_list_response(result, 'instructors')
    
    def get_instructors_by_department(self, department: str) -> dict:
        """Bölüme göre öğretim görevlilerini getirir"""
        with self.db.session_scope() as session:
            service = InstructorService(session)
            result = service.get_instructors_by_department(department)
            return self._format_list_response(result, 'instructors')
    
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
