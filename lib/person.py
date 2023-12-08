

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")


my_person = Person("Alice", 25)
my_person.talk()
my_person.walk()
