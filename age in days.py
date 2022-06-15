from datetime import date
today=date.today()
print(today)

year=int(input("Enter your born Year:"))
month=int(input("Enter your born month :"))
day=int(input("Enter your born date  :"))

date_of_birth=date(year=year,month=month,day=day)
print("Your Date Of Birth is :",date_of_birth)
print("Your Age is :",(today-date_of_birth).days,"  Days")
