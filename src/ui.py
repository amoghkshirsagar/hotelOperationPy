import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
from utils import getLogger
import logging
from logging import Logger
import tkinter as tk

from ui.statusbar.statusBar import addStatusBar
from ui.appcontent.appContent import addAppContent

logger: Logger = getLogger("UI", logging.INFO)

def buildAppUi():
    app: CTk = ctk.CTk()
    app.geometry("900x800")
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    addAppContent(app)

    addStatusBar(app)

    app.mainloop()

if __name__ == "__main__":
    buildAppUi()