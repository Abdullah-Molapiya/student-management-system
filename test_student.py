from student import (students,
add_student, remove_student, search_student, update_student,
export_students)

def setup_function():
    students.clear()

def test_add_student():
    add_student(1, "Abdullah")
    assert students[1] == "Abdullah"

def test_search_student():
    add_student(1, "Abdullah")
    assert search_student(1) == "Abdullah"

def test_search_student_not_found():
    assert search_student(10) is None

def test_remove_student():
    add_student(1, "Abdullah")
    remove_student(1)
    assert search_student(1) is None

def test_remove_student_not_found():  # Removing a Student That Doesn't Exist
    remove_student(10)  # Should not raise an error
    assert search_student(10) is None

def test_update_student():
    add_student(1, "Aryan")
    update_student(1, "Abdullah")
    assert search_student(1) == "Abdullah"

def test_update_student_not_found():  # Update a Student That Doesn't Exist
    update_student(10, "Zeeshan")
    assert search_student(10) is None

def test_add_multiple_students():  # Add multiple students and verify they are stored correctly
    add_student(1, "Abdullah")
    add_student(2, "Zeeshan")
    add_student(3, "Aryan")

    assert search_student(1) == "Abdullah"
    assert search_student(2) == "Zeeshan"
    assert search_student(3) == "Aryan"

def test_update_one_student():
    add_student(1, "Abdullah")
    add_student(2, "Rahul")

    update_student(2, "Zeeshan")

    assert search_student(1) == "Abdullah"
    assert search_student(2) == "Zeeshan"

def test_remove_one_student():
    add_student(1, "Abdullah")
    add_student(2, "Zeeshan")

    remove_student(2)

    assert search_student(1) == "Abdullah"
    assert search_student(2) is None

def test_export_students():
    add_student(101, "Abdullah")
    add_student(102, "Zeeshan")

    exported = export_students()

    assert exported == {
        101: "Abdullah",
        102: "Zeeshan"
    }

def test_export_students_empty():
    assert export_students() == {}