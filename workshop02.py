from xlrd import open_workbook
import pandas as wb

class Tech(object):
    def __init__(self, ID, Name, Password):
        self.ID = ID
        self.Name = Name
        self.Password = Password


    def __str__(self):
        return("Tech Support:\n"
               "  Tech_ID = {0}\n"
               "  DSPName = {1}\n"
               "  Password = {2} \n"
               .format(self.ID, self.Name, self.Password))

wb = open_workbook(r'C:\Users\amein\BootCampProject1\Technicals.xlsx.')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))
            except ValueError:
                pass
            finally:
                values.append(value)
        item = Tech(*values)
        items.append(item)

    for item in items:
        print (item)
        print(format(item.Name))
    print


