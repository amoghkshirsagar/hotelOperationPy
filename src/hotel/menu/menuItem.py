from hotel.menu.foodItem import FoodItem
import os

class MenuItem(FoodItem):
    _price = ""
    def __init__(self, name, description, price):
        super().__init__(name, description)
        self._price = price

    def __str__(self):
        return self.getName() + ": " + str(self._price)

    def __repr__(self) -> str:
        return f"foodItem: {self.getName()}, price: {self._price}"

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price
    
    def create():
        name =  input("Enter food item name: ")
        description = input("Enter food item description: ")
        price = input("Enter price: ")
        return MenuItem(name, description, price)