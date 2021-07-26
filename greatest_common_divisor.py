num1=int(input("Enter the first integer:"))
num2=int(input ("enter the second integer:"))
temp=1
gcd=1
while (num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
gcd=num1
print("The greatest common divisor:", gcd)