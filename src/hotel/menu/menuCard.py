from hotel.menu.menuItem import MenuItem
import os
import json
from utils import getLogger
from logging import Logger
from utils.fileUtils import writeJson, readJson

# Location of the menu card JSON file
menuCardLocation = "data/menuCard.json"

class MenuCard:
    # Singleton instance of MenuCard
    _menuCard = None
    # List to store menu items
    _menuItems: list[MenuItem] = []
    
    def __init__(self):
        # Initialize empty menu items list
        self._menuItems = []

    def __str__(self):
        # String representation of menu card
        return "Menu Card: " + str(self._menuItems)
    
    def addMenuItem(self, menuItem):
        # Add a new menu item and assign it an ID
        menuItem: MenuItem = menuItem
        menuItem.setId(len(self._menuItems) + 1)
        self._menuItems.append(menuItem)

    def removeMenuItem(self, menuItem):
        # Remove a menu item from the list
        self._menuItems.remove(menuItem)

    def create() -> 'MenuCard':
        # Create singleton instance of MenuCard if it doesn't exist
        if MenuCard._menuCard is None:
            MenuCard._menuCard = MenuCard()
        return MenuCard._menuCard
    
    def printMenuCard(self):
        # Display all menu items and wait for user input
        for menuItem in self._menuItems:
            print(repr(menuItem))
            print("---------------------------------------------")
        choice = input("Press enter to exit:")

    def getMenuItems(self):
        # Return list of all menu items
        return self._menuItems
    
    def getMenuItem(Id):
        # Find and return menu item by ID
        menuCard: MenuCard = MenuCard.create()
        for menuItem in menuCard._menuItems:
            if menuItem.getId() == int(Id):
                return menuItem
        return None
    
    def getMenuItemsInJsonFormat(self):
        # Convert menu items to JSON format
        menuItemsJsonData = []
        for menuItem in self._menuItems:
            menuItemsJsonData.append(menuItem.getMenuItemInJsonFormat())
        return menuItemsJsonData

    def menuScreen(self):
        # Interactive menu screen for managing menu items
        isCont = True
        while isCont:
            os.system('clear')
            print("---------------------------------------------")
            print("__              Menu Screen              __")
            print("---------------------------------------------")
            print("1. Add Menu Item")
            print("2. View Menu Card")
            print("---------------------------------------------")
            print("0. Back")
            print("---------------------------------------------")
            choice = input("select choice :")
            print("---------------------------------------------")

            match choice:
                case "0":
                    isCont = False
                case "1":
                    menuItem = MenuItem.create()
                    self.addMenuItem(menuItem)
                    print("Menu Item added successfully")
                case "2":
                    self.printMenuCard()
                case _:
                    if int(choice) > len(self._menuItems):
                        print("Invalid choice")
                    else:
                        print("You selected: " + str(self._menuItems[int(choice)-1]))
    
    @staticmethod
    def writeMenuCard():
        # Save menu card data to JSON file
        menuItemsJsonData = MenuCard._menuCard.getMenuItemsInJsonFormat()
        writeJson(menuCardLocation, menuItemsJsonData)

    @staticmethod
    def readMenuCard():
        # Load menu card data from JSON file
        menuCardContent = readJson(menuCardLocation)
        menuCard: MenuCard = MenuCard.create()
        for menuItemContent in menuCardContent:
            menuCard.addMenuItem(MenuItem.create(menuItemContent['name'], menuItemContent['description'], menuItemContent['price']))