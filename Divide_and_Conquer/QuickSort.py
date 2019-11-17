#분할정복 알고리즘
#partition-> sort

import random
#DataSet
d = [random.randint(1,50) for i in range(0,50)]
print(d)

def Quicksort(left,right):
    if left < right:
        p =Partition(left,right)
        Quicksort(left,p-1)
        Quicksort(p+1,right)

def Partition(left,right):
    x = d[left] #pivot
    i = left+1 #itemFromLeft
    j = right #itemFromRight
    while True :
        while d[i] <= x and i < right:
            i+=1
        while d[j] >= x and j > left:
            j-=1
        if i < j :
            d[i],d[j] = d[j],d[i] #swap
        else:
            break
    # i >= j
    d[left],d[j] = d[j],d[left]
    return j #pivot index반환

Quicksort(0,len(d)-1)
print(d)





