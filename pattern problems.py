"""
*
**
***
****
*****

for i in range(1,6):
    print("*"*i)


for i in reversed(range(1,5)):
    for j in range(0,i):
        print("*",end="")
    print()
"""  
"""
1
12
123
1234
12345
for i in range(5):
    for j in range(i+1):
        print(j+1,end='')
    print()

1
22
333
4444
55555

for i in range(5):
    for j in range(i+1):
        print(i+1,end='')
    print()

"""

"""
1
23
456
78910
x=1
for i in range(4):
    for j in range(i+1):
        print(x,end='')
        x=x+1
    print()
"""

"""
A
BB
CCC
DDDD
EEEEE

for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end='')
    print()

A
AB
ABC
ABCD
ABCDE

for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end='')
    print()
"""
#Q->print prime numbers b/w 1-100
a = 1
b = 100
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
