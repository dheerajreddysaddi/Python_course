'''def display(name,email='@gmail.com',password=''):
    print(f'name: {name}')
    print(f'email:{email}')
    print(f'password:{password}')
display('xyz','xyz@gmail.com','xyz@123')
display('xyz','xyz@gmail.com')
display('xyz')'''

'''def display(*name):
    print(name)
display('dheeraj')
display('dheeraj','reddy')
display('dheeraj','reddy','saddi')'''

def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)