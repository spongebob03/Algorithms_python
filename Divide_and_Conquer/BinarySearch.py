#Divide and Conquer

slist=[10,23,53,60,78,83,85,91,100]#정렬된 배열
x=int(input("찾고싶은 정수:"))

#이진검색
#Recursive Algorithm
def Binary_Search(low,high,list,x):
    if(low>high):
        return "없음"
    else:
        mid=(low+high)//2
        if (x==list[mid]):
            return str(mid)+"번째에 있음"
        elif(x<list[mid]):#왼쪽으로 반띵
            return Binary_Search(low,mid-1,list,x)
        else:#오른쪽으로 반띵
            return Binary_Search(mid+1,high,list,x)

#iterative Algorithm
def Binary_Search2(list,x):
    low=0
    high=len(list)-1
    loca=-1
    while(low<=high):
        mid=(low+high)//2
        if(x==list[mid]):
            loca=mid
            break
        elif(x<list[mid]):
            high=mid-1
        else:
            low=mid+1
    if loca==-1: return ("찾는 수 없음")
    return loca

print(Binary_Search(0,len(slist)-1,slist,x))
print("위치:",Binary_Search2(slist,x))



