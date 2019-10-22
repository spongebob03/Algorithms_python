#Divide and Conquer
import random
import time

#비교연산 횟수
cnt = 0
#실행시간
start = time.time()

#합병정렬
def mergesort(n,S):
    h=n//2
    m=n-h
    if(n>1):
        U = S[:h]
        V = S[h :]
        #print("split into two sets->",U,V)
        mergesort(h,U)
        mergesort(m,V)
        merge(h,m,U,V,S)

def merge(h,m,U,V,S):#U,V 배열 합쳐서 ->S
    #h,m은 배열 원소개수.
    i,j,k=0,0,0
    #print("before merge",U,V)
    global cnt
    while(i<h and j<m):
        cnt+=1
        if(U[i]<V[j]):
            S[k]=U[i]#합치는 S[k]요소 더 작은 수로 대체
            i+=1
        else:
            S[k]=V[j]
            j+=1
        k+=1
    if(i>=h):#U리스트 다 돈면 남은 V의 요소 그대로 S에
        S[k:]=V[j:]
    else:#V리스트 다 돈거
        S[k:]=U[i:]
    #print("mergesort->",S)
    return cnt


#DataSet
# #set1.
# data1=[i for i in range(1,51)]
# mergesort(len(data1),data1)
# #set2.
# data2=[i for i in range(50,0,-1)]
# mergesort(len(data2),data2)
#set3.
data3=[random.randint(1,50) for i in range(50)]
mergesort(len(data3),data3)
print("실행시간: ",time.time()-start,"seconds")
print("비교연산 횟수: ",cnt)

