class Demo:
    __a=10
    b=32
    def __display(self):
        print(self.__a)
        print('display method')
    def show(self):
        self.__display()

obj=Demo()
obj.show()
print(obj.b)
#print(obj.__a) invalid

'''
= RESTART: C:/Users/Amazonian/Desktop/ps/OOP-Python/Encapsulation.py
10
display method
32
'''
