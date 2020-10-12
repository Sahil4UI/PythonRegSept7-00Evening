#print 1-10 numbers using while loop
'''
num = 10
while(num >=1):
    print(num)
    num-=1
'''
#find the sum of digits of number

num = int(input("enter number : "))
sum1 = 0
while(num!=0):
    rem = num%10
    sum1+=rem
    num=num//10
print(sum1)
