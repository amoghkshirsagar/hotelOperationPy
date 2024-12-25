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
    statusBar.columnconfigure(1, weight=1)
    
    orderLimit: CTkLabel = ctk.CTkLabel(statusBar, fg_color="#003166", text="Orders")
    orderLimit.grid(row=0, column=0, sticky="ew", padx=20, pady=5)

    progressbarRow = ctk.CTkFrame(statusBar, fg_color="#003166")
    progressbarRow.grid(row=0, column=1, sticky="ew", padx=20, pady=5)

    progressbar = ctk.CTkProgressBar(progressbarRow)
    progressbar.configure(width=800)
    progressbar.pack(padx=20, pady=10)
    progressbar.set(len(Orders._orders))