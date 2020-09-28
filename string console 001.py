Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> string1="hello"
>>> string1.upper()
'HELLO'
>>> x='HeLLo'
>>> x.lower()
'hello'
>>> x.swapcase()
'hEllO'
>>> x
'HeLLo'
>>> x.endswith('e')
False
>>> x.endswith('o')
True
>>> x.startswith('H')
True
>>> x.startswith('H')
True
>>> x.startswith('h')
False
>>> x
'HeLLo'
>>> x.count('L')
2
>>> x.count('H')
1
>>> x.count('z')
0
>>> len(x)
5
>>> x
'HeLLo'
>>> x.center()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x.center()
TypeError: center() takes at least 1 argument (0 given)
>>> x.center(2)
'HeLLo'
>>> x.center(5)
'HeLLo'
>>> x.center(6)
'HeLLo '
>>> x.center(7)
' HeLLo '
>>> x.center(16)
'     HeLLo      '
>>> x.center(20,'*')
'*******HeLLo********'
>>> x.center(20,'-')
'-------HeLLo--------'
>>> x.center(20,'#')
'#######HeLLo########'
>>> x.center(20,'/')
'///////HeLLo////////'
>>> x.center(20,'*#')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x.center(20,'*#')
TypeError: The fill character must be exactly one character long
>>> x="               sahil                "
>>> x
'               sahil                '
>>> x.lstrip()
'sahil                '
>>> x.rstrip()
'               sahil'
>>> x
'               sahil                '
>>> x.strip()
'sahil'
>>> x='#######HeLLo########'
>>> x
'#######HeLLo########'
>>> x.strip("#")
'HeLLo'
>>> x="*#*#*#*#*#hello*#*#*#*#*#"
>>> x.strip("*")
'#*#*#*#*#hello*#*#*#*#*#'
>>> x
'*#*#*#*#*#hello*#*#*#*#*#'
>>> x.strip("*#")
'hello'
>>> x
'*#*#*#*#*#hello*#*#*#*#*#'
>>> x.replace("*"," ")
' # # # # #hello # # # # #'
>>> x.replace("*","")
'#####hello#####'
>>> x="hello"
>>> x.find("h")
0
>>> x.find('l')
2
>>> x.rfind('l')
3
>>> x="hello hello hello"
>>> x.find('e')
1
>>> x.rfind('e')
13
>>> x.find('e',0)
1
>>> x.find('e',2)
7
>>> x.find('z')
-1
>>> x.index('e')
1
>>> x.index('e',2)
7
>>> x.index('z')
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x.index('z')
ValueError: substring not found
>>> x=5
>>> x="hello"
>>> x.zfill(20)
'000000000000000hello'
>>> x.zfill(50)
'000000000000000000000000000000000000000000000hello'
>>> x="hello everyone"
>>> x.isdigit()
False
>>> x="78576587"
>>> x.isdigit()
True
>>> x="hlo"
>>> x.isalpha()
True
>>> x="hlo123"
>>> x.isdigit()
False
>>> x
'hlo123'
>>> x.isalnum()
True
>>> x="cow is an animal"
>>> x.split()
['cow', 'is', 'an', 'animal']
>>> #chr-character & ord-ordinal
>>> chr(65)
'A'
>>> chr(70)
'F'
>>> chr("6A")
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    chr("6A")
TypeError: an integer is required (got type str)
>>> chr(6A)
SyntaxError: invalid syntax
>>> chr(65)
'A'
>>> chr(90)
'Z'
>>> ord("q")
113
>>> ord("X")
88
>>> 