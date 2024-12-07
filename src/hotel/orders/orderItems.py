from hotel.menu.menuItem import MenuItem
from utils import getLogger
from logging import Logger

logger: Logger = getLogger("hotel.orderItems")

class OrderItem(MenuItem):
    _quantity = 0
    def __init__(self, name, description, price, quantity):
        logger.debug("init OrderItem: entry")
        super().__init__(name, description, price)
        self._quantity = quantity
        logger.debug("init OrderItem: exit")

        def __str__(self):
            return self.getName() + ": " + str(self._quantity)
        
        def __repr__(self) -> str:
            return f"foodItem: {self.getName()}, price: {self._price}"
        
        def getQuantity(self):
            return self._quantity

        def setQuantity(self, quantity):
            self._quantity = quantity

        def create(name, description, price, quantity):
            logger.info("Creating OrderItem")
            if name == None or description == None or price == None or quantity == None:
                name =  input("Enter food item name: ")
                description = input("Enter food item description: ")
                price = input("Enter price:")
                quantity = input("Enter quantity:")
            return OrderItem(name, description, price, quantity)

class OrderItems(OrderItem):
    _orderItems = []
    def __init__(self):
        self._orderItems = []
    
    def addOrderItem(self, orderItem):
        self._orderItems.append(orderItem)