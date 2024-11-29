from hotel.menu.foodItem import FoodItem
from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard
import os

menucard = MenuCard.create()

isCont = True
while isCont:
    os.system('clear')
    print("---------------------------------------------")
    print("__              Choose Screen              __")
    print("---------------------------------------------")
    print("1. Menu Screen")
    print("2. Order Screen")
    print("0. Exit Menu")
    print("---------------------------------------------")
    choice = input("select choice :")

    match choice:
        case "0":
            isCont = False
        case "1":
            menucard.menuScreen()