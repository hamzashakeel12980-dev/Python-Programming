warrior_name = "Thor"
warrior_health = 100
warrior_attack = 50

mage_name = "Gandalf"
mage_health = 80
mage_attack = 70

def attack_warrior():
    print(warrior_name + " attacks with power " + str(warrior_attack) + " damage!")
def attack_mage():
    print(mage_name + " attacks with power " + str(mage_attack) + " damage!")

attack_warrior()
attack_mage()

# problem is redundant code, we can use OOP to solve this problem.
# hard to maintain and update code, if we want to change something we have to change in multiple places.
# not sturctured code, we have to keep track of multiple variables and functions.