grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
name = sorted(students)
grade_0 = sum(grades[0]) / len(grades[0])
grade_1 = sum(grades[1]) / len(grades[1])
grade_2 = sum(grades[2]) / len(grades[2])
grade_3 = sum(grades[3]) / len(grades[3])
grade_4 = sum(grades[4]) / len(grades[4])
students_grades = { name[0] : grade_0, name[1] : grade_1, name[2] : grade_2, name[3] : grade_3, name[4] : grade_4}
print(students_grades)