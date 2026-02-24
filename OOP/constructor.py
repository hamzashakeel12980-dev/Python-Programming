#constructor
class student():
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
student1 = student("Hamza", 22, 85)
print("Hello, my name is " + student1.name + ", I am " + str
(student1.age) + " years old, and my marks are " + str(student1.marks))

"""
syntax of constructor:
class ClassName:
    def __init__(self, parameters):
        self.attribute1 = value1
        self.attribute2 = value2
        ...
        self.attributen = value
        object_name = ClassName(arguments)
        In the above syntax, the __init__ method is the constructor that initializes the attributes of the class. The self parameter refers to the instance of the class being created. The parameters in the __init__ method are used to set the values of the attributes when an object is instantiated."""

"""
Types of constructors:
1. Default Constructor: A constructor that takes no parameters and initializes the attributes with default values.
2. Parameterized Constructor: A constructor that takes parameters to initialize the attributes with specific values.
3. Copy Constructor: A constructor that creates a new object as a copy of an existing object.
4. Static Constructor: A constructor that is called only once when the class is loaded, and
is used to initialize static attributes of the class.
5. Private Constructor: A constructor that is declared as private and can only be accessed within the class, preventing the creation of objects from outside the class.
6. Destructor: A special method that is called when an object is destroyed, used to perform cleanup operations.
7. Class Method Constructor: A constructor that is defined as a class method and can be called on the class itself, rather than on an instance of the class.
8. Factory Method Constructor: A constructor that is defined as a static method and is used to create instances of the class based on certain conditions or parameters.
9. Abstract Constructor: A constructor that is defined in an abstract class and must be implemented by any concrete subclass that inherits from the abstract class.
10. Multiple Constructors: A class can have multiple constructors with different parameter lists, allowing for different ways to create objects of the class.

"""