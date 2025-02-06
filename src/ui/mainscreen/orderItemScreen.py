import logging
from logging import Logger
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from utils import getLogger
import customtkinter as ctk
import tkinter as tk
from CTkTable import CTkTable
from hotel.orders.orderItems import Order, OrderItem, Orders
from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard
from ui.utils.tableUtils import renderTable

logger: Logger = getLogger("Order-screen")

menuCard: MenuCard = MenuCard.create()
orders = Orders.readAllOrders()
Orders.setActiveOrder(len(Orders._orders))
class OrderScreen:
    def __init__(self, appContent: CTkFrame):
        self.appContent = appContent
        self.orderScreen: CTkFrame = ctk. CTkFrame(self.appContent, fg_color="#233040")
        self.orderScreen.grid(row=0, column=1, sticky="NSEW")
        self.orderScreen.rowconfigure(2, weight=0)
        self.orderScreen.columnconfigure(1, weight=1)

    def orderItemScreen(self):
        logger.debug("Order Item Screen")
        if Orders.activeOrder() == None:
            Orders.createOrder()
        
        for widget in self.orderScreen.winfo_children():
                widget.destroy()

        self.activeOrderLabel = ctk.StringVar()
        self.activeOrderLabel.set(self.getActiveOrderLabel())

        # Row 1
        titleRow = ctk.CTkFrame(self.orderScreen, fg_color="#003166")
        titleRow.grid(row=0, column=1, sticky="ew", padx=20, pady=5)
        titleRow.columnconfigure(1, weight=1)
        
        orderTitle: CTkLabel = ctk.CTkLabel(titleRow, fg_color="#003166", text="Order Items")
        orderTitle.grid(row=0, column=1, sticky="ew", padx=20, pady=0)

        activeOrder: CTkLabel = ctk.CTkLabel(titleRow, fg_color="#003166", textvariable=self.activeOrderLabel)
        activeOrder.grid(row=0, column=2, sticky="ew", padx=20, pady=0)

        self.activeOrder = ctk.CTkEntry(titleRow, placeholder_text="Set Active Order")
        self.activeOrder.grid(row=0, column=3, sticky="ew", padx=20, pady=0)

        setActiveBtn: CTkButton = ctk.CTkButton(titleRow, text="Set Active Order", command=self.setActiveOrder)
        setActiveBtn.grid(row=0, column=4, sticky="ew", padx=20, pady=0)

        # Row 2
        createOrderRow = ctk.CTkFrame(self.orderScreen, fg_color="#003166")
        createOrderRow.grid(row=1, column=1, sticky="ew", padx=20)
        createOrderRow.columnconfigure(1, weight=1)

        createOrderBtn: CTkButton = ctk.CTkButton(createOrderRow, text="Create Order", command=self.createOrder)
        createOrderBtn.grid(row=1, column=1, sticky="e", padx=20)

        # Row 3 - Active Order Table
        order: Order = Orders.getActiveOrder()
        tableOptions = {
            'rowGrid': 2
        }
        renderTable(self, self.orderScreen, order.getOrderItemsInArray(), tableOptions)

        # # Row 4 - Menu Table
        renderTable(self, self.orderScreen, MenuCard.getMenuItemsInJsonFormat(menuCard), {'rowGrid': 4 })
        
        # Row 5 - Menu Item Choice
        menuChoicesRow = ctk.CTkFrame(self.orderScreen, fg_color="#003166")
        menuChoicesRow.grid(row=3, column=1, sticky="ew", padx=20, pady=5)
        menuChoicesRow.columnconfigure(2, weight=1)

        self.menuItemId = ctk.CTkEntry(menuChoicesRow, placeholder_text="Menu Item Id")
        self.menuItemId.grid(row=1, column=0, sticky="ew", padx=20, pady=20)

        self.menuItemQuantity = ctk.CTkEntry(menuChoicesRow, placeholder_text="Quantity")
        self.menuItemQuantity.grid(row=1, column=1, sticky="ew", padx=20, pady=20)

        addOrderItem: CTkButton = ctk.CTkButton(menuChoicesRow, text="Add Order Item", command=self.createOrderItem)
        addOrderItem.grid(row=1, column=2, sticky="ew", padx=20)

        saveAllOrdersBtn: CTkButton = ctk.CTkButton(menuChoicesRow, text="Save All Orders", command=self.writeAllOrdersToJson)
        saveAllOrdersBtn.grid(row=1, column=3, sticky="ew", padx=20)

    def tableAction(self, event):
        logger.debug("tableAction: entry")
        logger.debug(event)

    def getActiveOrderLabel(self):
        return "Active Order: " + str(Orders.activeOrder())
    
    def setActiveOrder(self):
        ordernumber = self.activeOrder.get()
        Orders.setActiveOrder(ordernumber)
        self.activeOrderLabel.set(self.getActiveOrderLabel())
        self.orderItemScreen()

    def createOrderItem(self):
        Id = self.menuItemId.get()
        quantity = self.menuItemQuantity.get()
        menuItem: MenuItem = MenuCard.getMenuItem(Id)
        orderItem: OrderItem = OrderItem.createOrderItem(menuItem, quantity)
        order: Order = Orders.getActiveOrder()
        order.addOrderItem(orderItem)
        self.orderItemScreen()

    
    def createOrder(self):
        self.order: Order = Orders.createOrder()
        self.activeOrderLabel.set(self.getActiveOrderLabel())
        self.orderItemScreen()
    
    def writeAllOrdersToJson(self):
        Orders.writeAllOrders()
        

