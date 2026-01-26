"""
Course Registration System - Flask Web Application
"""
from flask import Flask, render_template, request, jsonify
from src.config.database import DatabaseManager
from src.resources import (
    StudentResource, InstructorResource, CourseResource, 
    EnrollmentResource, ReportResource
)

app = Flask(__name__)

# Database connection
db = DatabaseManager()
db.connect()
db.create_tables()

# Resources
student_resource = StudentResource(db)
instructor_resource = InstructorResource(db)
course_resource = CourseResource(db)
enrollment_resource = EnrollmentResource(db)
report_resource = ReportResource(db)


# ==================== STUDENT ROUTES ====================

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/api/students', methods=['GET'])
def get_students():
    """Get all students"""
    result = student_resource.get_all_students()
    return jsonify(result)


@app.route('/api/students', methods=['POST'])
def create_student():
    """Create a new student"""
    data = request.json
    result = student_resource.create_student(
        data.get('fname'),
        data.get('lname'),
        data.get('department')
    )
    return jsonify(result)


@app.route('/api/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Get a specific student"""
    result = student_resource.get_student(student_id)
    return jsonify(result)


@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update a student"""
    data = request.json
    result = student_resource.update_student(
        student_id,
        data.get('fname'),
        data.get('lname'),
        data.get('department')
    )
    return jsonify(result)


@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student"""
    result = student_resource.delete_student(student_id)
    return jsonify(result)


# ==================== INSTRUCTOR ROUTES ====================

@app.route('/api/instructors', methods=['GET'])
def get_instructors():
    """Get all instructors"""
    result = instructor_resource.get_all_instructors()
    return jsonify(result)


@app.route('/api/instructors', methods=['POST'])
def create_instructor():
    """Create a new instructor"""
    data = request.json
    result = instructor_resource.create_instructor(
        data.get('fname'),
        data.get('lname'),
        data.get('department')
    )
    return jsonify(result)


@app.route('/api/instructors/<int:instructor_id>', methods=['GET'])
def get_instructor(instructor_id):
    """Get a specific instructor"""
    result = instructor_resource.get_instructor(instructor_id)
    return jsonify(result)


@app.route('/api/instructors/<int:instructor_id>', methods=['PUT'])
def update_instructor(instructor_id):
    """Update an instructor"""
    data = request.json
    result = instructor_resource.update_instructor(
        instructor_id,
        data.get('fname'),
        data.get('lname'),
        data.get('department')
    )
    return jsonify(result)


@app.route('/api/instructors/<int:instructor_id>', methods=['DELETE'])
def delete_instructor(instructor_id):
    """Delete an instructor"""
    result = instructor_resource.delete_instructor(instructor_id)
    return jsonify(result)


# ==================== COURSE ROUTES ====================

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Get all courses"""
    result = course_resource.get_all_courses()
    return jsonify(result)


@app.route('/api/courses', methods=['POST'])
def create_course():
    """Create a new course"""
    data = request.json
    result = course_resource.create_course(
        data.get('course_name'),
        data.get('instructor_id')
    )
    return jsonify(result)


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Get a specific course"""
    result = course_resource.get_course(course_id)
    return jsonify(result)


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update a course"""
    data = request.json
    result = course_resource.update_course(
        course_id,
        data.get('course_name'),
        data.get('instructor_id')
    )
    return jsonify(result)


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """Delete a course"""
    result = course_resource.delete_course(course_id)
    return jsonify(result)


# ==================== ENROLLMENT ROUTES ====================

@app.route('/api/enrollments', methods=['POST'])
def enroll_student():
    """Enroll a student in a course"""
    data = request.json
    result = enrollment_resource.enroll_student(
        data.get('student_id'),
        data.get('course_id')
    )
    return jsonify(result)


@app.route('/api/enrollments/drop', methods=['POST'])
def drop_course():
    """Drop a student from a course"""
    data = request.json
    result = enrollment_resource.drop_course(
        data.get('student_id'),
        data.get('course_id')
    )
    return jsonify(result)


@app.route('/api/enrollments/grade', methods=['POST'])
def assign_grade():
    """Assign a grade to an enrollment"""
    data = request.json
    result = enrollment_resource.assign_grade(
        data.get('student_id'),
        data.get('course_id'),
        data.get('grade')
    )
    return jsonify(result)


@app.route('/api/enrollments/student/<int:student_id>', methods=['GET'])
def get_student_courses(student_id):
    """Get courses for a student"""
    result = enrollment_resource.get_student_courses(student_id)
    return jsonify(result)


@app.route('/api/enrollments/course/<int:course_id>', methods=['GET'])
def get_course_students(course_id):
    """Get students in a course"""
    result = enrollment_resource.get_course_students(course_id)
    return jsonify(result)


# ==================== REPORT ROUTES ====================

@app.route('/api/reports/students-per-course/<int:course_id>', methods=['GET'])
def report_students_per_course(course_id):
    """Students enrolled in a course"""
    result = report_resource.get_students_per_course(course_id)
    return jsonify(result)


@app.route('/api/reports/courses-per-student/<int:student_id>', methods=['GET'])
def report_courses_per_student(student_id):
    """Courses for a student"""
    result = report_resource.get_courses_per_student(student_id)
    return jsonify(result)


@app.route('/api/reports/instructor-workload', methods=['GET'])
def report_instructor_workload():
    """Instructor workload"""
    result = report_resource.get_instructor_workload()
    return jsonify(result)


@app.route('/api/reports/department-statistics', methods=['GET'])
def report_department_statistics():
    """Department statistics"""
    result = report_resource.get_department_statistics()
    return jsonify(result)


@app.route('/api/reports/grade-distribution/<int:course_id>', methods=['GET'])
def report_grade_distribution(course_id):
    """Grade distribution in a course"""
    result = report_resource.get_grade_distribution(course_id)
    return jsonify(result)


if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        print("\nApplication shutting down...")
        db.disconnect()
