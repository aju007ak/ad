import sys, string, math
a,b = input().split()
a,b = int(a), int(b)
L = [ int(x) for x in input().split()]
for i in range(0,b) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum(L[a-1:b]))
