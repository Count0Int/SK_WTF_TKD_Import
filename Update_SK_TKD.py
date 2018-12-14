import pandas as pd
from easygui import *
from openpyxl import load_workbook

memberfile = fileopenbox('Member List')
print(memberfile)
xlmembers = pd.ExcelFile(memberfile)
xlsheet = xlmembers.parse('2018')
MJdf = pd.DataFrame(xlsheet.values)

print(MJdf)


sktkdfile = fileopenbox('Destination File')

book = load_workbook(sktkdfile)
writer = pd.ExcelWriter(sktkdfile, engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

# Position the dataframes in the worksheet.
MJdf.to_excel(writer, 'Club Database ', startrow=23, startcol=1, index=False, header=False)
writer.save()

xlSKTKD = pd.ExcelFile(sktkdfile)
print(xlSKTKD.sheet_names)
xlsheetSK = xlSKTKD.parse('Club Database ')
SKdf = pd.DataFrame(xlsheetSK.values)
print(SKdf)