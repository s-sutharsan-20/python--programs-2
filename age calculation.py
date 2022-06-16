from datetime import date
def agecalculation():
    year=int(input("Enter your year of birth  :"))
    month=int(input("Enter your month of birth  :"))
    day=int(input("Enter your day  of birth :"))
    today=date.today()
    print("Today's date :",today)
    date_of_birth=date(year,month,day)
    print("Your Birth Date is  :",date_of_birth)
    total_days=(today-date_of_birth).days
    age=int(total_days/365.5)
    print("Your Age is  :",age)

agecalculation()
