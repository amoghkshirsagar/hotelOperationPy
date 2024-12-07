from hotel.menu.foodItem import FoodItem
from utils import getLogger
from logging import Logger

logger: Logger = getLogger("hotel.menuItem")

class MenuItem(FoodItem):
    _price = ""
    def __init__(self, name, description, price):
        logger.debug("init MenuItem: entry")
        super().__init__(name, description)
        self._price = price
        logger.debug("init MenuItem: exit")

    def __str__(self):
        return self.getName() + ": " + str(self._price)

    def __repr__(self) -> str:
        return f"foodItem: {self.getName()}, price: {self._price}"

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price
    
    def create(name, description, price):
        logger.info("Creating MenuItem")
        if name == None or description == None or price == None:
            name =  input("Enter food item name: ")
            description = input("Enter food item description: ")
            price = input("Enter price:")  
        return MenuItem(name, description, price)