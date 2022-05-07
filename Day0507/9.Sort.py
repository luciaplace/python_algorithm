''' 선택정렬
    리스트 a를 입력시 a를 정렬한 새로운 리스트를 출력하시오. '''

#1
def find_min_idx(a):
    n=len(a)
    min_idx = 0
    for i in range(n):
        if a[i]<a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result=[]
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

li = [2,6,4,44,1,9,8,76]
print(sel_sort(li))


#2
li2 = [2,6,4,44,1,9,8,76]
def sort2(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx =j
        a[i],a[min_idx] = a[min_idx],a[i]
    return a

print(sort2(li2))