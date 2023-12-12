SELECT student_id, grade
FROM grades
WHERE subject_id = 1 AND group_id = 1
ORDER BY date_received DESC
LIMIT 1;
