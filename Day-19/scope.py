'''def display(n):
    n=n+10
    print('Inside:',n)
n=10
display(n)
print('Outside:',n)'''
'''
def display():
    global n
    n=n+10
    print('Inside:',n)
n=10
display()
print('Outside:',n)'''
'''
def display():
    global n
    n='PFS'
    print('Inside:',n)
n='Jfs'
display()
print('Outside:',n)
'''
def display():
    n='jfs'
    def update():
        nonlocal n
        n='pfs'
        print('updated course',n)
    update()
    print('final course',n)
display()