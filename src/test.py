from hotel.menu.foodItem import FoodItem
from hotel.menu.menuItem import MenuItem
from hotel.menu.menuCard import MenuCard
import pygameUtils
import pygame, os

pygameUtils.startGame()

pygameUtils.drawText(pygameUtils.win, "Hotel Operations", 400, 300, pygame.font.SysFont("Arial", 40), (255, 255, 255))

menucard = MenuCard.create()

isCont = True
while isCont:
    os.system('cls')
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