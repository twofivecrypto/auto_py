import openpyxl
wb = openpyxl.Workbook()
wb.get_sheet_names()

sheet = wb.active
sheet.title

sheet.title = 'Spam Bacon Eggs Sheet'
wb.get_sheet_by_names()