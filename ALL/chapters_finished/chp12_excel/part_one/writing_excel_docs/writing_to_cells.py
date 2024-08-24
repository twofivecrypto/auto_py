#writing values to cells using the openpyxl module

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 'Hello world!'
print(sheet['A1'].value)