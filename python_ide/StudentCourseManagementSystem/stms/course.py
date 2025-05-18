class Course:
    def __init__(self, code, name, instructor_email):
        self.code = code
        self.name = name
        self.instructor_email = instructor_email

    def save_to_file(self):
        with open('../data/courses.txt', 'a') as file:
            file.write(f"{self.code},{self.name},{self.instructor_email}\n")


    def code_exists(self, code):
        try:
            with open('../data/courses.txt', 'r') as file:
                for exists in file:
                    if exists.split(',')[0] == code:
                        return True
        except FileNotFoundError:
            return False
        return False