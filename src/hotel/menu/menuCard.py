from hotel.menu.menuItem import MenuItem       
import os



class MenuCard:
    _menuCard = None
    _menuItems: list[MenuItem] = []
    def __init__(self):
        self._menuItems = []

    def __str__(self):
        return "Menu Card: " + str(self._menuItems)
    
    def addMenuItem(self, menuItem):
        menuItem: MenuItem = menuItem
        menuItem.setId(len(self._menuItems) + 1)
        self._menuItems.append(menuItem)

    def removeMenuItem(self, menuItem):
        self._menuItems.remove(menuItem)

    
    def create() -> 'MenuCard':
        if MenuCard._menuCard is None:
            MenuCard._menuCard = MenuCard()
        return MenuCard._menuCard
    
    def printMenuCard(self):
        for menuItem in self._menuItems:
            print(repr(menuItem))
            print("---------------------------------------------")
        choice = input("Press enter to exit:")

    def getMenuItems(self):
        return self._menuItems

    def showMenuCard(table):
        menuCard: MenuCard = MenuCard.create()
        menuItems = menuCard.getMenuItems()
        for menuItem in menuItems:
            table.add_row(menuItem.getMenuItemRow())

    def menuScreen(self):
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
