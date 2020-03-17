import math

a= int(input('Enter value of a: '))
b= int(input('Enter value of b: '))
c= int(input('Enter value of c: '))

D= b*b-4*a*c    #Discriminant

if D>=0:
    r1= ((-b + math.sqrt(D))/(2*a))  #Root 1
    r2= ((-b - math.sqrt(D))/(2*a))  #Root 2

else:   #Calculate Real and Imaginary Part
    rp= b/(2*a)
    ip= math.sqrt(-D)/(2*a)
    r1= str(rp)+ ' +j'+str(ip)
    r2= str(rp)+ ' -j'+str(ip)

print (f'Root 1: {r1} \t Root 2: {r2}')