s=set()
print(type(s))
a={10,20,30,40}
print(type(a))
print(len(a))
a.add(50)
a.add(60)
a.add(70)
print(a)
a.remove(70)
print(a)
a.discard(60)
a.discard(100000)
print(a)
a.pop()
print(a)
a.clear()
print(a)
del a

s={10,20,30}
s.update({30,40,50})
print(s)

s={10,20,30,40,50}
print(10 in s)
for i in s:
    print(i,end=' ')
print()

s={10,20,30}
t={10,20,30,40,50,60}
print(s.issubset(t))
print(t.issubset(s))
print(t.issuperset(s))
print(s.issuperset(t))

print(t.union(s))
print(s.intersection(t))
print(t.difference(s))

s={10,20,30,40,100}
t={10,20,30,40,50,60}
print(s.symmetric_difference(t))

s={10,20,30,100}
t={10,20,30,40,50,60}
s.update(t)
print(s)

s={10,20,30,40,50}
t={10,20}
s.intersection_update(t)
print(s)

t={10,20,30,40,50,60}
s=t.copy()
print(s)


'''
= RESTART: C:\Users\Amazonian\Desktop\ps\Python-basics\Sets.py
<class 'set'>
<class 'set'>
4
{70, 40, 10, 50, 20, 60, 30}
{40, 10, 50, 20, 60, 30}
{40, 10, 50, 20, 30}
{10, 50, 20, 30}
set()
{50, 20, 40, 10, 30}
True
50 20 40 10 30 
True
False
True
False
{40, 10, 50, 20, 60, 30}
{10, 20, 30}
{40, 50, 60}
{50, 100, 60}
{100, 40, 10, 50, 20, 60, 30}
{10, 20}
{50, 20, 40, 10, 60, 30}
'''
