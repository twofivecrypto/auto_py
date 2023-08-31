import openpyxl
wb = openpyxl.load_workbook('D:\\auto_py\\chp12_excel\\example.xlsx')
sheet = wb.active

second_column = sheet.columns[1]


for column in sheet.columns:
    for cell in column:
        if column[0].column == 2:
            print(cell.value)
            
'''
Apples
Cherries
Pears
Oranges
Apples
Bananas'''

