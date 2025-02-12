class Car:
    def move(self):
        print("Moving...")

    def ride(self):
        print("Riding...")

car1 = Car()
car1.move()
car1.ride()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()
john.name = "Sarah"
print(john.name)

ana = Person("Ana Markovic")
ana.talk()


# Learning inheritance

class Snake:
    def move(self):
        print("Moving like a snake...")


class Dog(Snake):
    def bark(self):
        print("Barking like a dog...")

class Cat(Snake):
    pass


dog1 = Dog()
dog1.move()
dog1.bark()

cat1 = Cat()
cat1.move()




















































