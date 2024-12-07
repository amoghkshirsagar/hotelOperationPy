from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from utils import getLogger
from logging import Logger
import customtkinter as ctk
import logging
import tkinter as tk
from CTkTable import CTkTable

from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard

menuCard: MenuCard = MenuCard.create()

class MainScreen:
    def __init__(self, appContent: CTkFrame):
        self.appContent = appContent
    def menuItemOptions(self):
        menuScreen: CTkFrame = ctk. CTkFrame(self.appContent, fg_color="#233040")
        menuScreen.grid(row=0, column=1, sticky="NSEW")
        menuScreen.rowconfigure(2, weight=0)
        menuScreen.columnconfigure(1, weight=1)

        title: CTkLabel = ctk.CTkLabel(menuScreen,fg_color="#003166", text="Menu Options")
        title.grid(row=0, column=1, sticky="ew", padx=20, pady=20)

        self.name = ctk.CTkEntry(menuScreen, placeholder_text="CTkEntry")
        self.name.grid(row=1, column=1, sticky="ew", padx=20, pady=20)
        self.name.delete(0, ctk.END)

        self.description = ctk.CTkEntry(menuScreen, placeholder_text="CTkEntry")
        self.description.grid(row=2, column=1, sticky="ew", padx=20, pady=20)
        self.description.delete(0, ctk.END)

        self.price = ctk.CTkEntry(menuScreen, placeholder_text="CTkEntry")
        self.price.grid(row=3, column=1, sticky="ew", padx=20, pady=20)
        self.price.delete(0, ctk.END)

        button1: CTkButton = ctk.CTkButton(menuScreen, text="Add Menu Item", command=self.addMenuItem)
        button1.grid(row=4, column=1, sticky="ew", padx=20, pady=20)

        button2: CTkButton = ctk.CTkButton(menuScreen, text="View Menu Items")
        button2.grid(row=5, column=1, sticky="ew", padx=20, pady=20)
    
        self.tableFrame: CTkScrollableFrame = CTkScrollableFrame(menuScreen, height=400, corner_radius=0, fg_color="transparent")
        self.tableFrame.grid(row=6, column=1, sticky="SWE", padx=20, pady=20)

        self.values = [['name', 'description', 'price']]
        self.table: CTkTable = CTkTable(self.tableFrame, row=0, column=3, values=self.values, corner_radius=0, width=200)
        self.table.grid(row=0, column=0, sticky="ew", padx=20, pady=20)

    def orderItemOptions(self):
        orderScreen: CTkFrame = ctk. CTkFrame(self.appContent, fg_color="#233040")
        orderScreen.grid(row=0, column=1, sticky="NSEW")
        orderScreen.rowconfigure(2, weight=0)
        orderScreen.columnconfigure(1, weight=1)

        title: CTkLabel = ctk.CTkLabel(orderScreen,fg_color="#003166", text="Order Options")
        title.grid(row=0, column=1, sticky="ew", padx=20, pady=20)

        button1: CTkButton = ctk.CTkButton(orderScreen, text="Add Order Item")

    def addMenuItem(self):
        name = self.name.get()
        description = self.description.get()
        price = self.price.get()
        menuItem = MenuItem.create(name, description, price)
        menuCard.addMenuItem(menuItem)
        self.table.add_row([name, description, price])
        print(f"{self.table.rows} rows")