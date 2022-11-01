class Human:
    def __init__(self,c,n,h):
        self.color=c
        self.name=n
        self.height=h
        
    def run(self,n):
        print(n+' running....')
    def walk(self):
        print(self.name+' walking....')

obj=Human('Pink','Ogre',6.1)
print(obj.color,obj.name,obj.height)
obj.run('yujiro')
obj.walk()

'''
= RESTART: C:/Users/Amazonian/Desktop/ps/OOP-Python/Constructors.py
Pink Ogre 6.1
yujiro running....
Ogre walking....
'''
