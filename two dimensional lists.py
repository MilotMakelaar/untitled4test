studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gem_cijfer = []
    for item in studentencijfers:
        gem_Per_Student = sum(item) / len(item)
        gem_cijfer.append(gem_Per_Student)
    return gem_cijfer

def gemiddelde_van_alle_studenten(studentencijfers):
    gem_Cijfer_Student = gemiddelde_per_student(studentencijfers)
    gem_Per_Student = sum(gem_Cijfer_Student) / len(gem_Cijfer_Student)
    return gem_Per_Student

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))