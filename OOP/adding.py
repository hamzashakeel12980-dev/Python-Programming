class car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color
    def display_details(self):
        print(f'This car is a {self.color} {self.brand}. ')

car1 = car()
car1.set_details("Toyota", "Red")
car1.display_details()
car2 = car()
car2.set_details("Honda", "Blue")
car2.display_details()
