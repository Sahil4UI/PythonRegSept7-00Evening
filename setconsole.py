Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #SET
>>> #unordered python data collection
>>> x={1,2,3,4,5,6}
>>> x
{1, 2, 3, 4, 5, 6}
>>> x = {'a','b','c','d','e'}
>>> x
{'c', 'e', 'a', 'b', 'd'}
>>> x={1,2,3,4,5,6}
>>> x
{1, 2, 3, 4, 5, 6}
>>> x = {'a','b','c','d','e'}
>>> x
{'c', 'e', 'a', 'b', 'd'}
>>> x={"ram","shyam","ankit","rajesh"}
>>> x
{'ram', 'rajesh', 'ankit', 'shyam'}
>>> #every element in the set is unique
>>> #no duplicate values can be stored inside set
>>> x={'a','b','c','a','b','c','d'}
>>> x
{'d', 'c', 'a', 'b'}
>>> x={}
>>> type(x)
<class 'dict'>
>>> x=set(x)
>>> x
set()
>>> type(x)
<class 'set'>
>>> x.add('a')
>>> x
{'a'}
>>> x.add('b')
>>> x
{'a', 'b'}
>>> x.add('c')
>>> x
{'c', 'a', 'b'}
>>> x.add('d')
>>> x
{'d', 'c', 'a', 'b'}
>>> y = [1,1,1,2,3,3,4,5,5,5]
>>> y = list(set(y))
>>> y
[1, 2, 3, 4, 5]
>>> x
{'d', 'c', 'a', 'b'}
>>> x.discard('a')
>>> x
{'d', 'c', 'b'}
>>> x.discard('d')
>>> x
{'c', 'b'}
>>> x.discard('x')
>>> x
{'c', 'b'}
>>> y = ['a','b','c','d','e','f']
>>> y
['a', 'b', 'c', 'd', 'e', 'f']
>>> y = set(y)
>>> y
{'c', 'e', 'd', 'a', 'f', 'b'}
>>> list(y)
['c', 'e', 'd', 'a', 'f', 'b']
>>> sorted(list(y))
['a', 'b', 'c', 'd', 'e', 'f']
>>> x
{'c', 'b'}
>>> x.add('a')
>>> x
{'c', 'b', 'a'}
>>> x.pop()
'c'
>>> x
{'b', 'a'}
>>> x.pop()
'b'
>>> x
{'a'}
>>> x.pop()
'a'
>>> x = {1,2,3,4,5,6}
>>> x.clear()
>>> 
>>> x
set()
>>> x = {'a','b','c','d'}
>>> y = {'c','d','e','f'}
>>> #UNION
>>> #union - all but without repetition
>>> x.union(y)
{'c', 'e', 'd', 'a', 'f', 'b'}
>>> #intersection - common
>>> x.intersection(y)
{'c', 'd'}
>>> x
{'d', 'c', 'a', 'b'}
>>> y
{'f', 'c', 'd', 'e'}
>>> x.difference(y)
{'a', 'b'}
>>> y.difference(x)
{'f', 'e'}
>>> 
