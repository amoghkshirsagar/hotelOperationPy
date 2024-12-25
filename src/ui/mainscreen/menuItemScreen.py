import logging
from logging import Logger
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from utils import getLogger
import customtkinter as ctk
import tkinter as tk
from CTkTable import CTkTable

from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard

menuCard: MenuCard = MenuCard.create()
logger = getLogger("MenuScreen", logging.INFO)

class MenuScreen:
    def __init__(self, appContent: CTkFrame):
        self.appContent = appContent
    def menuItemScreen(self):
            menuScreen: CTkFrame = ctk. CTkFrame(self.appContent, fg_color="#233040")
            menuScreen.grid(row=0, column=1, sticky="NSEW")
            menuScreen.rowconfigure(2, weight=0)
            menuScreen.columnconfigure(1, weight=1)

            menuTitle: CTkLabel = ctk.CTkLabel(menuScreen,fg_color="#003166", text="Menu Options")
            menuTitle.grid(row=0, column=1, sticky="ew", padx=20, pady=20)

            self.name = ctk.CTkEntry(menuScreen, placeholder_text="Name")
            self.name.grid(row=1, column=1, sticky="ew", padx=20, pady=20)

            self.description = ctk.CTkEntry(menuScreen, placeholder_text="Description")
            self.description.grid(row=2, column=1, sticky="ew", padx=20, pady=20)

            self.price = ctk.CTkEntry(menuScreen, placeholder_text="Price")
            self.price.grid(row=3, column=1, sticky="ew", padx=20, pady=20)

            btnRow = ctk.CTkFrame(menuScreen, fg_color="#003166")
            btnRow.grid(row=4, column=1, sticky="ew", padx=20, pady=5)
            btnRow.columnconfigure(1, weight=1)

            button1: CTkButton = ctk.CTkButton(btnRow, text="Add Menu Item", command=self.addMenuItem)
            button1.grid(row=4, column=1, sticky="ew", padx=20, pady=20)

            button1: CTkButton = ctk.CTkButton(btnRow, text="Clear Entry Box", command=self.clearEntryBox)
            button1.grid(row=4, column=0, sticky="ew", padx=20, pady=20)
        
            self.tableFrame: CTkScrollableFrame = CTkScrollableFrame(menuScreen, height=400, corner_radius=0, fg_color="transparent")
            self.tableFrame.grid(row=6, column=1, sticky="ew", padx=20, pady=20)
            self.tableFrame.columnconfigure(0, weight=1)

            self.values = [['Sr.No', 'name', 'description', 'price']]
            self.table: CTkTable = CTkTable(self.tableFrame, row=0, column=4, values=self.values, corner_radius=0, width=200)
            self.table.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
            MenuCard.showMenuCard(self.table)

    def addMenuItem(self):
        name = self.name.get()
        description = self.description.get()
        price = self.price.get()
        logger.info(f"price {price}")
        menuItem = MenuItem.create(name, description, price)
        menuCard.addMenuItem(menuItem)
        self.clearEntryBox()
        self.table.add_row(menuItem.getMenuItemRow())

    def clearEntryBox(self):
        self.name.delete(0, ctk.END)
        self.description.delete(0, ctk.END)
        self.price.delete(0, ctk.END)