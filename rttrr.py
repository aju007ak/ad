import sys,string, math, itertools

def bonAppetit(a,b,c,D):
    dif = (sum(D) - D[k]) / 2
    if c == dif:
        return 'Bon Appetit'
    else:
        return str(D[b] // 2)


a, b = map(int, input().split())
D = list(map(int, input().split()))
c = int(input())
result = bonAppetit(a, b, c, D)
print(result)
