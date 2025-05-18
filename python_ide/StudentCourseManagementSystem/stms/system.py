from StudentCourseManagementSystem.stms.instructor import Instructor
from StudentCourseManagementSystem.stms.student import Student

class System:
    def __init__(self):
        self.current_user = None


    def email_exists(self, email, filename):
        try:
            with open(filename, 'r') as file:
                for exists in file:
                    if exists.split(',')[0] == email:
                        return True
        except FileNotFoundError:
            return False
        return False


    def is_email_unique(self, email):
        student_file = f"../data/students.txt"
        instructor_file = f"../data/instructors.txt"

        if self.email_exists(email, student_file):
            print(f" Email: {email} already exists for a student.")
            return False

        if self.email_exists(email, instructor_file):
            print(f"Email: {email} already exists for an instructor.")
            return False
        return True



    def login(self, email, password, filename):
        try:
            with open(filename, 'r') as file:
                for exists in file:
                    user_data = exists.strip().split(',')
                    if user_data[0] == email and user_data[1] == password:
                        return user_data
        except FileNotFoundError:
            return None
        return None



    def register(self, email, password, name, user_type):

        if user_type == 'student':
            result = self.register_student(email, password, name)
        elif user_type == 'instructor':
            result = self.register_instructor(email, password, name)
        else:
            print(f"Registration failed: Invalid user type {user_type}.")
            return False

        if result:
            print(f"Successfully registered {user_type}: {name}")
        return result


    def register_student(self, email, password, name):
        student = Student(email, password, name)
        return student.register()



    def register_instructor(self, email, password, name):
        instructor = Instructor(email, password, name)
        return instructor.register()



    def enroll_student(self, student_email, course_code):
        try:
            if self.email_exists(student_email, '../data/students.txt'):
                with open('../data/courses.txt', 'r') as file:
                    for exists in file:
                        code, _, _ = exists.strip().split(',')
                        if code == course_code:
                            with open('../data/enrollments.txt', 'a') as enroll_file:
                                enroll_file.write(f"{student_email},{course_code}\n")
                                return True
            return False
        except FileNotFoundError:
            return False


    def create_course(self, code, name):
        if isinstance(self.current_user, Instructor):
            return self.current_user.create_course(code, name)
        print("Only instructor can create courses.")
        return False