Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import calendar
>>> year=2020
>>> month=10
>>> print(calendar.month(year,month))
    October 2020
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

>>> calendar.month(year,month)
'    October 2020\nMo Tu We Th Fr Sa Su\n          1  2  3  4\n 5  6  7  8  9 10 11\n12 13 14 15 16 17 18\n19 20 21 22 23 24 25\n26 27 28 29 30 31\n'
>>> #\n->next line
>>> calendar.calendar(2020)
'                                  2020\n\n      January                   February                   March\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2                         1\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8\n13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22\n27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29\n                                                    30 31\n\n       April                      May                       June\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7\n 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14\n13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21\n20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28\n27 28 29 30               25 26 27 28 29 30 31      29 30\n\n        July                     August                  September\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                      1  2          1  2  3  4  5  6\n 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13\n13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20\n20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27\n27 28 29 30 31            24 25 26 27 28 29 30      28 29 30\n                          31\n\n      October                   November                  December\nMo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su\n          1  2  3  4                         1          1  2  3  4  5  6\n 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13\n12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20\n19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27\n26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31\n                          30\n'
>>> print(calendar.calendar(2020))
                                  2020

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                         1
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
                                                    30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
27 28 29 30               25 26 27 28 29 30 31      29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2          1  2  3  4  5  6
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
                          31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1          1  2  3  4  5  6
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
                          30

>>> #list - Python data collection
>>> x = [1,2,45,9,8,766,69,65]
>>> #indexing
>>> x[0]
1
>>> x[1]
2
>>> x[-1]
65
>>> x = [1,2,3,[4,5,[6,7,8,[9,10,11]]]]
>>> x[3]
[4, 5, [6, 7, 8, [9, 10, 11]]]
>>> x[3][2]
[6, 7, 8, [9, 10, 11]]
>>> x[3][2][3]
[9, 10, 11]
>>> x[3][2][3][1]
10
>>> x=[1,2,3,4]
>>> y = [5,6,7,8]
>>> x+y
[1, 2, 3, 4, 5, 6, 7, 8]
>>> x-y
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x-y
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> x
[1, 2, 3, 4]
>>> y
[5, 6, 7, 8]
>>> x*y
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'list'
>>> x*5
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> x = []
>>> x.append(10)
>>> x
[10]
>>> x.append(20)
>>> x
[10, 20]
>>> x.append(30)
>>> x
[10, 20, 30]
>>> x.append(40)
>>> x
[10, 20, 30, 40]
>>> x.append(50)
>>> x.insert(2,100)
>>> x
[10, 20, 100, 30, 40, 50]
>>> x
[10, 20, 100, 30, 40, 50]
>>> x[2]=2000
>>> 
>>> x
[10, 20, 2000, 30, 40, 50]
>>> #update
>>> x
[10, 20, 2000, 30, 40, 50]
>>> x.pop()
50
>>> x
[10, 20, 2000, 30, 40]
>>> x.pop(30)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x.pop(30)
IndexError: pop index out of range
>>> x.pop()
40
>>> x.pop(2)
2000
>>> x
[10, 20, 30]
>>> x.remove(30)
>>> x
[10, 20]
>>> del x[1]
>>> x
[10]
>>> x
[10]
>>> x=[1,2,3,4,554,4,34,34,3,4]
>>> x.clear()
>>> x
[]
>>> x=[1,2,3,4]
>>> y=[9,8,7,6]
>>> x.extend(y)
>>> x
[1, 2, 3, 4, 9, 8, 7, 6]
>>> y
[9, 8, 7, 6]
>>> x = [1,9,9,91,1,2,2,3,3,2,3,3,4,5,6,7,7,7,7,7,8]
>>> x.count(9)
2
>>> x.count(7)
5
>>> x=[1,2,3,4,5,6]
>>> x.index(5)
4
>>> x=[1,2,3,4,5,6,5,5,5]
>>> x.index(5)
4
>>> x.index(5,5)
6
>>> x.index(100000)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    x.index(100000)
ValueError: 100000 is not in list
>>> x=[1,2,3,4]
>>> x.reverse()
>>> x
[4, 3, 2, 1]
>>> x=['a','c','e','f','b','d']
>>> x.sort()
>>> x
['a', 'b', 'c', 'd', 'e', 'f']
>>> x.sort(reverse=True)
>>> x
['f', 'e', 'd', 'c', 'b', 'a']
>>> x=[1,2,3,[4,5,6]]
>>> import copy
>>> y = copy.copy(x)
>>> x
[1, 2, 3, [4, 5, 6]]
>>> y
[1, 2, 3, [4, 5, 6]]
>>> id(x)
140571553474912
>>> id(y)
140571554226416
>>> id(x[3])
140571541495968
>>> id(y[3])
140571541495968
>>> del x[3][0]
>>> x
[1, 2, 3, [5, 6]]
>>> y
[1, 2, 3, [5, 6]]
>>> del x[2]
>>> x
[1, 2, [5, 6]]
>>> y
[1, 2, 3, [5, 6]]
>>> #deep copy
>>> x
[1, 2, [5, 6]]
>>> y=copy.deepcopy(x)
>>> x
[1, 2, [5, 6]]
>>> y
[1, 2, [5, 6]]
>>> id(x)
140571553474912
>>> id(y)
140571554445264
>>> id(x[2])
140571541495968
>>> id(y[2])
140571554444704
>>> [1, 2, [5, 6]]
[1, 2, [5, 6]]
>>> x=[1,99,100,12,13,14,5,4,34,23,232,456,76,509,78]
>>> value = int(input("Enter a number to search in the list : "))
Enter a number to search in the list : 78
>>> if value in x:
	print("found")
else:print("not found")

found
>>> if "found" value in x else "not found"
SyntaxError: invalid syntax
>>> "found" if value in x else "not found"
'found'
>>> 