DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    group_id INT
);

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(50)
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(50),
    teacher_id INT
);

DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT,
    date_received DATE
);
