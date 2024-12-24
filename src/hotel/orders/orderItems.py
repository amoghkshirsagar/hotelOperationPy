from hotel.menu.menuItem import MenuItem
from utils import getLogger
from logging import Logger

logger: Logger = getLogger("hotel.orderItems")


class OrderItem(MenuItem):
    _quantity = 0
    def __init__(self, menuItem: MenuItem, quantity):
        logger.debug("init OrderItem: entry")
        super().__init__(menuItem.name, menuItem.description, menuItem.price)
        self._quantity = quantity
        logger.debug("init OrderItem: exit")

        def __str__(self):
            return self.name + ": " + str(self._quantity)
        
        def __repr__(self) -> str:
            return f"foodItem: {self.name}, price: {self._price}"
        
        def getQuantity(self):
            return self._quantity

        def setQuantity(self, quantity):
            self._quantity = quantity

class Order:
    _orderItems: list[OrderItem] = []
    _orderNumber = 0
    def __init__(self, orderNumber):
        self._orderItems = []
        self._orderNumber = orderNumber
    
    def addOrderItem(self, orderItem: OrderItem):
        self._orderItems.append(orderItem)
    
    def getOrderNumber(self):
        return self._orderNumber

class Orders:
    _orders = []
    _activeOrder: Order = None
    def __init__(self):
        self._orders = []
        _activeOrder = None
    
    def addOrder(order):
        Orders._orders.append(order)
    
    def create() -> 'Orders':
        if Orders._orders is None:
            Orders._orders = Orders()
        return Orders._orders

    def createOrder():
        order: Order = Order(len(Orders._orders)+1)
        Orders.addOrder(order)
        Orders._activeOrder = order
        logger.info(f"Created order {order._orderNumber}")
        return Orders._activeOrder
    
    def activeOrder():
        for order in Orders._orders:
            if order == Orders._activeOrder:
                return order._orderNumber

    def setActiveOrder(orderNumber):
        logger.info(f"Setting active order to {orderNumber}")
        for order in Orders._orders:
            if order._orderNumber == int(orderNumber):
                Orders._activeOrder = order
                return
        
        logger.info(f"No order found with number {orderNumber}")
        Orders._activeOrder = None
        