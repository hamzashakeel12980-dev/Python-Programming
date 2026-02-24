#inheritance
class animal():
    def eat(self):
        print("Animal is eating")
class dog(animal):
    def bark(self):
        print("Dog is barking")
dog1 = dog()
dog1.eat()  # Output: Animal is eating
dog1.bark()  # Output: Dog is barking
