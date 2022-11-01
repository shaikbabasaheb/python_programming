#Single inheritance
class Baseclass:
    a=10
    b=20
    def display(self):
        print('Base class')
class Derivedclass(Baseclass):
    c=30
    d=40
    def show(self):
        print('Derived class')
obj=Derivedclass()
print(obj.a,obj.b,obj.c,obj.d)
obj.display()
obj.show()
'''
= RESTART: C:/Users/Amazonian/Desktop/ps/OOP-Python/Inheritance.py
10 20 30 40
Base class
Derived class
'''
#MultiLevel inheritance
class gpclass:
    def gpdisplay(self):
        print('Grand parent class')
class pclass(gpclass):
    def pdisplay(self):
        print('Parent class')
class cclass(pclass):
    def cdisplay(self):
        print('Child class')
obj=cclass()
obj.cdisplay()
obj.pdisplay()
obj.gpdisplay()

'''
Child class
Parent class
Grand parent class
'''

#Hierachial inheritance
class Parent:
    def pdisplay(self):
        print('parent class')
class Son(Parent):
    def sdisplay(self):
        print('Son class')
class Daughter(Parent):
    def ddisplay(self):
        print('Daughter class')

sonobj=Son()
sonobj.sdisplay()
sonobj.pdisplay()

daughterobj=Daughter()
daughterobj.ddisplay()
daughterobj.pdisplay()

'''
Son class
parent class
Daughter class
parent class
'''
#Multiple inheritance
class Father:
    def fdisplay(self):
        print('father class')
class Mother:
    def mdisplay(self):
        print('mother display')
class Child(Father,Mother):
    def cdisplay(self):
        print('child class')
obj=Child()
obj.cdisplay()
obj.mdisplay()
obj.fdisplay()
'''
child class
mother display
father class
'''
