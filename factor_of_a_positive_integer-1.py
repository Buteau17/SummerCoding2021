number=int(input("Enter an integer:"))
print(f"the factors of {number} are:")
for i in range (1,number+1):
    if number%i==0:
        print(i)