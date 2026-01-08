DROP TABLE IF EXISTS enrollment;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS instructor;
DROP TABLE IF EXISTS student;

CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    department VARCHAR(50)
);

CREATE TABLE instructor (
    instructor_id SERIAL PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    department VARCHAR(50)
);

CREATE TABLE course (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    instructor_id INT REFERENCES instructor(instructor_id)
);

CREATE TABLE enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id),
    course_id INT REFERENCES course(course_id),
    grade VARCHAR(2)
);

--data
INSERT INTO student (fname, lname, department) VALUES
('Merve', 'Karatas', 'Computer Engineering'),
('Kevser', 'Kutlu', 'Software Engineering'),
('Zeynep', 'Muratoglu', 'Electrical Engineering'),
('Burak', 'Kara', 'Industrial Engineering'),
('Elif', 'Metin', 'Computer Engineering'),
('Ahmet', 'Sahin', 'Mathematics'),
('Zeynep', 'Arslan', 'Software Engineering'),
('Mehmet', 'Aydin', 'Computer Engineering'),
('Sena', 'Guler', 'Economics'),
('Eren', 'Polat', 'Computer Engineering');

INSERT INTO instructor (fname, lname, department) VALUES
('Hakan', 'Ersoy', 'Computer Engineering'),
('Selin', 'Yildiz', 'Software Engineering'),
('Cem', 'Acar', 'Electrical Engineering'),
('Gozde', 'Turan', 'Industrial Engineering'),
('Onur', 'Korkmaz', 'Mathematics');

INSERT INTO course (course_name, instructor_id) VALUES
('Database Systems', 1),
('Algorithms', 1),
('Web Programming', 2),
('Object-Oriented Programming', 2),
('Circuit Analysis', 3),
('Microcontrollers', 3),
('Operations Research', 4),
('Engineering Economics', 4),
('Calculus I', 5),
('Linear Algebra', 5);

INSERT INTO enrollment (student_id, course_id, grade) VALUES
(1, 1, 'AA'), (1, 2, 'BB'), (1, 3, 'BA'),
(2, 1, 'CC'), (2, 4, 'BB'),
(3, 5, 'BA'), (3, 6, 'AA'),
(4, 7, 'CB'), (4, 8, 'BB'),
(5, 1, 'AA'), (5, 3, 'BA'), (5, 4, 'CB'),
(6, 9, 'CC'), (6, 10, 'BA'),
(7, 2, 'AA'), (7, 3, 'BB'),
(8, 1, 'BA'), (8, 2, 'CB'), (8, 3, 'BB'),
(9, 7, 'AA'), (9, 8, 'BA'),
(10, 1, 'BB'), (10, 9, 'AA'), (10, 3, 'BA');


--control
SELECT * FROM student;
SELECT * FROM instructor;
SELECT * FROM course;
SELECT * FROM enrollment;


CREATE VIEW student_course_list AS
SELECT 
    s.fname AS student_first_name, 
    s.lname AS student_last_name, 
    c.course_name,
    e.grade
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
JOIN course c ON e.course_id = c.course_id;

CREATE VIEW instructor_workload AS
SELECT 
    i.fname AS instructor_first_name, 
    i.lname AS instructor_last_name, 
    COUNT(c.course_id) AS total_courses
FROM instructor i
LEFT JOIN course c ON i.instructor_id = c.instructor_id
GROUP BY i.instructor_id, i.fname, i.lname;
