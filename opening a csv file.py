import csv
with open('C:\\Users\\User\\OneDrive\\Desktop\\python programs\\menu.csv','r')as F:
    reader=csv.reader(F)
    for row in reader:
        print(row)
F.close()
