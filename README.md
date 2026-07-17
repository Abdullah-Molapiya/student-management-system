# Student Management System

## Project Description

This project is a simple Student Management System developed in Python. It demonstrates the use of Git, GitHub, GitHub Actions, and pytest for version control, collaboration, automated testing, and continuous integration.

## Features

- Add a student
- Remove a student
- Search for a student
- Update student information

## Project Structure

```
student-management-system/
│── student.py
│── test_student.py
│── requirements.txt
│── README.md
└── .github/
    └── workflows/
        └── python.yml
```

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah-Molapiya/student-management-system.git
```

### 2. Navigate to the project folder

```bash
cd student-management-system
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

### 4. Run the test cases

```bash
pytest
```

## Git Commands Used

The following Git commands were used during the development of this project:

```bash
git init
git status
git add .
git commit -m "Initial commit with student management system and tests"

git branch feature-student-search
git checkout feature-student-search

git add student.py
git commit -m "Modified search_student implementation"

git push -u origin main
git push -u origin feature-student-search

git add .github/workflows/python.yml
git commit -m "Add GitHub Actions workflow"

git commit -m "Introduced bug for testing"
git commit -m "Fixed add_student implementation"

git push
```

## GitHub Actions Workflow

GitHub Actions is configured to run automatically on every **push** and **pull request**.

The workflow performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Runs all pytest test cases.
5. Reports whether the workflow passed or failed.

A bug was intentionally introduced to verify that the workflow detected the failure. After fixing the bug, the workflow passed successfully.

## Testing

The project contains 10 pytest test cases covering:

- Add student
- Search existing student
- Search non-existing student
- Remove student
- Remove non-existing student
- Update existing student
- Update non-existing student
- Add multiple students
- Update one student without affecting others
- Remove one student without affecting others

## Repository

GitHub Repository:
https://github.com/Abdullah-Molapiya/student-management-system