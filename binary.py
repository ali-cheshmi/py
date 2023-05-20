

import random

def gues(l,i):
    low=0
    high=len(l)-1
    
    while low<=high:
        mid=int((low+high)/2)

        g=l[mid]

        if g==i:
            return g
        if (g)>i:
            high=mid-1
        if (g)<i:
            low=mid+1
    
        
l = [i for i in range(1, 101)]
i=70

print(gues(l,i))
