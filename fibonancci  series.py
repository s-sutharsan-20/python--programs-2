a=-1
b=1
n=int(input("Enter the no. of terms:"))
i=0
fibo=[]
while i<n:
    s=b+a
    fibo.append(s)
    a=b
    b=s
    i+=1
print("Fibonancci series upto ",n,"  terms is :",fibo)
