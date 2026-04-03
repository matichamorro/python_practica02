students = [
    {"name": " Ana García ", "grade": "8", "status":
    "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status":
    "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status":
    "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status":
    "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status":
    "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status":
    "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status":
    "desaprobado"},
    {"name": " ", "grade": "5}", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status":
    "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status":
    "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status":
    "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status":
    "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status":
    "ausente"},
    {"name": "roberto díaz", "grade": "", "status":
    "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status":
    "aprobado"},
    {"name": " laura méndez", "grade": "8", "status":
    "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status":
    "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status":
    "Desaprobado"}
]


def standardise_students(students):
    banned_entries = [None, "''", " "]
    standardised_students = []
    
    for student in students:
        if student['name'] not in banned_entries:
            if student['grade'] not in banned_entries and student['grade'].isdigit():
                standardised_students.append(
                                        {"name": student['name'], 
                                        "grade": student['grade'],
                                        "status": student['status'] }
                )
        
    for student in standardised_students:
        student["name"] = student["name"].strip().title()
        student["status"] = student["status"].title()
    
    standardised_students.sort(key=lambda student: student['name'])
    
    best_notes = {}
    for student in standardised_students:
        name = student["name"]
        grade = student["grade"]
        status = student["status"]
        if name not in best_notes or int(grade) > best_notes[name][0]:
            best_notes[name] = (int(grade), status)
            
            
    print("\nRegistros limpios de alumnos:")
    print("Nombre                Nota       Estado")
    print("-------------------------------------------------")
    for student in best_notes:        
        print(f"{student:<15}       {best_notes[student][0]:<4}       {best_notes[student][1]:<11}")
    
    
    print(f"\nTotal de alumnos válidos: {len(best_notes)}")
    