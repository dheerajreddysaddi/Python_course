Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4]
id(l)
1639599541696
l.append(12)
l
[1, 2, 3, 4, 12]
#append is used to add the elements at the end of the list
id(l)
1639599541696
l.insert(1,11)
l
[1, 11, 2, 3, 4, 12]
#inserted at a particular place l.insert(position,number u want to insert)
l.extend([1,1,1])
l
[1, 11, 2, 3, 4, 12, 1, 1, 1]
l[2]=12
l
[1, 11, 12, 3, 4, 12, 1, 1, 1]
#we have modified the element in the above list
l.pop()
1
l.pop()
1
l.pop()
1
l.pop()
12
#pop deletes the last element
#pop deletes the last element
l.pop(1)
11
#pop deletes the indexed element if mentioned
l
[1, 12, 3, 4]
l.remove(12)
l
[1, 3, 4]
#remove is used to del the element by directly mentioning the element other than index
l.clear()
l
[]
#clear is to remove all elements in the list
l.del()
SyntaxError: invalid syntax
l(id)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l(id)
TypeError: 'list' object is not callable
id(l)
1639599541696
1639599541696
1639599541696
l=[1,5,2,8,9]
max(l)
9
min(l)
1
sorted(l)
[1, 2, 5, 8, 9]
l.reverse()
l
[9, 8, 2, 5, 1]
l.sort()
>>> l
[1, 2, 5, 8, 9]
>>> #sorted gives temporary changes whereas sort give permanent change
>>> sum(l)
25
>>> #sum of all elementa in the list
>>> a=l.copy()
>>> a
[1, 2, 5, 8, 9]
>>> a.append(12)
>>> a
[1, 2, 5, 8, 9, 12]
>>> l
[1, 2, 5, 8, 9]
>>> #copy doesnt change the original list
>>> all([0,'',[],(),{},set(),False])
False
>>> any([1,'',[],(),{},set(),False])
True
>>> l
[1, 2, 5, 8, 9]
>>> l.count(3)
0
>>> l.count(1)
1
>>> l.index(2)
1
>>> l.index(5)
2
>>> l[[0,2],[1,4]]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    l[[0,2],[1,4]]
TypeError: list indices must be integers or slices, not tuple
>>> l=[[0,2],[1,4]]
>>> l
[[0, 2], [1, 4]]
>>> l[0,1]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l[0,1]
TypeError: list indices must be integers or slices, not tuple
>>> l[0][1]
2
>>> l[0][0]
0
