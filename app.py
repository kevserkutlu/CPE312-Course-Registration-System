# Import the DatabaseManager class from db_connection.py
from src.config.database import DatabaseManager
from src.models import Student, Instructor, Course, Enrollment
from src.resources import EnrollmentResource

def main():
    # Create an instance from the class
    db = DatabaseManager()

    # Establish connection
    conn = db.connect()

    if conn:
        # Create tables
        db.create_tables()
        
        print("Application is running...")
        print("=" * 60)
        
        # Initialize EnrollmentResource
        enrollment_resource = EnrollmentResource(db)
        
        # Example: List all students
        with db.session_scope() as session:
            students = session.query(Student).all()
            print(f"\n✓ Total {len(students)} students found")
        
        # Example: Courses
        with db.session_scope() as session:
            courses = session.query(Course).all()
            print(f"✓ Total {len(courses)} courses found")
        
        print("\n" + "=" * 60)
        print("ENROLLMENT EXAMPLES")
        print("=" * 60)
        
        # Example 1: Enroll student in course
        print("\n1️⃣  Enrolling student in course...")
        result = enrollment_resource.enroll_student(student_id=1, course_id=1)
        print(f"   {result['message']}")
        
        # Example 2: Try to enroll again (should already be enrolled)
        print("\n2️⃣  Enrolling same student in same course again...")
        result = enrollment_resource.enroll_student(student_id=1, course_id=1)
        print(f"   {result['message']}")
        
        # Example 3: Assign grade to student
        print("\n3️⃣  Assigning grade to student...")
        result = enrollment_resource.assign_grade(student_id=1, course_id=1, grade='AA')
        print(f"   {result['message']}")
        
        # Example 4: List student's courses
        print("\n4️⃣  Listing student's courses...")
        result = enrollment_resource.get_student_courses(student_id=1)
        print(f"   {result['message']}")
        if result['data']:
            for course_info in result['data']:
                print(f"      - {course_info['course_name']} ({course_info['instructor_name']}) - Grade: {course_info['grade']}")
        
        # Example 5: List students in course
        print("\n5️⃣  Listing students in course...")
        result = enrollment_resource.get_course_students(course_id=1)
        print(f"   {result['message']}")
        if result['data']:
            for student_info in result['data']:
                print(f"      - {student_info['student_name']} ({student_info['department']}) - Grade: {student_info['grade']}")
        
        # Example 6: Enroll another student in another course
        print("\n6️⃣  Enrolling another student in another course...")
        result = enrollment_resource.enroll_student(student_id=2, course_id=2)
        print(f"   {result['message']}")
        
        # Example 7: Drop student from course
        print("\n7️⃣  Dropping student from course...")
        result = enrollment_resource.drop_course(student_id=2, course_id=2)
        print(f"   {result['message']}")
        
        print("\n" + "=" * 60)
        
        try:
            # Run application until Ctrl+C
            while True:
                pass
        except KeyboardInterrupt:
            print("\nApplication shutting down...")
        finally:
            # Close connection when done
            db.disconnect()

if __name__ == "__main__":
    main()

