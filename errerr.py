import sys,string
a = input()
b = len(s)
for j in range(b-2,-1,-1) :
    #print('arr len = ', j+1)
    for i in range(0,b-j) :
        li, ri = i,j+i
        c2 = s[li:ri + 1]
        #print(li, ri, s2)
        if c2 > s :
            print(c2)
            sys.exit()
