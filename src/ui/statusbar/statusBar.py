import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton
from utils import getLogger
import logging
from logging import Logger
import tkinter as tk

logger: Logger = getLogger("status-bar")

def addStatusBar(app: CTkFrame):
    logger.debug("Add StatusBar")
    statusBar: CTkFrame = ctk.CTkFrame(app, fg_color="gray", height= 25)
    statusBar.grid(row=1, sticky="NSEW")


# if __name__ == "__main__":
#     app: CTk = ctk.CTk()
#     app.geometry("800x600")
#     app.columnconfigure(0, weight=1)
#     app.rowconfigure(0, weight=1)
#     addStatusBar()