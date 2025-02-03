from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard
from utils import getLogger
from logging import Logger
from utils.fileUtils import writeJson, readJson

logger: Logger = getLogger("hotel.orderItems")
OrderListLocation = "data/orderList.json"

def modifyOrderItemQty(id, qty):
    activeOrder = Orders.getActiveOrder()
    print(f"{activeOrder._orderNumber} : {id} -> {qty}")
    orderItem: OrderItem = activeOrder.getOrderItemById(id)
    quantity = orderItem.getQuantity()
    quantity = int(quantity) + qty
    orderItem.setQuantity(quantity=quantity)



class OrderItem:
    _id = 0
    _name = ""
    _description = ""
    _price = 0
    _quantity = 0
    def __init__(self, menuItem: MenuItem, quantity):
        logger.debug("init OrderItem: entry")
        self._name = menuItem._name
        self._description = menuItem._description
        self._price = menuItem._price
        self._quantity = quantity
        self._id = menuItem._id
        logger.debug("init OrderItem: exit")

    def __str__(self):
        return self.name + ": " + str(self._quantity)
    
    def __repr__(self) -> str:
        return f"foodItem: {self.name}, price: {self._price}"
    
    def getPrice(self):
        return self._price

    def getDescription(self):
        return self._description
    
    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id
        
    def setPrice(self, price):
        self._price = price

    def getQuantity(self):
        return self._quantity
    
    def setQuantity(self, quantity):
        self._quantity = quantity

    def createOrderItem(menuItem, quantity):
        logger.info("Creating OrderItem")
        if menuItem == None or quantity == None:
            menuItem = input("Enter menu item name: ")
            quantity = input("Enter quantity:")
        return OrderItem(menuItem, quantity)
    
    def getOrderItemInJsonFormat(self):
        return {
            "id": self.getId(),
            "name": self.getName(),
            "description": self.getDescription(),
            "price": self.getPrice(),
            "-": {
                "name": "-",
                "width": 10,
                "action": modifyOrderItemQty,
                "id": self.getId(),
                "qty": -1
            },
            "quantity": self.getQuantity(),
            "+": {
                "name": "+",
                "width": 10,
                "action": modifyOrderItemQty,
                "id": self.getId(),
                "qty": 1
            }
        }

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
    
    def getOrderInJsonFormat(self):
        order = {
            "orderNumber": self._orderNumber
        }
        orderItemsJsonData = []
        for orderItem in self._orderItems:
            orderItemsJsonData.append(orderItem.getOrderItemInJsonFormat())
        order["orderItems"] = orderItemsJsonData
        return order

    def getOrderItemsInArray(self):
        orderItemsJsonData = []
        for orderItem in self._orderItems:
            orderItemsJsonData.append(orderItem.getOrderItemInJsonFormat())
        return orderItemsJsonData
    
    def getOrderItemById(self, id):
        for orderItem in self._orderItems:
            if orderItem.getId() == id:
                return orderItem
    
class Orders:
    _orders = []
    _activeOrder: Order = None
    def __init__(self):
        self._orders = []
        _activeOrder = None
    
    @staticmethod
    def addOrder(order):
        Orders._orders.append(order)
    
    @staticmethod
    def create() -> 'Orders':
        if Orders._orders is None:
            Orders._orders = Orders()
        return Orders._orders

    @staticmethod
    def createOrder():
        order: Order = Order(len(Orders._orders)+1)
        Orders.addOrder(order)
        Orders._activeOrder = order
        logger.info(f"Created order {order._orderNumber}")
        return Orders._activeOrder
    
    @staticmethod
    def activeOrder():
        for order in Orders._orders:
            if order == Orders._activeOrder:
                return order._orderNumber
            
    @staticmethod
    def getActiveOrder():
        return Orders._activeOrder

    @staticmethod
    def setActiveOrder(orderNumber):
        logger.info(f"Setting active order to {orderNumber}")
        for order in Orders._orders:
            if order._orderNumber == int(orderNumber):
                Orders._activeOrder = order
    
    @staticmethod
    def getOrdersInJsonFormat():
        ordersJsonData = []
        for order in Orders._orders:
            ordersJsonData.append(Order.getOrderInJsonFormat(order))
        return ordersJsonData
    
    @staticmethod
    def writeAllOrders():
        ordersdata = Orders.getOrdersInJsonFormat()
        writeJson(OrderListLocation, ordersdata)
    
    @staticmethod
    def readAllOrders():
        orderListContent = readJson(OrderListLocation)
        Orders.create()
        for orderContent in orderListContent:
            order:Order = Order(orderContent['orderNumber'])
            for orderItemContent in orderContent['orderItems']:
                orderItem: OrderItem = OrderItem(MenuCard.getMenuItem(orderItemContent['id']), orderItemContent['quantity'])
                order.addOrderItem(orderItem)
            Orders.addOrder(order)
