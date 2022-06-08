celcius=float(input("Enter the Temperature in celcius  :"))
def convert(c):
    return 9/5*celcius+32
fahrenheit=convert(celcius)
print(celcius," degree celcius is =",fahrenheit,"degree fahrenheit")
