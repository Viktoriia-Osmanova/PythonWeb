SELECT DISTINCT subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 1;
