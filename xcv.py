import sys, string, math
a,b = input().split()
a,b = int(a), int(b)
L = [ int(x) for x in input().split()]
for i in range(0,a) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(min(L[a-1:b]))
