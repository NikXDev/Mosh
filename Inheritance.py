class Mammal():  # parent class
    def walk(self):
        return ("Walk Walk")


class Dog(Mammal):  # inherited Mammal class functions
    pass  # to avoid error as we cant leave a class empty


class Cat(Mammal):
    pass


class Mouse:
    def noisy(self):
        return "Okkkkuuuuuuuuuuurr!"


a = Dog()
print(a.walk())
print(".......................")
b = Cat()
print(b.walk())
print(".......................")
c = Mouse()
print(c.noisy())


