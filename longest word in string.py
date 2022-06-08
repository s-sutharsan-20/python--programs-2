text=input("Enter a string :")
s=text.split()
a=len(s)
def char(text):
    count=0
    for ch in text:
        count+=1
    return count
num=[char(s[i]) for i in range(a)]
x=num.index(max(num))
print("The longest word in ",text," is:",s[x])
