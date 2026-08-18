'''1-10
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)'''
        
''' 10-1
def display(n):
    if n>10:
        return
    display(n+1)
    print(n)   
display(1)'''
''' SUM of N num
def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(8))'''

'''display product of N
def displayprod(n):
    if n==0:
        return 1
    return n*displayprod(n-1)
print(displayprod(5))'''

''' str 
def displaystr(ind):
    if ind==len(s):
        return 
    print(s[ind],end=' ')
    displaystr(ind+1)
    
s='Python Programming'
displaystr(0)'''

''' str rev
def displaystr(ind):
    if ind==len(s):
        return 
    displaystr(ind+1)
    print(s[ind],end=' ')    
s='Python Programming'
displaystr(0)'''

''' s[:1]->s[:n]
def displaystr(n):
    if n>len(s):
        return  
    print(s[:n])
    displaystr(n+1)   
s='Python Programming'
displaystr(1)'''

''' str with index (sliding window)
def display(i,w):
    if i>len(s)-w:
        return
    print(s[i:i+w])
    display(i+1,w)
s='Dheeraj_Reddy'
display(0,5)'''

''' 
def display(n):
    if n==0:
        return 
    display(n//10)
    print(n%10) 
n=456781
display(n)'''
''' sum of all digits in a given number 
def display(n):
    if n==0:
        return 0
    return n%10 + display(n//10) 
n=456781
print(display(n))'''

 

    

