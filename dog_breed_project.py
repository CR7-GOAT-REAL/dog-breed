class Dog():
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


    def breed(self):
        print("My breed is ",  self.breed)


class Animal(Dog):
    def __init__(self, breed, color):

p1 = Dog() 