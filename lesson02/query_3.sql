SELECT g.group_id, AVG(grades.grade) AS average_grade
FROM groups g
JOIN students s ON g.group_id = s.group_id
JOIN grades ON s.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE subjects.subject_id = 1
GROUP BY g.group_id;