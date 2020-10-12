number = int(input("Enter Number : "))
sumdigit=0
for i in range(len(str(number))):
    rem=number%10
    sumdigit = sumdigit*10+rem
    number = number//10
print(sumdigit)
