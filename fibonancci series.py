a=-1
b=1
n=int(input("Enter the number of terms :"))
i=0
sum=0
fibo=[]
while i<n:
    s=a+b
    fibo.append(s)
    sum+=s
    a=b
    b=s
    i+=1
print("Fibonancci series upto ",n," terms is:",fibo)
print("The sum of Fibonancci series is :",sum)
