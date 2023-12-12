SELECT students.name AS student_name, grades.grade, subjects.subject_name
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
JOIN groups ON students.group_id = groups.group_id
WHERE groups.group_id = 1 AND subjects.subject_id = 1;
