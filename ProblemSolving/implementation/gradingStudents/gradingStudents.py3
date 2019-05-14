def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38:
            continue
        elif grades[i] % 5 >= 3:
            grades[i] += 5 - (grades[i] % 5)
    return grades
    
