from customtkinter import CTkFrame, CTkButton, CTkLabel
import customtkinter as ctk
from ui.mainscreen.menuItemScreen import MenuScreen
from ui.mainscreen.orderItemScreen import OrderScreen

class MainScreen:
    def __init__(self, appContent: CTkFrame):
        self.appContent = appContent

    def menuScreen(self):
        menuScreen: MenuScreen = MenuScreen(self.appContent)
        menuScreen.menuItemScreen()

    def orderScreen(self):
        orderScreen: OrderScreen = OrderScreen(self.appContent)
        orderScreen.orderItemScreen()
