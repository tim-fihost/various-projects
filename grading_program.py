student_score = {
    "Harry":81,
    "Rob":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
student_grade = {}
for name in student_score:
    if student_score[name] > 91 or student_score[name] <= 100:
        student_grade[name] = f"{student_score[name]} = Outstading"
    if student_score[name] > 81 or student_score[name] <= 90:
        student_grade[name] = f"{student_score[name]} = Great"
    if student_score[name] > 71 or student_score[name] <= 80:
        student_grade[name] = f"{student_score[name]} = Exceeds Expectations"
    if student_score[name] > 60 or student_score[name] <= 70:
        student_grade[name] = f"{student_score[name]} = Acceptable"
    if student_score[name] <60:
        student_grade[name] = f"{student_score[name]} = Fail"
for i in student_grade.items():
    print(i)