class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, ", self.name)

p1 = Person("Allan")
p1.say_hello()

p2 = Person("John")
p2.say_hello()
