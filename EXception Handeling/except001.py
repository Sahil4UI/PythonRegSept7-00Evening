#exception Handeling
#Types of Error
#syntactical error
#run time Error ->Exception(code ->correct->runtime error -> eXception)

try:
    a = int(input("Enter first Number : "))
    b = int(input("Enter Second Number : "))

    c = a+b
    d = a-b
    e=a*b
    f=a/b
  

except BaseException as be:
    print(be)
else:
    print("sum=",c)
    print("sub=",d)
    print("mul=",e)
    print("div=",f)
    
   
'''
except ZeroDivisionError:
    print("Cannot be divided by zero")

except ValueError:
    print("Invalid Value")
'''
