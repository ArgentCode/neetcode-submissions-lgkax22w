SELECT student_id, MIN(exam_id) exam_id, score
FROM exam_results e
WHERE score = (SELECT MAX(score) FROM exam_results where student_id = e.student_id)
GROUP BY student_id, score
ORDER BY student_id;