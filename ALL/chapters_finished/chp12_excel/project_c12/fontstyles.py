#Customize font styles in cells

import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook('D:\\auto_py\\chp12_excel\\produceSales.xlsx')
sheet = wb.get_sheet_by_name('Sheet')
print
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
sheet['AI'] = 'Hello world!'
wb.save('styled.xlsx')