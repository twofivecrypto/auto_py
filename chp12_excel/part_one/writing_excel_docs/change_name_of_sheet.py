import openpyxl
wb = openpyxl.load_workbook("D:\\auto_py\\chp12_excel\\part_one\\writing_excel_docs\\example.xlsx")
sheet = wb.active
sheet.title = 'Spam Spam Spam'
wb.save('example_copy.xlsx')