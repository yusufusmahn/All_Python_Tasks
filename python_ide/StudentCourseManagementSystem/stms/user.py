class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.email},{self.password},{self.name}\n")


