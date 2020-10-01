Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Screen()
<turtle._Screen object at 0x7fd5c37a8790>
>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> turtle.shape("turtle")
>>> turtle.forward(200)
>>> turtle.shape("rectangle")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    turtle.shape("rectangle")
  File "<string>", line 8, in shape
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named rectangle
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.reset()
>>> for i in range(4):
	turtle.forward(200)
	turtle.left(90)

>>> turtle.reset()
>>> radius=100
>>> turtle.circle(radius)
>>> turtle.reset
<function reset at 0x7fd5c4126830>
>>> turtle.reset()
>>> for i in range(500):
	turtle.forward(10)
	turtle.left(90)

Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    turtle.forward(10)
  File "<string>", line 8, in forward
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1637, in forward
    self._go(distance)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3195, in _goto
    self._update() #count=True)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 744, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> for i in range(5):
	print(i)

0
1
2
3
4
>>> turtle.reset()
>>> for i in range(500):
	turtle.forward(10+i*5)
	turtle.left(90)

Traceback (most recent call last):
  File "<pyshell#33>", line 2, in <module>
    turtle.forward(10+i*5)
  File "<string>", line 8, in forward
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1637, in forward
    self._go(distance)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3179, in _goto
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 744, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> 