import math 
  

def sum(a): 
  
    s= 0
    for i in range(1,a+1): 
        s= s+ (2 * i - 1) * (2 * i - 1) 
    return s
      

a= 10
print(sumOfSeries(a)) 
