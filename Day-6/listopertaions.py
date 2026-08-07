Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l=[]
>>> l=list()
>>> l=[1,2,3,4,5],'str',[12,13]
>>> l
([1, 2, 3, 4, 5], 'str', [12, 13])
>>> type(l)
<class 'tuple'>
>>> l=[1,12,1,2]
>>> type(l)
<class 'list'>
>>> l[2]
1
>>> l[0]
1
>>> l[3]
2
>>> l[1]
12
>>> l[:3]
[1, 12, 1]
>>> l[::-1]
[2, 1, 12, 1]
