class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Чик-чирик")

    def eat(self):
        print(f"{self.name} ест семечки")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Привет, я млекопитающее животное")

    def eat(self):
        print("Ест мясо")

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("рррррр")

    def eat(self):
        print("Ест рыбу")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name} {animal.age} лет")

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            print(employee.name, employee.age)

class ZooKeeper:
    def __init__(self, name, age):
          self.name = name
          self.age = age
    def feed_animal(self, animal):
        animal.eat()
        print(f"{zookeeper.name} покормил {animal.name}")
class Veterinarian():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self, animal):
        animal.make_sound()

straus = Bird("Страус", 5)
zookeeper = ZooKeeper("Вася", 30)
veterinarian = Veterinarian("Маша", 25)
zoo = Zoo()
zoo.add_animal(straus)
zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)
zoo.display_animals()
zoo.display_employees()
zookeeper.feed_animal(straus)