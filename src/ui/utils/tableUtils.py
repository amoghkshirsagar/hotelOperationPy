from customtkinter import CTkButton, CTkLabel, CTkScrollableFrame
import customtkinter as ctk

def renderTable(parent, rows, tableOptions = {
    'rowGrid': 0
}):
    if rows is None or len(rows) == 0 or type(rows).__name__ != 'list':
        return

    row1 = rows[0]
    headers = []

    for key in row1:
        headers.append(key)

    tableFrame = CTkScrollableFrame(parent, corner_radius=0, fg_color="transparent")
    tableFrame.grid(row=tableOptions['rowGrid'], column=1, sticky="ew", padx=20, pady=20)

    if tableOptions is not None and 'expandColNumber' in tableOptions:
        tableFrame.columnconfigure(tableOptions['expandColNumber'], weight=1)
    
    colCount = 0
    for headerName in headers:
        if tableOptions is None or 'expandColNumber' not in tableOptions:
            tableFrame.columnconfigure(colCount, weight=1)

        header: CTkLabel = ctk.CTkLabel(tableFrame, fg_color="#003166", text=headerName)
        header.grid(row=0, column=colCount, sticky="ew", padx=5, pady=3)

        colCount += 1

    __renderRows(tableFrame=tableFrame, rows=rows)
def actionFunction(actionScript):
    eval(actionScript)

def __renderRows(tableFrame, rows):
    rowCount = 0
    for row in rows:
        colCount = 0
        rowCount += 1
        if type(row).__name__ == 'dict':
            for value in row.values():
                isLabelType = True

                if not (isinstance(value, str) or isinstance(value, int) or isinstance(value, (bool, float, complex))):
                    isLabelType = False

                if isLabelType:
                    row: CTkLabel = ctk.CTkLabel(tableFrame, fg_color="#003166", text=value)
                    row.grid(row=rowCount, column=colCount, sticky="ew", padx=5, pady=3)
                else:
                    actionFn = value['action']
                    row: CTkButton = ctk.CTkButton(tableFrame, text=value['name'], width=value['width'], command=lambda id = value['id'], qty = value['qty']: actionFn(id,qty))
                    row.grid(row=rowCount, column=colCount, sticky="ew", pady=3)
                colCount += 1