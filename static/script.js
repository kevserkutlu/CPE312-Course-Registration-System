// Tab Switching
function switchTab(tabName) {
    // Hide all tabs
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => content.classList.remove('active'));
    
    // Remove active from all buttons
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active to clicked button
    event.target.classList.add('active');
}

// Helper function to show messages
function showMessage(message, type = 'info') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    
    const container = document.body;
    container.insertBefore(messageDiv, container.firstChild);
    
    setTimeout(() => messageDiv.remove(), 5000);
}

// ==================== STUDENT FUNCTIONS ====================

function createStudent() {
    const fname = document.getElementById('student-fname').value;
    const lname = document.getElementById('student-lname').value;
    const department = document.getElementById('student-dept').value;
    
    if (!fname || !lname || !department) {
        showMessage('Please fill in all fields!', 'error');
        return;
    }
    
    fetch('/api/students', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fname, lname, department })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            showMessage(data.message, 'success');
            document.getElementById('student-fname').value = '';
            document.getElementById('student-lname').value = '';
            document.getElementById('student-dept').value = '';
            loadStudents();
        } else {
            showMessage(data.message, 'error');
        }
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function loadStudents() {
    fetch('/api/students')
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('students-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        if (!data.students || data.students.length === 0) {
            list.innerHTML = '<p>No students found.</p>';
            return;
        }
        
        list.innerHTML = data.students.map(s => `
            <div class="item">
                <div class="item-info">
                    <strong>ID: ${s.student_id}</strong><br>
                    <p><strong>Name:</strong> ${s.fname} ${s.lname}</p>
                    <p><strong>Department:</strong> ${s.department}</p>
                </div>
                <div class="item-actions">
                    <button class="btn-small btn-delete" onclick="deleteStudent(${s.student_id})">Delete</button>
                </div>
            </div>
        `).join('');
    })
    .catch(err => showMessage('Hata: ' + err, 'error'));
}

