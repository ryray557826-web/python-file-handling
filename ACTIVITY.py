import os

program = True
students = []

filename = 'Student List.txt'

# Load from file at the start
if os.path.exists(filename):
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(', ')
            if len(parts) == 3:
                name = parts[0].split(': ')[1]
                student_id = parts[1].split(': ')[1]
                course = parts[2].split(': ')[1]
                students.append({'name': name, 'id': student_id, 'course': course})

while program:
    print('\n===== Student Information System =====')
    print("""
    1. Add Student 
    2. Display Students
    3. Update Student
    4. Delete Student
    5. Save to File
    6. Load from File
    7. Exit
    """)
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue

    if choice == 1:
        print('You have chosen to Add a student')
        name = input('Input Student Name: ').strip().capitalize()
        student_id = input('Input Student ID: ').strip()
        course = input('Input Student Course: ').strip().upper()
        students.append({'name': name, 'id': student_id, 'course': course})
        print('Student added successfully.')

    elif choice == 2:
        print('\n===== Display Students =====')
        if not students:
            print("No students to display.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"{i}. Name: {student['name']}, ID: {student['id']}, Course: {student['course']}")

    elif choice == 3:
        print('\n===== Update Student =====')
        sid = input("Enter Student ID to update: ").strip()
        found = False
        for student in students:
            if student['id'] == sid:
                print(f"Current info: Name: {student['name']}, Course: {student['course']}")
                student['name'] = input("Enter new name: ").strip().capitalize()
                student['course'] = input("Enter new course: ").strip().upper()
                print("Student updated successfully.")
                found = True
                break
        if not found:
            print("Student ID not found.")

    elif choice == 4:
        print('\n===== Delete Student =====')
        sid = input("Enter Student ID to delete: ").strip()
        for student in students:
            if student['id'] == sid:
                students.remove(student)
                print("Student deleted successfully.")
                break
        else:
            print("Student ID not found.")

    elif choice == 5:
        print('\n===== Save to File =====')
        with open(filename, 'w') as f:
            for student in students:
                line = f"Student Name: {student['name']}, ID: {student['id']}, Course: {student['course']}\n"
                f.write(line)
        print("Data saved successfully.")

    elif choice == 6:
        print('\n===== Load from File =====')
        students.clear()
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(', ')
                    if len(parts) == 3:
                        name = parts[0].split(': ')[1]
                        student_id = parts[1].split(': ')[1]
                        course = parts[2].split(': ')[1]
                        students.append({'name': name, 'id': student_id, 'course': course})
            print("Data loaded successfully.")
        else:
            print("File not found.")

    elif choice == 7:
        print("Exiting the Student Information System. Goodbye!")
        program = False

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
