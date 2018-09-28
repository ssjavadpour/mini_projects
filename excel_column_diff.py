import xlrd
import xlwt

loc = "C:\\Users\\ssjav\\Downloads\\Fount Media plus small lists.xlsx"
#loc_hot = "C:\\Users\\ssjav\\Downloads\\Pro remodeler hotties as singles for dedeuping.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet_hot = wb.sheet_by_index(1)
sheet_not = wb.sheet_by_index(2)

fname_col = 0
lname_col = 1

hot_lst = []
for i in range(sheet_hot.nrows):
    hot_lst.append(sheet_hot.cell_value(i,lname_col))

#for item in hot_lst:
#    print(item)

for i in range(sheet.nrows):
    #for each lastname in all, does it exist in hotties
    #if not, save to array along with the first name
    lname = sheet.cell_value(i,lname_col)
    if not (lname in hot_lst):
        print(sheet.row_values(i),"\n`")
