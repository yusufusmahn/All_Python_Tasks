from StudentCourseManagementSystem.stms.user import User

class Student(User):
    def __init__(self, email, password, name):
        super().__init__(email, password, name)


    def register(self):
        self.save_to_file('../data/students.txt')
        return True



    def get_instructor_name(self, instructor_email):
        try:
            with open('..\data\instructors.txt', 'r') as instructor_file:
                for exits in instructor_file:
                    email, _, instructor_name = exits.strip().split(',')
                    if email == instructor_email:
                        return instructor_name
        except FileNotFoundError:
            print("record not found")
        return "Unknown Instructor"



    def view_courses(self):
        courses = []
        try:
            with open('..\data\enrollments.txt', 'r') as file:
                for exists in file:
                    student_email, course_code = exists.strip().split(',')
                    if student_email == self.email:
                        with open('..\data\courses.txt', 'r') as course_file:
                            for exists in course_file:
                                code, name, instructor_email = exists.strip().split(',')
                                if code == course_code:
                                    instructor_name = self.get_instructor_name(instructor_email)
                                    courses.append((code, name, instructor_name))
        except FileNotFoundError:
            print("record not found")
        return courses


    def view_grades(self):
        grades = []
        try:
            with open('../data/grades.txt', 'r') as grade_file:
                for exists in grade_file:
                    student_email, course_code, grade = exists.strip().split(',')
                    if student_email == self.email:
                        grades.append((course_code, grade))
        except FileNotFoundError:
            print("record not found")
        return grades