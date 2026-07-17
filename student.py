students = {}

def add_student(student_id, student_name):
    students[student_id] = student_name

def remove_student(student_id):
    if student_id in students:
        del students[student_id]

def search_student(student_id):
    if student_id in students:
        return students[student_id]
    return None

def update_student(student_id, student_name):
    if student_id in students:
        students[student_id] = student_name

def export_students():
    return students.copy()