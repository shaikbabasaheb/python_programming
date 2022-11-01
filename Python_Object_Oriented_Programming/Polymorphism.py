#method overloading using default parameters
class Demo:
    def add(self,a,b=0,c=0,d=0):
        print(a+b+c+d)
objadd=Demo()
objadd.add(2)
objadd.add(3,6)
objadd.add(3,6,7)
'''
= RESTART: C:/Users/Amazonian/Desktop/ps/OOP-Python/Polymorphism.py
2
9
16
'''

class Demo:
    def add(self,*values):
        print(sum(values))

objadd=Demo()
objadd.add(2)
objadd.add(3,4,8,6)
objadd.add(3,6,7,123,45,65,34,56,68,54,32)
'''
2
21
493
'''
#method overriding
class Parent:
    def transport(self):
        print('Bicycle')
class Child(Parent):
    def transport(self):
        super().transport()
        print('Bike')
obj=Child()
obj.transport()
'''
Bicycle
Bike
'''
