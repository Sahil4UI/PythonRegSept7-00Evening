def tempConversion(celcius):
    fah = 9/5*celcius + 32
    return fah

#print(tempConversion(34))

tempList = [22.5,30,45,20,0,-10,24,33,100]
'''
x=[]
for temp in tempList:
    x.append(tempConversion(temp))

print(x)
    
f=list(map(tempConversion,tempList))
print(f)
'''

def myfun(x):
    return x**2
'''
p=[1,2,3,4,5,6,7,8,9,10]
f= list(map(myfun,p))
print(f)
'''
def even(x):
    if x%2==0:
        return True
    else:
        return False
    
z= [1,2,3,4,5,6,7,8,9,10]
'''   
f = list(filter(even,z))
print(f)
'''
#lambda function
x = list(map(lambda a : 9/5*a+32 , tempList))
print(x)
