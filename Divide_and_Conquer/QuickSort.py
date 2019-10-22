#분할정복 알고리즘
#partition-> sort

import random
#DataSet
#set1
#set2
#d=[i for i in range(50,0,-1)]
#set3
d = [random.randint(1,50) for i in range(0,50)]
print(d)

def Partition(left,right):
    x = d[left]
    i = left+1 #itemFromLeft
    j = right #itemFromRight
    while i <= j :
        while d[i] <= x and i <= right:
            i+=1
        while d[j] >= x and j >= (left+1):
            j-=1
        if i <= j :
            d[i],d[j] = d[j],d[i] #swap
        else:
            break
    d[left],d[j] = d[j],d[left]
    return j #pivot index반환

def Quicksort(left,right):
    if left < right:
        p=Partition(left,right)
        Quicksort(left,p-1)
        Quicksort(p+1,right)

Quicksort(0,49)
print(d)





