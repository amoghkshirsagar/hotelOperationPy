import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
from utils import getLogger
import logging
from logging import Logger
import tkinter as tk

from ui.mainscreen.mainScreen import MainScreen

logger: Logger = getLogger("app-content")

def addAppContent(app: CTkFrame):
    logger.debug("Add AppContent")

    appContent: CTkFrame = ctk.CTkFrame(app, fg_color="black")
    appContent.grid(row=0, sticky="NSEW")
    appContent.rowconfigure(0, weight=1)
    appContent.columnconfigure(1, weight=1)

    mainScreen = MainScreen(appContent)

    frame1: CTkFrame = ctk.CTkFrame(appContent)
    frame1.grid(row=0, column=0, sticky="NSEW")
    frame1.rowconfigure(2, weight=1)

    button1: CTkButton = ctk.CTkButton(frame1, text="Menu Options", command=mainScreen.menuScreen)
    button1.grid(row=0,sticky="ew", pady=20)

    button2: CTkButton = ctk.CTkButton(frame1, text="Order Options", command=mainScreen.orderScreen)
    button2.grid(row=1,sticky="ew")

    button3: CTkButton = ctk.CTkButton(frame1, text="button3")
    button3.grid(row=2, sticky="new", pady=20)

    # frame2: CTkFrame = ctk.CTkFrame(appContent, fg_color="black")
    # frame2.grid(row=0, column=1, sticky="NSEW")

