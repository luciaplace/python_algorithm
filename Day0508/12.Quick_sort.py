'''퀵 정렬
    -> 기준 값을 하나 선택한 후 그 값보다 큰 그룹, 작은그룹으로 나누어 재귀호출을 통해 정렬한다.
        최종적으로 반환시에는 정렬된 작은그룹 + 기준 + 큰그룹으로 반환한다. '''

#1
def quick_sort(a):
    n = len(a)
    if n<= 1:
        return a
    pivot = a[-1] #기준값을 리스트의 마지막 값으로 잡기
    g1 =[]
    g2 =[]

    for i in range(0,n-1):
        if a[i] < pivot: #리스트의 첫 값이 마지막 값보다 작다면
            g1.append(a[i])
        else:
            g2.append(a[i])


    return quick_sort(g1) + [pivot] + quick_sort(g2)

d= [2,6,4,87,1,44,66,3]
print(quick_sort(d))

#2
# 리스트 a, 시작점 start, 끝점 end

def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)

def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

d = [6,8,3,9,10,1,2,4,7,5]
quick_sort(d)
print(d)

