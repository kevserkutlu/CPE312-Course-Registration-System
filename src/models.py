from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.config.database.db import Base


class Student(Base):
    """Öğrenci modeli"""
    __tablename__ = "student"
    
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    
    # İlişkiler
    enrollments = relationship("Enrollment", back_populates="student")
    
    def __repr__(self):
        return f"<Student(student_id={self.student_id}, fname={self.fname}, lname={self.lname}, department={self.department})>"
    
    def to_dict(self):
        """Modeli sözlüğe dönüştür"""
        return {
            'student_id': self.student_id,
            'fname': self.fname,
            'lname': self.lname,
            'department': self.department
        }


class Instructor(Base):
    """Öğretmen/Öğretim görevlisi modeli"""
    __tablename__ = "instructor"
    
    instructor_id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    
    # İlişkiler
    courses = relationship("Course", back_populates="instructor")
    
    def __repr__(self):
        return f"<Instructor(instructor_id={self.instructor_id}, fname={self.fname}, lname={self.lname}, department={self.department})>"
    
    def to_dict(self):
        """Modeli sözlüğe dönüştür"""
        return {
            'instructor_id': self.instructor_id,
            'fname': self.fname,
            'lname': self.lname,
            'department': self.department
        }


class Course(Base):
    """Ders modeli"""
    __tablename__ = "course"
    
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(100), nullable=False)
    instructor_id = Column(Integer, ForeignKey("instructor.instructor_id"), nullable=False)
    
    # İlişkiler
    instructor = relationship("Instructor", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    
    def __repr__(self):
        return f"<Course(course_id={self.course_id}, course_name={self.course_name}, instructor_id={self.instructor_id})>"
    
    def to_dict(self):
        """Modeli sözlüğe dönüştür"""
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'instructor_id': self.instructor_id
        }


class Enrollment(Base):
    """Kayıt modeli (Öğrenci-Ders ilişkisi)"""
    __tablename__ = "enrollment"
    
    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.student_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("course.course_id"), nullable=False)
    grade = Column(String(2), nullable=True)
    
    # İlişkiler
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    
    def __repr__(self):
        return f"<Enrollment(enrollment_id={self.enrollment_id}, student_id={self.student_id}, course_id={self.course_id}, grade={self.grade})>"
    
    def to_dict(self):
        """Modeli sözlüğe dönüştür"""
        return {
            'enrollment_id': self.enrollment_id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'grade': self.grade
        }
