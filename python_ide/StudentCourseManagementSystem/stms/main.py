from StudentCourseManagementSystem.stms.instructor import Instructor
from StudentCourseManagementSystem.stms.system import System
from StudentCourseManagementSystem.stms.student import Student



def student_menu(system):
    while True:
        print("\nStudent Menu")
        print("1. View Enrolled Courses")
        print("2. View Grades")
        print("3. Enroll a Course")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            courses = system.current_user.view_courses()
            if courses:
                print("\nEnrolled Courses:")
                for code, name, instructor_email in courses:
                    print(f"Course Code: {code}, Course Name: {name}, Instructor: {instructor_email}")
            else:
                print("No courses enrolled")

        elif choice == '2':
            grades = system.current_user.view_grades()
            if grades:
                print("\nGrades:")
                for course_code, grade in grades:
                    print(f"Course Code: {course_code}, Grade: {grade}")
            else:
                print("No grades available.")


        elif choice == '3':
            course_code = input("Course Code: ").strip()
            if system.enroll_student(system.current_user.email, course_code):
                print("Enrolled in course successfully!")
            else:
                print("Enrollment failed.")


        elif choice == '4':
            system.current_user = None
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice!")


def instructor_menu(system):
    while True:
        print("\nInstructor Menu")
        print("1. Create Course")
        print("2. View Enrolled Students")
        print("3. Assign Grade")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            code = input("Course Code: ").strip()
            name = input("Course Name: ").strip()
            if system.create_course(code, name):
                print("Course created successfully!")
            else:
                print("Course creation failed: ")

        elif choice == '2':
            course_code = input("Enter Course Code: ").strip()
            students = system.current_user.view_enrolled_students(course_code)
            if students:
                print(f"\nStudents enrolled in {course_code}:")
                for email, name in students:
                    print(f"Email: {email}, Name: {name}")
            else:
                print("No students enrolled.")

        elif choice == '3':
            student_email = input("Student Email: ").strip()
            course_code = input("Course Code: ").strip()
            grade = input("Grade: ").strip()
            if system.current_user.assign_grade(student_email, course_code, grade):
                print("Grade assigned successfully!")
            else:
                print("Grade assignment failed.")

        elif choice == '4':
            system.current_user = None
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")


def main():
    system = System()
    while True:
        print("\nCourse Management System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            user_type = input("Enter user type (student/instructor): ").lower()
            if user_type not in ['student', 'instructor']:
                print("Invalid user type!")
                continue
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            filename = f"../data/{user_type}s.txt"
            user_data = system.login(email, password, filename)
            if user_data:
                name = user_data[2]
                print(f"Welcome, {name}!")
                if user_type == 'student':
                    system.current_user = Student(email, password, name)
                    student_menu(system)
                else:
                    system.current_user = Instructor(email, password, name)
                    instructor_menu(system)
            else:
                print("Invalid credentials!")


        elif choice == '2':
            user_type = input("Enter user type (student/instructor): ").lower()
            if user_type not in ['student', 'instructor']:
                print("Invalid user type!")
                continue
            while True:
                email = input("Enter Email: ").strip()
                if not email or '@' not in email:
                    print("Invalid email! Must be non-empty and contain '@'.")
                    continue
                if not system.is_email_unique(email):
                    print("please try a different email.")
                    continue
                break
            password = input("Enter Password: ").strip()
            if not password or password == email:
                print("Invalid password! Must be non-empty and different from email.")
                continue
            name = input("Enter Name: ").strip()
            if not name or name == password or name.isdigit():
                print("Invalid name! Must be non-empty, not a number, and different from password.")
                continue
            if system.register(email, password, name, user_type):
                print("Registration successful!")
            else:
                print("Registration failed!")


        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()