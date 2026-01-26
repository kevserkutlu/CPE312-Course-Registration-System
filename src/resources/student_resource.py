"""
Student Resource - Student API Endpoints
"""
from src.config.database import DatabaseManager
from src.services import StudentService


class StudentResource:
    """Öğrenci işlemleri için API endpoints'i sağlar"""
    
    def __init__(self, db: DatabaseManager):
        """
        Args:
            db: DatabaseManager nesnesi
        """
        self.db = db
    
    def create_student(self, fname: str, lname: str, department: str) -> dict:
        """Yeni öğrenci ekler"""
        with self.db.session_scope() as session:
            service = StudentService(session)
            result = service.create_student(fname, lname, department)
            return self._format_response(result, 'student')
    
    def update_student(self, student_id: int, fname: str = None, lname: str = None, department: str = None) -> dict:
        """Öğrenci bilgilerini günceller"""
        with self.db.session_scope() as session:
            service = StudentService(session)
            result = service.update_student(student_id, fname, lname, department)
            return self._format_response(result, 'student')
    
    def delete_student(self, student_id: int) -> dict:
        """Öğrenci siler"""
        with self.db.session_scope() as session:
            service = StudentService(session)
            result = service.delete_student(student_id)
            return self._format_response(result, 'student')
    
    def get_student(self, student_id: int) -> dict:
        """Öğrenci bilgilerini getirir"""
        with self.db.session_scope() as session:
            service = StudentService(session)
            result = service.get_student(student_id)
            return self._format_response(result, 'student')
    
    def get_all_students(self) -> dict:
        """Tüm öğrencileri getirir"""
        with self.db.session_scope() as session:
            service = StudentService(session)
            result = service.get_all_students()
            return self._format_list_response(result, 'students')
    
    def get_students_by_department(self, department: str) -> dict:
        """Bölüme göre öğrencileri getirir"""
        with self.db.session_scope() as session:
            service = StudentService(session)
            result = service.get_students_by_department(department)
            return self._format_list_response(result, 'students')
    
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
