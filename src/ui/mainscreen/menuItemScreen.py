import logging
from logging import Logger
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame
from utils import getLogger
import customtkinter as ctk
import tkinter as tk
import json
import os
from CTkTable import CTkTable

from ui.utils.tableUtils import renderTable

from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard

# Global menu card instance to store all menu items
menuCard: MenuCard = MenuCard.create()

# Configure logger for the menu screen
logger = getLogger("MenuScreen", logging.INFO)

# Load existing menu card data when screen is initialized
MenuCard.readMenuCard()

class MenuScreen:
    def __init__(self, appContent: CTkFrame):
        self.appContent = appContent
        
        # Create main container frame for the menu screen
        self.menuScreen: CTkFrame = ctk. CTkFrame(self.appContent, fg_color="#233040")
        self.menuScreen.grid(row=0, column=1, sticky="NSEW")
        self.menuScreen.rowconfigure(2, weight=0)
        self.menuScreen.columnconfigure(1, weight=1)

    def menuItemScreen(self):
            for widget in self.menuScreen.winfo_children():
                widget.destroy()

            # Title section of the menu screen
            menuTitle: CTkLabel = ctk.CTkLabel(self.menuScreen,fg_color="#003166", text="Menu Options")
            menuTitle.grid(row=0, column=1, sticky="ew", padx=20, pady=20)

            # Input fields for new menu item details
            self.name = ctk.CTkEntry(self.menuScreen, placeholder_text="Name")
            self.name.grid(row=1, column=1, sticky="ew", padx=20, pady=20)

            self.description = ctk.CTkEntry(self.menuScreen, placeholder_text="Description")
            self.description.grid(row=2, column=1, sticky="ew", padx=20, pady=20)

            self.price = ctk.CTkEntry(self.menuScreen, placeholder_text="Price")
            self.price.grid(row=3, column=1, sticky="ew", padx=20, pady=20)

            # Button container for all action buttons
            btnRow = ctk.CTkFrame(self.menuScreen, fg_color="#003166")
            btnRow.grid(row=4, column=1, sticky="ew", padx=20, pady=5)
            btnRow.columnconfigure(1, weight=1)

            # Action buttons for menu operations
            addMenuItemsBtn: CTkButton = ctk.CTkButton(btnRow, text="Add Menu Item", command=self.addMenuItem)
            addMenuItemsBtn.grid(row=4, column=1, sticky="ew", padx=20, pady=20)

            clearEntryBoxBtn: CTkButton = ctk.CTkButton(btnRow, text="Clear Entry Box", command=self.clearEntryBox)
            clearEntryBoxBtn.grid(row=4, column=0, sticky="ew", padx=20, pady=20)

            saveMenuCardBtn: CTkButton = ctk.CTkButton(btnRow, text="Save Menu Card", command=self.writeToTheJsonFile)
            saveMenuCardBtn.grid(row=4, column=2, sticky="ew", padx=20, pady=20)

            tableOptions = {
                "rowGrid": 5
            }
            renderTable(self, self.menuScreen, MenuCard.getMenuItemsInJsonFormat(menuCard), tableOptions)

    def addMenuItem(self):
        # Create and add new menu item from input fields
        name = self.name.get()
        description = self.description.get()
        price = self.price.get()
        logger.info(f"price {price}")
        menuItem = MenuItem.create(name, description, price)
        menuCard.addMenuItem(menuItem)
        self.clearEntryBox()
        logger.info("added menu item")
        self.menuItemScreen()


    def clearEntryBox(self):
        # Clear all input fields
        self.name.delete(0, ctk.END)
        self.description.delete(0, ctk.END)
        self.price.delete(0, ctk.END)
        logger.info("cleared entry box")
    
    def writeToTheJsonFile(self):
        # Save current menu card to persistent storage
        MenuCard.writeMenuCard()
        logger.info("saved menu card")