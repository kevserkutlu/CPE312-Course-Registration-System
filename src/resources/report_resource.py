"""
Report Resource - Report API Endpoints
"""
from src.config.database import DatabaseManager
from src.services.report_service import ReportService


class ReportResource:
    """Raporlama işlemleri için API endpoints'i sağlar"""
    
    def __init__(self, db: DatabaseManager):
        """
        Args:
            db: DatabaseManager nesnesi
        """
        self.db = db
    
    def get_students_per_course(self, course_id: int) -> dict:
        """Bir derse kayıtlı öğrencilerin listesi"""
        with self.db.session_scope() as session:
            service = ReportService(session)
            return service.get_students_per_course(course_id)
    
    def get_courses_per_student(self, student_id: int) -> dict:
        """Bir öğrencinin kayıtlı olduğu derslerin listesi"""
        with self.db.session_scope() as session:
            service = ReportService(session)
            return service.get_courses_per_student(student_id)
    
    def get_instructor_workload(self) -> dict:
        """Tüm öğretim görevlilerinin ders yükü"""
        with self.db.session_scope() as session:
            service = ReportService(session)
            return service.get_instructor_workload()
    
    def get_department_statistics(self) -> dict:
        """Bölümlere göre istatistikler"""
        with self.db.session_scope() as session:
            service = ReportService(session)
            return service.get_department_statistics()
    
    def get_grade_distribution(self, course_id: int) -> dict:
        """Bir derste verilen notların dağılımı"""
        with self.db.session_scope() as session:
            service = ReportService(session)
            return service.get_grade_distribution(course_id)
