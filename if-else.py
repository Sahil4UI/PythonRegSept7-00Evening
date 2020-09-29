a = int(input("Enter side no 1 : "))
b = int(input("Enter side no 2 : "))
c = int(input("Enter side no 3 : "))

#ladder if -else 


if ((a+b>c) and (b+c>a) and (a+c>b) and (a>0 and b>0 and c>0) ):
    if (a==b==c):
        print("Equilateral Traingle" )
    elif ((a==b) or (b==c) or (c==a)):
        print("Isoceles Traingle")
    elif ((a**2== b**2+c**2) or (b**2 == c**2+a**2) or (c**2 == a**2+b**2)):
        print("right angle traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Traingle")
