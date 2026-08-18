'''n=int(input())
for i in range(n):
    for _ in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()'''
'''
n=int(input())
for i in range(n):
    for _ in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()'''
'''
n=int(input())
for i in range(n):
    for _ in range(n-i-1):
        print('',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for s in range(i):
        print('',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print()'''
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' X

n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
''' A
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
''' B
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' C
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1  :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

''' D
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

''' E
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1  or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

''' F
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' G
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or (i==n-1 and j<=m) or (j==m and i>=m)or (i==m and j>=m) or (j==n-1 and i>=m)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' H
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' I
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' J
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0  or j==n//2 or (i==n-1 and j<=n//2) or (i==n-2 and j==0):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''  K
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i+j==n-1 and i<=m) or (i==j and i>=m) or (i==m and j<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' K(no-)
n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or i + j == n - 1 or i == j and (j!=1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''
''' O
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 and n-1>j>0) or(j==0 and n-1>i>0) or (i==n-1 and n-1>j>0) or (j==n-1 and n-1>i>0):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

''' Y
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' V
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' M
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1) or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )'''
''' N
n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' V without bottom blanks
n = int(input())
# Loop only through the top rows to eliminate bottom blank lines
if n%2==0 or n%2!=0:
    n=n*2
    for i in range((n + 1) // 2):
        for j in range(n):
            if i == j or i + j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
else:
    print('give an odd number to print V')'''
    
''' R
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or (i==j and i>=m) or (i==m and j<=n-1) or (i<m and j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
''' P
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or (i==m and j<=n-1) or (i<m and j==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''  Q
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' Q
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 and n-1>j>0) or(j==0 and n-1>i>0) or (i==n-1 and n-1>j>0) or (j==n-1 and n-1>i>0) or(i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' S
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1) or (i==n//2) or (j==0 and i<n//2) or (j==n-1 and i>n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
''' V
n= int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or(i-j==m and i>=m) or (i+j==m+n-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''