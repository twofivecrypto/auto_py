import openpyxl

# GETTING SHEETS FROM THE WORKBOOK
wb = openpyxl.load_workbook('D:\\auto_py\\chp12_excel\\example.xlsx')
print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet3')
print(sheet)
print(type(sheet))
print(sheet.title)
anotherSheet = wb.active
print(anotherSheet)
