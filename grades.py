def grade(score):
    if score >= 80:
        return "Distinction"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

students = {"Amina": 85, "John": 62, "Grace": 45}

for name, score in students.items():
    print(name, "-", grade(score))
