n=int(input("Enter a positive integer:"))
k=0
while (n!=1):
    if (n==1):
        break
    elif (n%2==0): 
        n=n/2
        k=k+1
        print(n)
    else:
        n=3*n+1
        k=k+1
        print(n)
      