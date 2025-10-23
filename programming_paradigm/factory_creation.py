class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
         return cls(name, 0)

child = Person.create_child("Alice")
print(child.name)
print(child.age)

