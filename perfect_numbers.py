number1=int(input("Please, enter the lower limit:"))
number2=int(input(" Please ,Enter the upper limit"))
print("All perfect numbers less than imteger:\n")   

for  num in range(number1,number2+1):
    sum=0
    for i in range(1, num):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        print(num)
