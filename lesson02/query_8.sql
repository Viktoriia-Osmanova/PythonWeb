SELECT teacher_id, AVG(grade) as avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE subjects.teacher_id = 1
GROUP BY teacher_id;
