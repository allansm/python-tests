import openpyxl
from openpyxl.styles import Font, Alignment
from random import randint

wb = openpyxl.Workbook()

sheet = wb.active

sheet["A1"] = "Values"
sheet["A1"].font = Font(bold=True)
sheet["A1"].alignment = Alignment(horizontal = "center")

for n in range(1, 100):
    sheet.cell(row=n+1, column=1).alignment = Alignment(horizontal = "center")
    sheet.cell(row=n+1, column=1).value=n+randint(0, 100)


sheet["B1"].font = Font(bold=True)
sheet["B1"].alignment = Alignment(horizontal = "center")
sheet["B1"] = "Average"

sheet["B2"].alignment = Alignment(horizontal = "center")
sheet["B2"] = "= AVERAGE(A1:A98)"


sheet["C1"].font = Font(bold=True)
sheet["C1"].alignment = Alignment(horizontal = "center")
sheet["C1"] = "Total"

sheet["C2"].alignment = Alignment(horizontal = "center")
sheet["C2"] = "= SUM(A1:A98)"

wb.save("test.xlsx")
