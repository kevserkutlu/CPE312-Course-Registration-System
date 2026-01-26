"""
Report Service - Raporlama İşlemleri
"""
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.models import Student, Instructor, Course, Enrollment


class ReportService:
    """Raporlama işlemlerini yönetir"""
    
    def __init__(self, db_session: Session):
        """
        Args:
            db_session: SQLAlchemy session nesnesi
        """
        self.session = db_session
    
    def get_students_per_course(self, course_id: int) -> dict:
        """
        Bir derse kayıtlı öğrencilerin sayısı ve listesi
        
        Args:
            course_id: Ders ID'si
            
        Returns:
            dict: Raporlama sonucu
        """
        try:
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            
            if not course:
                return {'success': False, 'message': f'Ders ID {course_id} bulunamadı', 'data': None}
            
            enrollments = self.session.query(Enrollment).filter_by(course_id=course_id).all()
            
            students_data = []
            for enrollment in enrollments:
                student = self.session.query(Student).filter_by(student_id=enrollment.student_id).first()
                students_data.append({
                    'student_id': student.student_id,
                    'name': f'{student.fname} {student.lname}',
                    'department': student.department,
                    'grade': enrollment.grade
                })
            
            return {
                'success': True,
                'message': f'{course.course_name} dersine {len(students_data)} öğrenci kayıtlı',
                'data': {
                    'course_name': course.course_name,
                    'instructor': f'{course.instructor.fname} {course.instructor.lname}',
                    'total_students': len(students_data),
                    'students': students_data
                }
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'data': None}
    
    def get_courses_per_student(self, student_id: int) -> dict:
        """
        Bir öğrencinin kayıtlı olduğu derslerin sayısı ve listesi
        
        Args:
            student_id: Öğrenci ID'si
            
        Returns:
            dict: Raporlama sonucu
        """
        try:
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            if not student:
                return {'success': False, 'message': f'Öğrenci ID {student_id} bulunamadı', 'data': None}
            
            enrollments = self.session.query(Enrollment).filter_by(student_id=student_id).all()
            
            courses_data = []
            for enrollment in enrollments:
                course = self.session.query(Course).filter_by(course_id=enrollment.course_id).first()
                courses_data.append({
                    'course_id': course.course_id,
                    'course_name': course.course_name,
                    'instructor': f'{course.instructor.fname} {course.instructor.lname}',
                    'grade': enrollment.grade
                })
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} {len(courses_data)} derse kayıtlı',
                'data': {
                    'student_name': f'{student.fname} {student.lname}',
                    'department': student.department,
                    'total_courses': len(courses_data),
                    'courses': courses_data
                }
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'data': None}
    
    def get_instructor_workload(self) -> dict:
        """
        Tüm öğretim görevlilerinin ders yükü
        
        Returns:
            dict: Raporlama sonucu
        """
        try:
            instructors = self.session.query(Instructor).all()
            
            workload_data = []
            for instructor in instructors:
                courses = self.session.query(Course).filter_by(instructor_id=instructor.instructor_id).all()
                total_students = 0
                for course in courses:
                    enrollments = self.session.query(Enrollment).filter_by(course_id=course.course_id).all()
                    total_students += len(enrollments)
                
                workload_data.append({
                    'instructor_id': instructor.instructor_id,
                    'name': f'{instructor.fname} {instructor.lname}',
                    'department': instructor.department,
                    'total_courses': len(courses),
                    'total_students': total_students
                })
            
            return {
                'success': True,
                'message': f'{len(workload_data)} öğretim görevlisinin iş yükü raporlandı',
                'data': workload_data
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'data': None}
    
    def get_department_statistics(self) -> dict:
        """
        Bölümlere göre öğrenci ve öğretim görevlisi istatistikleri
        
        Returns:
            dict: Raporlama sonucu
        """
        try:
            # Bölümler
            departments = self.session.query(Student.department).distinct().all()
            
            stats_data = []
            for (dept,) in departments:
                students = self.session.query(Student).filter_by(department=dept).all()
                instructors = self.session.query(Instructor).filter_by(department=dept).all()
                
                stats_data.append({
                    'department': dept,
                    'total_students': len(students),
                    'total_instructors': len(instructors)
                })
            
            return {
                'success': True,
                'message': f'{len(stats_data)} bölüm için istatistikler hesaplandı',
                'data': stats_data
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'data': None}
    
    def get_grade_distribution(self, course_id: int) -> dict:
        """
        Bir derste verilen notların dağılımı
        
        Args:
            course_id: Ders ID'si
            
        Returns:
            dict: Raporlama sonucu
        """
        try:
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            
            if not course:
                return {'success': False, 'message': f'Ders ID {course_id} bulunamadı', 'data': None}
            
            enrollments = self.session.query(Enrollment).filter_by(course_id=course_id).all()
            
            # Not dağılımı
            grade_distribution = {}
            for enrollment in enrollments:
                grade = enrollment.grade if enrollment.grade else 'No Grade'
                grade_distribution[grade] = grade_distribution.get(grade, 0) + 1
            
            return {
                'success': True,
                'message': f'{course.course_name} dersinde not dağılımı hesaplandı',
                'data': {
                    'course_name': course.course_name,
                    'total_students': len(enrollments),
                    'grade_distribution': grade_distribution
                }
            }
        
        except Exception as e:
            return {'success': False, 'message': f'Sorgu sırasında hata: {str(e)}', 'data': None}
