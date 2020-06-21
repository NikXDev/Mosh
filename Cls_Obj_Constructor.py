class Person:
    def __init__(self, name):  # entered input variable
        self.name = name  # joined input variable with self to get input from user

    def talk(self):
        return f"Talk Function Is Activated Miss {self.name}"
# print() brings None At the Output screen


# obj 1
a = Person("Samayra")  # created an obj and stored it in a variable
print(a.name)
print(a.talk())  # dropdown list mentions talk() as defined in Person along with other stuff

print("....................")

# obj 2
b = Person("Bobby")
print(b.name)
print(b.talk())
