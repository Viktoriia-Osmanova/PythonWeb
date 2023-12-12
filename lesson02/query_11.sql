SELECT teacher_id, student_id, AVG(grade) as avg_grade
FROM grades
WHERE teacher_id = 1 AND student_id = 1
GROUP BY teacher_id, student_id;
