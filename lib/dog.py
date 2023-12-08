class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")


# Test the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
my_dog.sit()
