Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data={'name':'Dheeraj','batch':63,'course':'PFS'}
data{'name'}
SyntaxError: invalid syntax
data['name']
'Dheeraj'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    data['age']
KeyError: 'age'
get('age')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    get('age')
NameError: name 'get' is not defined. Did you mean: 'set'?
data.get('age','key not present')
'key not present'
data['batch']=64
data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS'}
data['age']=21
data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'age': 21}
data.update({'phno':8688665522,'email':'saddidheerajreddy@gmail.com'})
data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'age': 21, 'phno': 8688665522, 'email': 'saddidheerajreddy@gmail.com'}
data.pop('age')
21
data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'phno': 8688665522, 'email': 'saddidheerajreddy@gmail.com'}
data.pop()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.popitem()
('email', 'saddidheerajreddy@gmail.com')
>>> data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'phno': 8688665522}
>>> data.clear()
>>> data
{}
>>> data={'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'age': 21, 'phno': 8688665522, 'email': 'saddidheerajreddy@gmail.com'}
>>> data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'age': 21, 'phno': 8688665522, 'email': 'saddidheerajreddy@gmail.com'}
>>> data.keys()
dict_keys(['name', 'batch', 'course', 'age', 'phno', 'email'])
>>> data.items()
dict_items([('name', 'Dheeraj'), ('batch', 64), ('course', 'PFS'), ('age', 21), ('phno', 8688665522), ('email', 'saddidheerajreddy@gmail.com')])
>>> data.values()
dict_values(['Dheeraj', 64, 'PFS', 21, 8688665522, 'saddidheerajreddy@gmail.com'])
>>> sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno']
>>> sorted(data,reverse=True)
['phno', 'name', 'email', 'course', 'batch', 'age']
>>> max(data)
'phno'
>>> min(data)
'age'
>>> data.setdefault('gender','')
''
>>> data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'age': 21, 'phno': 8688665522, 'email': 'saddidheerajreddy@gmail.com', 'gender': ''}
>>> data.setdefault('name','')
'Dheeraj'
>>> data
{'name': 'Dheeraj', 'batch': 64, 'course': 'PFS', 'age': 21, 'phno': 8688665522, 'email': 'saddidheerajreddy@gmail.com', 'gender': ''}
>>> len(data)
7
>>> all(data)
True
>>> any(data)
True
>>> True
True
