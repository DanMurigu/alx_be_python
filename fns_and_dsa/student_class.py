class Student:
    def __init__(self, name="", age=0):
        self.age = age
        self.name = name

    def get_details(self):
        self.name = input("Whats your name? ")
        self.age = int(input("Whats your age? "))

    def display_details(self):
        print(f"I am{self.name} and I am {self.age} Year's old.")

student1 = Student()
student1.get_details()
student1.display_details()