"""
Enrollment Service - Ders Kayıt İşlemleri
"""
from sqlalchemy.orm import Session
from src.models import Student, Course, Enrollment


class EnrollmentService:
    """Ders kayıt işlemlerini yönetir"""
    
    def __init__(self, db_session: Session):
        """
        Args:
            db_session: SQLAlchemy session nesnesi
        """
        self.session = db_session
    
    def enroll_student(self, student_id: int, course_id: int) -> dict:
        """
        Öğrenciyi derse kaydeder
        
        Args:
            student_id: Öğrenci ID'si
            course_id: Ders ID'si
            
        Returns:
            dict: Kayıt sonucu {'success': bool, 'message': str, 'enrollment': Enrollment}
        """
        try:
            # Öğrenciyi kontrol et
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            if not student:
                return {
                    'success': False,
                    'message': f'Öğrenci ID {student_id} bulunamadı',
                    'enrollment': None
                }
            
            # Dersi kontrol et
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            if not course:
                return {
                    'success': False,
                    'message': f'Ders ID {course_id} bulunamadı',
                    'enrollment': None
                }
            
            # Zaten kayıtlı mı kontrol et
            existing_enrollment = self.session.query(Enrollment).filter_by(
                student_id=student_id,
                course_id=course_id
            ).first()
            
            if existing_enrollment:
                return {
                    'success': False,
                    'message': f'Öğrenci {student.fname} {student.lname} zaten {course.course_name} dersine kayıtlı',
                    'enrollment': existing_enrollment
                }
            
            # Yeni kayıt oluştur
            enrollment = Enrollment(
                student_id=student_id,
                course_id=course_id,
                grade=None
            )
            
            self.session.add(enrollment)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} başarıyla {course.course_name} dersine kaydedildi',
                'enrollment': enrollment
            }
        
        except Exception as e:
            self.session.rollback()
            return {
                'success': False,
                'message': f'Kayıt sırasında hata oluştu: {str(e)}',
                'enrollment': None
            }
    
    def drop_course(self, student_id: int, course_id: int) -> dict:
        """
        Öğrenciyi dersten çıkarır
        
        Args:
            student_id: Öğrenci ID'si
            course_id: Ders ID'si
            
        Returns:
            dict: İşlem sonucu
        """
        try:
            enrollment = self.session.query(Enrollment).filter_by(
                student_id=student_id,
                course_id=course_id
            ).first()
            
            if not enrollment:
                return {
                    'success': False,
                    'message': f'Kayıt bulunamadı (Öğrenci: {student_id}, Ders: {course_id})',
                    'enrollment': None
                }
            
            # Dersin adını al
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            self.session.delete(enrollment)
            self.session.commit()
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} başarıyla {course.course_name} dersinden çıkarıldı',
                'enrollment': None
            }
        
        except Exception as e:
            self.session.rollback()
            return {
                'success': False,
                'message': f'Dersten çıkarma sırasında hata oluştu: {str(e)}',
                'enrollment': None
            }
    
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
        try:
            # Geçerli notlar
            valid_grades = ['AA', 'BA', 'BB', 'CB', 'CC', 'DC', 'DD', 'FD', 'FF']
            
            if grade not in valid_grades:
                return {
                    'success': False,
                    'message': f'Geçersiz not: {grade}. Geçerli notlar: {", ".join(valid_grades)}',
                    'enrollment': None
                }
            
            enrollment = self.session.query(Enrollment).filter_by(
                student_id=student_id,
                course_id=course_id
            ).first()
            
            if not enrollment:
                return {
                    'success': False,
                    'message': f'Kayıt bulunamadı (Öğrenci: {student_id}, Ders: {course_id})',
                    'enrollment': None
                }
            
            old_grade = enrollment.grade
            enrollment.grade = grade
            self.session.commit()
            
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} için {course.course_name} notı {old_grade} -> {grade} olarak güncellendi',
                'enrollment': enrollment
            }
        
        except Exception as e:
            self.session.rollback()
            return {
                'success': False,
                'message': f'Not verme sırasında hata oluştu: {str(e)}',
                'enrollment': None
            }
    
    def get_student_courses(self, student_id: int) -> dict:
        """
        Öğrencinin kayıtlı olduğu dersleri listeler
        
        Args:
            student_id: Öğrenci ID'si
            
        Returns:
            dict: Derslerin listesi
        """
        try:
            student = self.session.query(Student).filter_by(student_id=student_id).first()
            
            if not student:
                return {
                    'success': False,
                    'message': f'Öğrenci ID {student_id} bulunamadı',
                    'data': []
                }
            
            enrollments = self.session.query(Enrollment).filter_by(student_id=student_id).all()
            
            courses_data = []
            for enrollment in enrollments:
                course = self.session.query(Course).filter_by(course_id=enrollment.course_id).first()
                instructor = course.instructor
                
                courses_data.append({
                    'enrollment_id': enrollment.enrollment_id,
                    'course_id': course.course_id,
                    'course_name': course.course_name,
                    'instructor_name': f'{instructor.fname} {instructor.lname}',
                    'grade': enrollment.grade
                })
            
            return {
                'success': True,
                'message': f'{student.fname} {student.lname} için {len(courses_data)} ders bulundu',
                'data': courses_data
            }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'Sorgu sırasında hata oluştu: {str(e)}',
                'data': []
            }
    
    def get_course_students(self, course_id: int) -> dict:
        """
        Derse kayıtlı öğrencileri listeler
        
        Args:
            course_id: Ders ID'si
            
        Returns:
            dict: Öğrencilerin listesi
        """
        try:
            course = self.session.query(Course).filter_by(course_id=course_id).first()
            
            if not course:
                return {
                    'success': False,
                    'message': f'Ders ID {course_id} bulunamadı',
                    'data': []
                }
            
            enrollments = self.session.query(Enrollment).filter_by(course_id=course_id).all()
            
            students_data = []
            for enrollment in enrollments:
                student = self.session.query(Student).filter_by(student_id=enrollment.student_id).first()
                
                students_data.append({
                    'enrollment_id': enrollment.enrollment_id,
                    'student_id': student.student_id,
                    'student_name': f'{student.fname} {student.lname}',
                    'department': student.department,
                    'grade': enrollment.grade
                })
            
            return {
                'success': True,
                'message': f'{course.course_name} dersine {len(students_data)} öğrenci kayıtlı',
                'data': students_data
            }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'Sorgu sırasında hata oluştu: {str(e)}',
                'data': []
            }
    
    def get_enrollment_info(self, enrollment_id: int) -> dict:
        """
        Kayıt detaylarını getirir
        
        Args:
            enrollment_id: Kayıt ID'si
            
        Returns:
            dict: Kayıt bilgileri
        """
        try:
            enrollment = self.session.query(Enrollment).filter_by(enrollment_id=enrollment_id).first()
            
            if not enrollment:
                return {
                    'success': False,
                    'message': f'Kayıt ID {enrollment_id} bulunamadı',
                    'data': None
                }
            
            student = self.session.query(Student).filter_by(student_id=enrollment.student_id).first()
            course = self.session.query(Course).filter_by(course_id=enrollment.course_id).first()
            
            return {
                'success': True,
                'message': 'Kayıt bulundu',
                'data': {
                    'enrollment_id': enrollment.enrollment_id,
                    'student': student.to_dict(),
                    'course': course.to_dict(),
                    'grade': enrollment.grade
                }
            }
        
        except Exception as e:
            return {
                'success': False,
                'message': f'Sorgu sırasında hata oluştu: {str(e)}',
                'data': None
            }
