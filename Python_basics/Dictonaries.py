d={}
print(type(d))
d={'name':'abc', 'age':21}
print(d['name'])
print(d['age'])
print(d)
d['college']='mtiet'
print(d)

d1={'department':'cse'}
d.update(d1)
print(d)

print('dict comprehension')

d={i:i**2 for i in range(10)}
print(d)

d={i:i**3 for i in range(10) if i%2==0}
print(d)

dd={'name':{'fname':'ogre','lname':'yujiro'},'duration':6}
print(dd)
print(dd['name']['fname'])
print(dd['name']['lname'])
print(len(dd))

c=dd.copy()
print(c)

d={'a':1,'b':2,'c':3}
print(d.items())
print(d.values())
print(d.keys())


'''
= RESTART: C:/Users/Amazonian/Desktop/ps/Python-basics/Dictonaries.py
<class 'dict'>
abc
21
{'name': 'abc', 'age': 21}
{'name': 'abc', 'age': 21, 'college': 'mtiet'}
{'name': 'abc', 'age': 21, 'college': 'mtiet', 'department': 'cse'}
dict comprehension
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
{'name': {'fname': 'ogre', 'lname': 'yujiro'}, 'duration': 6}
ogre
yujiro
2
{'name': {'fname': 'ogre', 'lname': 'yujiro'}, 'duration': 6}
dict_items([('a', 1), ('b', 2), ('c', 3)])
dict_values([1, 2, 3])
dict_keys(['a', 'b', 'c'])
'''


















