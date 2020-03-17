flag=1
i=2

n=int (input('Enter a number to check prime: '))

while i<n/2:
    if n%i==0:
        flag=0
    
    i=i+1

if flag==0:
    print(n, ' is not a prime number.')

else:
    print(n, ' is a prime number.')