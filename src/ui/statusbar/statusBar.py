import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkButton, CTkProgressBar, CTkLabel
from utils import getLogger
import logging
from logging import Logger
import tkinter as tk
from hotel.orders.orderItems import Order, OrderItem, Orders

logger: Logger = getLogger("status-bar")

def addStatusBar(app: CTkFrame):
    logger.debug("Add StatusBar")
    statusBar: CTkFrame = ctk.CTkFrame(app, fg_color="gray", height= 25)
    statusBar.grid(row=1, sticky="NSEW")
    