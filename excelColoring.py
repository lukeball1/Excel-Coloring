import openpyxl
from openpyxl.styles import PatternFill

# Load the spreadsheet
workbook = openpyxl.load_workbook("your_file.xlsx")
spreadsheet = workbook.active

#set global color fills
greenFill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
redFill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")


with open("FileDescriptorOrPath", "r") as f:
    # do stuff with file here
    content = f.readLine()