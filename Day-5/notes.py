int         ->int(input())
float       ->float(input())
str         ->input()
#str doesnt require mapping for input
list of str->   input().split()
list of int->   list(map(int,input().split()))
list of float-> list(map(float,input().split()))

tuple of str->   tuple(input().split())
tuple of int->   tuple(map(int,input().split()))
tuple of float-> tuple(map(float,input().split()))

set of str->   set(input().split())
set of int->   set(map(int,input().split()))
set of float-> set(map(float,input().split()))

#example
#id,pwd=input().split() {multiple inputs are given}

eval ->eval(input()) #all kind of operations and input funtions can be done
#not recommended

str->#concardination,repetition,slicing(accesing the group of values),indexing,membership
#slicing -> [start:end+1:step]->s[0:len:1]
