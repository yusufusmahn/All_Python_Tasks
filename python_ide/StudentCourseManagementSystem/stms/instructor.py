from StudentCourseManagementSystem.stms.user import User
from StudentCourseManagementSystem.stms.course import Course

class Instructor(User):
    def __init__(self, email, password, name):
        super().__init__(email, password, name)

    def register(self):
        self.save_to_file('../data/instructors.txt')
        return True


    def create_course(self, code, name):
        course = Course(code, name, self.email)
        if not course.code_exists(code):
            course.save_to_file()
            return True
        return False


    def view_enrolled_students(self, course_code):
        students = []
        try:
            with open('../data/enrollments.txt', 'r') as file:
                for exists in file:
                    student_email, enrolled_course = exists.strip().split(',')
                    if enrolled_course == course_code:
                        with open('../data/students.txt', 'r') as sf:
                            for student_exists in sf:
                                email, _, name = student_exists.strip().split(',')
                                if email == student_email:
                                    students.append((email, name))
        except FileNotFoundError:
            pass
        return students


    def assign_grade(self, student_email, course_code, grade):
        try:
            with open('../data/enrollments.txt', 'r') as file:
                for exists in file:
                    email, code = exists.strip().split(',')
                    if email == student_email and code == course_code:
                        with open('../data/grades.txt', 'a') as grade_file:
                            grade_file.write(f"{student_email},{course_code},{grade}\n")
                        return True
        except FileNotFoundError:
            pass
        return False