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

logger: Logger = getLogger("Order-screen")

class OrderScreen:
    def __init__(self, appContent: CTkFrame):
        self.appContent = appContent

    def orderItemScreen(self):
        logger.debug("Order Item Screen")
        Orders.create()
        if Orders.activeOrder() == None:
            Orders.createOrder()
        orderScreen: CTkFrame = ctk. CTkFrame(self.appContent, fg_color="#233040")
        orderScreen.grid(row=0, column=1, sticky="NSEW")
        orderScreen.rowconfigure(2, weight=0)
        orderScreen.columnconfigure(1, weight=1)
        self.activeOrderLabel = ctk.StringVar()
        self.activeOrderLabel.set(self.getActiveOrderLabel())

        # Row 1
        titleRow = ctk.CTkFrame(orderScreen, fg_color="#003166")
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
        createOrderRow = ctk.CTkFrame(orderScreen, fg_color="#003166")
        createOrderRow.grid(row=1, column=1, sticky="ew", padx=20)
        createOrderRow.columnconfigure(1, weight=1)
        createOrderBtn: CTkButton = ctk.CTkButton(createOrderRow, text="Create Order", command=self.createOrder)
        createOrderBtn.grid(row=1, column=1, sticky="e", padx=20)

        # Row 3 - Order table
        self.orderTableFrame: CTkScrollableFrame = CTkScrollableFrame(orderScreen, corner_radius=0, fg_color="transparent")
        self.orderTableFrame.grid(row=2, column=1, sticky="ew", padx=20, pady=20)
        self.orderTableFrame.columnconfigure(1, weight=1)

        self.orderValues = [['SrNo','name', 'description', 'price']]
        self.orderTable: CTkTable = CTkTable(self.orderTableFrame, values=self.orderValues, corner_radius=0)
        self.orderTable.grid(row=0, column=1, sticky="ew", padx=20, pady=20)

        # Row 4 - Menu Table
        self.menuTableFrame: CTkScrollableFrame = CTkScrollableFrame(orderScreen, corner_radius=0, fg_color="transparent")
        self.menuTableFrame.grid(row=3, column=1, sticky="ew", padx=20, pady=20)
        self.menuTableFrame.columnconfigure(1, weight=1)

        self.menuValues = [['Sr.No', 'name', 'description', 'price']]
        self.menuTable: CTkTable = CTkTable(self.menuTableFrame, values=self.menuValues, corner_radius=0)
        self.menuTable.grid(row=0, column=1, sticky="ew", padx=20, pady=20)
        MenuCard.showMenuCard(self.menuTable)


    def getActiveOrderLabel(self):
        return "Active Order: " + str(Orders.activeOrder())
    
    def setActiveOrder(self):
        ordernumber = self.activeOrder.get()
        Orders.setActiveOrder(ordernumber)
        self.activeOrderLabel.set(self.getActiveOrderLabel())

    def createOrderItem(menuItem: MenuItem, quantity):
        order: OrderItem = OrderItem(menuItem, quantity)
    
    def createOrder(self):
        self.order: Order = Orders.createOrder()
        self.activeOrderLabel.set(self.getActiveOrderLabel())
