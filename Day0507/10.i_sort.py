'''삽입정렬
    리스트 a를 정렬하시오'''

#1

def find_ins_idx(r,v):
    for i in range(0,len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result=[]
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result,value)
        result.insert(ins_idx,value)
    return result

li = [1,3,55,4,14,22,99]
print(ins_sort(li))


#2

def ins_sort2(a):
    n=len(a)
    for i in range(1,n): #1부터 n-1까지 그래야 끝까지 비교가능!
        key=a[i] #i번 위치에 있는 값을 key에 저장
        #j를 i 바로 왼쪽 위치로 저장
        j=i-1
        #리스트 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
            a[j+1]=key

            print(d)
d=[2,4,5,1,3]
ins_sort2(d)
