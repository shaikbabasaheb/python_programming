weeks=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
print(weeks)
print(type(weeks))
print(weeks[0])
#weeks[1]='day' invalid
li=list(weeks)
li[1]='Monday'
weeks=tuple(li)
print(weeks)
print(weeks[2:])
print(weeks[::-1])
month=('jan','feb','mar','apr')
print(weeks+month)
t=(12,34,54,56,56,56)
print(sum(t))
print(10 in t)
print(t.count(56))
print(t.index(54))
for i in t:
    print(i,end=' ')
print()
tt=((12,23),56,3,32,56)
print(tt[0][1])
print(tt[0])
print(tt[1])

'''
= RESTART: C:/Users/Amazonian/Desktop/ps/Python-basics/Tuples.py
('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
<class 'tuple'>
sunday
('sunday', 'Monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
('tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
('saturday', 'friday', 'thursday', 'wednesday', 'tuesday', 'Monday', 'sunday')
('sunday', 'Monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'jan', 'feb', 'mar', 'apr')
268
False
3
2
12 34 54 56 56 56 
23
(12, 23)
56
'''
