print("Welcome to the Student Data Organizer!")
print("Manage student records with ID, name, age, grade, DOB, and subjects.")

students = []  # List to store all student records

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            # Add Student
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            subjects_input = input("Enter Subjects (comma-separated): ")
            subjects = [s.strip() for s in subjects_input.split(",")]

            # Tuple for immutable ID and DOB
            identity = (student_id, dob)

            # Dictionary for student data
            student_data = {
                "identity": identity,
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects
            }

            students.append(student_data)
            print("Student added successfully!")

        case "2":
            # Display All Students
            if not students:
                print("No student records found.")
            else:
                print("\n--- Student Records ---")
                for s in students:
                    sid, dob = s["identity"]
                    print(f"Student ID: {sid} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
                    print(f"Date of Birth: {dob}")
                    print("Subjects:", ", ".join(s["subjects"]))
                    print("-" * 40)

        case "3":
            # Update Student Info
            sid = input("Enter Student ID to update: ")
            for s in students:
                if s["identity"][0] == sid:
                    s["age"] = int(input("Enter new Age: "))
                    s["grade"] = input("Enter new Grade: ")
                    new_subjects = input("Enter new Subjects (comma-separated): ")
                    s["subjects"] = [sub.strip() for sub in new_subjects.split(",")]
                    print("Student information updated.")
                    break
            else:
                print("Student not found.")

        case "4":
            # Delete Student
            sid = input("Enter Student ID to delete: ")
            for i, s in enumerate(students):
                if s["identity"][0] == sid:
                    del students[i]
                    print("Student deleted successfully.")
                    break
            else:
                print("Student not found.")

        case "5":
            # Display Subjects Offered
            subject_set = set()
            for s in students:
                subject_set.update(s["subjects"])
            print("Subjects Offered:")
            for sub in sorted(subject_set):
                print("-", sub)

        case "6":
            print("Thank you for using the Student Data Organizer. Goodbye!")
            break

        case _:
            print("Invalid choice. Please try again.")
