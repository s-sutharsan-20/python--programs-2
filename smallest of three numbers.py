n1=float(input("Enter the first number :"))
n2=float(input("Enter the second number :"))
n3=float(input("Enter the third number :"))
if n1<n2 and n1<n3:
    print("The First number(",n1,") is Smallest of given three numbers .")
elif n2<n1 and n2<n3:
    print("The Second number(",n2,") is Smallest of given three numbers .")
elif (n3<n1 and n3<n2):
    print("The Third number(",n3,") is Smallest of given three numbers .")
