"""
one aneme, multiple forms
Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). Polymorphism can be achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass. This allows for dynamic method dispatch, where the appropriate method is called based on the actual type of the object at runtime."""
#polymorphism with classes method overriding
class animal:
    def sound(self):
        print("Animal makes a sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class cat(animal):
    def sound(self):
        print("Cat meows")
animal1 = animal()
dog1 = dog()
cat1 = cat()
animal1.sound()  # Output: Animal makes a sound
dog1.sound()     # Output: Dog barks
cat1.sound()     # Output: Cat meows