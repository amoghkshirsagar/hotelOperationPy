import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
from utils import getLogger
import logging
from logging import Logger
from hotel.menu.menuItem import MenuItem
import tkinter as tk

from ui.statusbar.statusBar import addStatusBar

logger: Logger = getLogger("UI", logging.INFO)

def buildAppUi():
    app: CTk = ctk.CTk()
    app.geometry("800x600")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    appContent: CTkFrame = ctk.CTkFrame(app, fg_color="black")
    appContent.grid(row=0, sticky="NSEW")
    appContent.rowconfigure(0, weight=1)
    appContent.columnconfigure(1, weight=1)

    frame1: CTkFrame = ctk.CTkFrame(appContent)
    frame1.grid(row=0, column=0, sticky="NSEW")
    frame1.rowconfigure(2, weight=1)

    button1: CTkButton = ctk.CTkButton(frame1, text="button1")
    button1.grid(row=0,sticky="ew", pady=20)

    button2: CTkButton = ctk.CTkButton(frame1, text="button2")
    button2.grid(row=1,sticky="ew")

    button3: CTkButton = ctk.CTkButton(frame1, text="button3")
    button3.grid(row=2, sticky="NEW", pady=20)


    frame2: CTkFrame = ctk.CTkFrame(appContent, fg_color="black")
    frame2.grid(row=0, column=1, sticky="NSEW")

    addStatusBar(app)

    app.mainloop()

if __name__ == "__main__":
    buildAppUi()