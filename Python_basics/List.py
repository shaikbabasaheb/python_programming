l=[12,23,34,54,67,78]
print(type(l))
print(l[3])
print(l[1:])
print(l[-1])
print(l[::-1])
l[3]=123
print(l)
dl=[[1,2,3,4],[5,6,7,8,9]]
print(dl[0][1])
print(dl[1][0])
print(len(dl))
print(len(dl[0]))
l1=[1,2,3,4,5,6]
l2=[32,43,54,65,76]
print(l1+l2)
print(l1*3)
print(2*l2)
print(len(l1))
print(max(l1))
print(min(l1))
print(sum(l1))
print(54 in l2)
print(34 not in l1)
for i in range(len(l1)):
    print(l1[i],end=' ')
print()
for i in l1:
    print(i,end=' ')
print()
a=[]
a.append(10)
a.append(20)
a.extend([12,23,34,45])
print(a)
a.insert(2,344)
print(a)
a.remove(34)
print(a)
a.pop()
print(a)
a.pop(1)
print(a)

del a[1]
print(a)
c=[98,56,34,77,32,56,61,82,56,59]
c.sort()
print(c)
print(max(c))
print(min(c))
c.sort(reverse=True)
print(c)
print(sorted(c))
print(c.count(56))
print(c)
print(c.index(77))
c.reverse()
print(c)

'''List comphrehension '''
l=[ele for ele in range(10)]
print(l)
l1=[ele*ele for ele in range(10)]
print(l1)
l2=[ele for ele in range(100) if ele%2==0]
print(l2)
l2=[ele*3 for ele in range(10) if ele%2==0]
print(l2)

tple=[(i,i*2) for i in range(10)]
print(tple)

'''
========= RESTART: C:\Users\Amazonian\Desktop\ps\Python-basics\List.py =========
<class 'list'>
54
[23, 34, 54, 67, 78]
78
[78, 67, 54, 34, 23, 12]
[12, 23, 34, 123, 67, 78]
2
5
2
4
[1, 2, 3, 4, 5, 6, 32, 43, 54, 65, 76]
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
[32, 43, 54, 65, 76, 32, 43, 54, 65, 76]
6
6
1
21
True
True
1 2 3 4 5 6 
1 2 3 4 5 6 
[10, 20, 12, 23, 34, 45]
[10, 20, 344, 12, 23, 34, 45]
[10, 20, 344, 12, 23, 45]
[10, 20, 344, 12, 23]
[10, 344, 12, 23]
[10, 12, 23]
[32, 34, 56, 56, 56, 59, 61, 77, 82, 98]
98
32
[98, 82, 77, 61, 59, 56, 56, 56, 34, 32]
[32, 34, 56, 56, 56, 59, 61, 77, 82, 98]
3
[98, 82, 77, 61, 59, 56, 56, 56, 34, 32]
2
[32, 34, 56, 56, 56, 59, 61, 77, 82, 98]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
[0, 6, 12, 18, 24]
[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12), (7, 14), (8, 16), (9, 18)]
'''

