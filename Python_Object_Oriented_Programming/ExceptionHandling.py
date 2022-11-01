#1.Attribte Error:

class Demo:
    a=10
try:
    obj=Demo()
    print(obj.b)
except Exception as e:
    print(e)
'''
= RESTART: C:/Users/Amazonian/Desktop/ps/OOP-Python/ExceptionHandling.py
'Demo' object has no attribute 'b'
'''

#2 Filenot Found Error
try:
    fo=open('abcd.text','r')
    print(fo.read())
    fo.close()
except Exception as e:
    print(e)
    print('File not found')
'''
[Errno 2] No such file or directory: 'abcd.text'
File not found
'''

#3 Index Error:
l=[1,2,3,4,5,6,7]
try:
    for i in range(10):
        print(l[i],end=' ')
except Exception as e:
    print(e)
    print('Index out of bound')

'''
1 2 3 4 5 6 7 list index out of range
Index out of bound
'''

#4 Key Error:
d={'ABC':10,'def':100}
#print(d['hello'])
'''
Traceback (most recent call last):
  File "C:/Users/Amazonian/Desktop/ps/OOP-Python/ExceptionHandling.py", line 44, in <module>
    print(d['hello'])
KeyError: 'hello'
'''

#5 Name Error:
a=123
b=23
#print(a,b,c)
'''
Traceback (most recent call last):
  File "C:/Users/Amazonian/Desktop/ps/OOP-Python/ExceptionHandling.py", line 55, in <module>
    print(a,b,c)
NameError: name 'c' is not defined
'''

#6 Value Error:

a='Hello'
#b=int(a)
#print(b)
'''
Traceback (most recent call last):
  File "C:/Users/Amazonian/Desktop/ps/OOP-Python/ExceptionHandling.py", line 66, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: 'Hello'
'''

#7 Type Error:
try:
    l=[12,21,45,46,221]
    print(l[0])
except Exception as e:
    print(e)
else:
    print('No exception')
finally:
    print('program completed')
'''
12
No exception
program completed
'''
#8 Type Error:
a=10+'12'
print(a)


'''
Traceback (most recent call last):
  File "C:/Users/Amazonian/Desktop/ps/OOP-Python/ExceptionHandling.py", line 91, in <module>
    a=10+'12'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''














    
    