function deleteStudent(studentId) {
    if (!confirm('Delete this student? This action cannot be undone.')) return;
    
    fetch(`/api/students/${studentId}`, { method: 'DELETE' })
    .then(r => r.json())
    .then(data => {
        showMessage(data.message, data.success ? 'success' : 'error');
        if (data.success) loadStudents();
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

// ==================== INSTRUCTOR FUNCTIONS ====================

function createInstructor() {
    const fname = document.getElementById('instructor-fname').value;
    const lname = document.getElementById('instructor-lname').value;
    const department = document.getElementById('instructor-dept').value;
    
    if (!fname || !lname || !department) {
        showMessage('Please fill in all fields!', 'error');
        return;
    }
    
    fetch('/api/instructors', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fname, lname, department })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            showMessage(data.message, 'success');
            document.getElementById('instructor-fname').value = '';
            document.getElementById('instructor-lname').value = '';
            document.getElementById('instructor-dept').value = '';
            loadInstructors();
        } else {
            showMessage(data.message, 'error');
        }
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function loadInstructors() {
    fetch('/api/instructors')
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('instructors-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        if (!data.instructors || data.instructors.length === 0) {
            list.innerHTML = '<p>No instructors found.</p>';
            return;
        }
        
        list.innerHTML = data.instructors.map(i => `
            <div class="item">
                <div class="item-info">
                    <strong>ID: ${i.instructor_id}</strong><br>
                    <p><strong>Name:</strong> ${i.fname} ${i.lname}</p>
                    <p><strong>Department:</strong> ${i.department}</p>
                </div>
                <div class="item-actions">
                    <button class="btn-small btn-delete" onclick="deleteInstructor(${i.instructor_id})">Delete</button>
                </div>
            </div>
        `).join('');
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function deleteInstructor(instructorId) {
    if (!confirm('Delete this instructor? This action cannot be undone.')) return;
    
    fetch(`/api/instructors/${instructorId}`, { method: 'DELETE' })
    .then(r => r.json())
    .then(data => {
        showMessage(data.message, data.success ? 'success' : 'error');
        if (data.success) loadInstructors();
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

// ==================== COURSE FUNCTIONS ====================

function createCourse() {
    const course_name = document.getElementById('course-name').value;
    const instructor_id = document.getElementById('course-instructor').value;
    
    if (!course_name || !instructor_id) {
        showMessage('Please fill in all fields!', 'error');
        return;
    }
    
    fetch('/api/courses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ course_name, instructor_id: parseInt(instructor_id) })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            showMessage(data.message, 'success');
            document.getElementById('course-name').value = '';
            document.getElementById('course-instructor').value = '';
            loadCourses();
        } else {
            showMessage(data.message, 'error');
        }
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function loadCourses() {
    fetch('/api/courses')
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('courses-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        if (!data.courses || data.courses.length === 0) {
            list.innerHTML = '<p>No courses found.</p>';
            return;
        }
        
        list.innerHTML = data.courses.map(c => `
            <div class="item">
                <div class="item-info">
                    <strong>ID: ${c.course_id}</strong><br>
                    <p><strong>Course Name:</strong> ${c.course_name}</p>
                    <p><strong>Instructor ID:</strong> ${c.instructor_id}</p>
                </div>
                <div class="item-actions">
                    <button class="btn-small btn-delete" onclick="deleteCourse(${c.course_id})">Delete</button>
                </div>
            </div>
        `).join('');
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function deleteCourse(courseId) {
    if (!confirm('Delete this course? This action cannot be undone.')) return;
    
    fetch(`/api/courses/${courseId}`, { method: 'DELETE' })
    .then(r => r.json())
    .then(data => {
        showMessage(data.message, data.success ? 'success' : 'error');
        if (data.success) loadCourses();
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

// ==================== ENROLLMENT FUNCTIONS ====================

function enrollStudent() {
    const student_id = parseInt(document.getElementById('enroll-student').value);
    const course_id = parseInt(document.getElementById('enroll-course').value);
    
    if (!student_id || !course_id) {
        showMessage('Please enter student and course IDs!', 'error');
        return;
    }
    
    fetch('/api/enrollments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ student_id, course_id })
    })
    .then(r => r.json())
    .then(data => {
        showMessage(data.message, data.success ? 'success' : 'error');
        if (data.success) {
            document.getElementById('enroll-student').value = '';
            document.getElementById('enroll-course').value = '';
        }
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function dropCourse() {
    const student_id = parseInt(document.getElementById('drop-student').value);
    const course_id = parseInt(document.getElementById('drop-course').value);
    
    if (!student_id || !course_id) {
        showMessage('Please enter student and course IDs!', 'error');
        return;
    }
    
    fetch('/api/enrollments/drop', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ student_id, course_id })
    })
    .then(r => r.json())
    .then(data => {
        showMessage(data.message, data.success ? 'success' : 'error');
        if (data.success) {
            document.getElementById('drop-student').value = '';
            document.getElementById('drop-course').value = '';
        }
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function assignGrade() {
    const student_id = parseInt(document.getElementById('grade-student').value);
    const course_id = parseInt(document.getElementById('grade-course').value);
    const grade = document.getElementById('grade-value').value;
    
    if (!student_id || !course_id || !grade) {
        showMessage('Please fill in all fields!', 'error');
        return;
    }
    
    fetch('/api/enrollments/grade', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ student_id, course_id, grade })
    })
    .then(r => r.json())
    .then(data => {
        showMessage(data.message, data.success ? 'success' : 'error');
        if (data.success) {
            document.getElementById('grade-student').value = '';
            document.getElementById('grade-course').value = '';
            document.getElementById('grade-value').value = '';
        }
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function loadStudentCourses() {
    const student_id = parseInt(document.getElementById('student-courses-id').value);
    
    if (!student_id) {
        showMessage('Please enter student ID!', 'error');
        return;
    }
    
    fetch(`/api/enrollments/student/${student_id}`)
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('enrollments-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        if (!data.data || !data.data.courses || data.data.courses.length === 0) {
            list.innerHTML = '<p>No courses found.</p>';
            return;
        }
        
        list.innerHTML = `
            <h3>${data.data.student_name} - Courses</h3>
            ${data.data.courses.map(c => `
                <div class="item">
                    <div class="item-info">
                        <p><strong>Course Name:</strong> ${c.course_name}</p>
                        <p><strong>Instructor:</strong> ${c.instructor}</p>
                        <p><strong>Grade:</strong> ${c.grade || 'Not yet assigned'}</p>
                    </div>
                </div>
            `).join('')}
        `;
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

// ==================== REPORT FUNCTIONS ====================

function reportStudentsPerCourse() {
    const course_id = parseInt(document.getElementById('report-course-id').value);
    
    if (!course_id) {
        showMessage('Please enter course ID!', 'error');
        return;
    }
    
    fetch(`/api/reports/students-per-course/${course_id}`)
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('reports-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        list.innerHTML = `
            <h3>${data.data.course_name}</h3>
            <p><strong>Instructor:</strong> ${data.data.instructor}</p>
            <p><strong>Total Students:</strong> ${data.data.total_students}</p>
            <hr>
            ${data.data.students.map(s => `
                <div class="item">
                    <div class="item-info">
                        <p><strong>${s.name}</strong> (${s.department})</p>
                        <p><strong>Grade:</strong> ${s.grade || 'Not yet assigned'}</p>
                    </div>
                </div>
            `).join('')}
        `;
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function reportCoursesPerStudent() {
    const student_id = parseInt(document.getElementById('report-student-id').value);
    
    if (!student_id) {
        showMessage('Please enter student ID!', 'error');
        return;
    }
    
    fetch(`/api/reports/courses-per-student/${student_id}`)
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('reports-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        list.innerHTML = `
            <h3>${data.data.student_name} (${data.data.department})</h3>
            <p><strong>Total Courses:</strong> ${data.data.total_courses}</p>
            <hr>
            ${data.data.courses.map(c => `
                <div class="item">
                    <div class="item-info">
                        <p><strong>${c.course_name}</strong></p>
                        <p><strong>Instructor:</strong> ${c.instructor}</p>
                        <p><strong>Grade:</strong> ${c.grade || 'Not yet assigned'}</p>
                    </div>
                </div>
            `).join('')}
        `;
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function reportInstructorWorkload() {
    fetch('/api/reports/instructor-workload')
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('reports-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        list.innerHTML = `
            <h3>Instructors - Workload</h3>
            <hr>
            ${data.data.map(w => `
                <div class="item">
                    <div class="item-info">
                        <p><strong>${w.name}</strong> (${w.department})</p>
                        <p>Courses: ${w.total_courses} | Total Students: ${w.total_students}</p>
                    </div>
                </div>
            `).join('')}
        `;
    })
    .catch(err => showMessage('Error: ' + err, 'error'));
}

function reportDepartmentStatistics() {
    fetch('/api/reports/department-statistics')
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('reports-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        list.innerHTML = `
            <h3>Department Statistics</h3>
            <hr>
            ${data.data.map(d => `
                <div class="item">
                    <div class="item-info">
                        <p><strong>${d.department}</strong></p>
                        <p>Students: ${d.total_students} | Instructors: ${d.total_instructors}</p>
                    </div>
                </div>
            `).join('')}
        `;
    })
    .catch(err => showMessage('Hata: ' + err, 'error'));
}

function reportGradeDistribution() {
    const course_id = parseInt(document.getElementById('report-grade-course-id').value);
    
    if (!course_id) {
        showMessage('Please enter course ID!', 'error');
        return;
    }
    
    fetch(`/api/reports/grade-distribution/${course_id}`)
    .then(r => r.json())
    .then(data => {
        const list = document.getElementById('reports-list');
        if (!data.success) {
            list.innerHTML = `<p class="error">${data.message}</p>`;
            return;
        }
        
        const dist = data.data.grade_distribution;
        list.innerHTML = `
            <h3>${data.data.course_name} - Grade Distribution</h3>
            <p><strong>Total Students:</strong> ${data.data.total_students}</p>
            <hr>
            <table>
                <thead>
                    <tr>
                        <th>Grade</th>
                        <th>Number of Students</th>
                    </tr>
                </thead>
                <tbody>
                    ${Object.entries(dist).map(([grade, count]) => `
                        <tr>
                            <td><strong>${grade}</strong></td>
                            <td>${count}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    })
    .catch(err => showMessage('Hata: ' + err, 'error'));
}
