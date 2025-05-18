from StudentCourseManagementSystem.stms.user import User

class Student(User):
    def __init__(self, email, password, name):
        super().__init__(email, password, name)


    def register(self):
        self.save_to_file('../data/students.txt')
        return True


    def view_courses(self):
        courses = []
        try:
            with open('../data/enrollments.txt', 'r') as file:
                for exists in file:
                    student_email, course_code = exists.strip().split(',')
                    if student_email == self.email:
                        with open('../data/courses.txt', 'r') as course_file:
                            for exists in course_file:
                                code, name, instructor_email = exists.strip().split(',')
                                if code == course_code:
                                    courses.append((code, name, instructor_email))
        except FileNotFoundError:
            pass
        return courses


    def view_grades(self):
        grades = []
        try:
            with open('../data/grades.txt', 'r') as f:
                for line in f:
                    student_email, course_code, grade = line.strip().split(',')
                    if student_email == self.email:
                        grades.append((course_code, grade))
        except FileNotFoundError:
            pass
        return grades