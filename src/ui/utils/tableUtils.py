from customtkinter import CTkButton, CTkLabel, CTkScrollableFrame
import customtkinter as ctk
import tkinter as tk

def renderTable(parentSelf, parent, rows, tableOptions = {
    'rowGrid': 0
}):
    """
    Creates and renders a table-like structure using CustomTkinter widgets
    Args:
        parentSelf: Reference to parent class for refresh functionality
        parent: Parent widget to contain the table
        rows: List of dictionaries containing row data
        tableOptions: Dictionary with table configuration options
    """
    # Validate input data
    if rows is None or len(rows) == 0 or type(rows).__name__ != 'list':
        return

    # Extract first row to determine headers
    row1 = rows[0]
    headers = []

    # Get column headers from dictionary keys
    for key in row1:
        headers.append(key)

    # Create scrollable frame to contain the table
    tableFrame = CTkScrollableFrame(parent, corner_radius=0, fg_color="transparent")
    tableFrame.grid(row=tableOptions['rowGrid'], column=1, sticky="ew", padx=20, pady=20)

    # Configure column expansion if specified in options
    if tableOptions is not None and 'expandColNumber' in tableOptions:
        tableFrame.columnconfigure(tableOptions['expandColNumber'], weight=1)
    
    # Render table headers
    colCount = 0
    for headerName in headers:
        # If no specific column expansion is set, make all columns expand equally
        if tableOptions is None or 'expandColNumber' not in tableOptions:
            tableFrame.columnconfigure(colCount, weight=1)

        # Create and position header labels
        header: CTkLabel = ctk.CTkLabel(tableFrame, fg_color="#003166", text=headerName)
        header.grid(row=0, column=colCount, sticky="ew", padx=5, pady=3)

        colCount += 1

    # Render table rows
    __renderRows(parentSelf=parentSelf, tableFrame=tableFrame, rows=rows)

def __renderRows(parentSelf, tableFrame, rows):
    """
    Renders the data rows of the table
    Args:
        parentSelf: Reference to parent class
        tableFrame: Frame containing the table
        rows: List of dictionaries containing row data
    """
    rowCount = 0

    def refreshParent(refreshFn):
        """
        Helper function to execute refresh methods from parent
        Args:
            refreshFn: Name of the refresh function to call
        """
        refreshFnx = getattr(parentSelf, refreshFn, f"Function {refreshFn} Attribute not found")
        if isinstance(refreshFnx, str):
            print(refreshFnx)
        else:
            refreshFnx()

    # Iterate through each row in the data
    for row in rows:
        colCount = 0
        rowCount += 1
        if type(row).__name__ == 'dict':
            # Process each value in the row
            for value in row.values():
                isLabelType = True

                # Check if value is a simple data type that can be displayed as text
                if not (isinstance(value, str) or isinstance(value, int) or isinstance(value, (bool, float, complex))):
                    isLabelType = False

                if isLabelType:
                    # Create label for simple data types
                    row: CTkLabel = ctk.CTkLabel(tableFrame, fg_color="#003166", text=value)
                    row.grid(row=rowCount, column=colCount, sticky="ew", padx=5, pady=3)
                else:
                    # Create button for complex data types (actions)
                    actionFn = value['action']
                    row: CTkButton = ctk.CTkButton(tableFrame, text=value['name'], width=value['width'], 
                                                 command=lambda id = value['id'], qty = value['qty'], 
                                                 refreshFn = value['refreshFn']: [actionFn(id,qty), refreshParent(refreshFn)])
                    row.grid(row=rowCount, column=colCount, sticky="ew", pady=3)
                colCount += 1