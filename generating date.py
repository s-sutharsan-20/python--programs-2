import pandas as pd
s=(input("Enter the starting date in MM-DD-YYYY format:"))
e=(input("Enter the ending date in MM-DD-YYYY format:"))
dr=pd.date_range(start=s,end=e)
print(dr)
