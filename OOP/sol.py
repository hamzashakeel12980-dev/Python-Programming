class student():
    def set_details(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

student1 = student()
student1.set_details("Hamza", 22, 85)
print("Hello, my name is " + student1.name + ", I am " + str(student1.age) + " years old, and my marks are " + str(student1.marks))
