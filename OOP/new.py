# class character:
#     def __init__(self, name, health, attack):
#         self.name = name
#         self.health = health
#         self.attack = attack

#     def attack_enemy(self):
#         print(self.name + " attacks with power " + str(self.attack) + " damage!")   
# warrior = character("Thor", 100, 50)
# mage = character("Gandalf", 80, 70)

# warrior.attack_enemy()
# mage.attack_enemy()
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

person1 = Human("Hamza", 22, "Male")
person2 = Human("Sitara", 20, "Female")
person3 = Human("Ali", 25, "Male")
person1.introduce()
person2.introduce()
person3.introduce()