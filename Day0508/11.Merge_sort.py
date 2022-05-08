''' 병합정렬'''

#1
def merge_sort(a):
    n=len(a)
    if n <= 1:
        return a

    mid = n//2
    g1 = merge_sort(a[:mid]) #재귀호출.
    g2 = merge_sort(a[mid:])
    result =[]

    print("g1:",g1)
    print("g2:",g2)

    while g1 and g2:
        if g1[0] < g2[0]: #g1, g2의 각 첫번째 값을 비교하여 g1 의 값이 작다면
            result.append(g1.pop(0)) #g1 의 첫번째 값을 result 에 저장
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d=[6,8,3,9,10,1,2,4,7,5]
print(merge_sort(d))

#2
def merge(a):
    n =len(a)
    if n<=1:
        return a

    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge(g1)
    merge(g2)

    i1=0
    i2=0
    ia=0

    while i1 < len(g1) and i2 <len(g2):
        if g1[i1] < g2[i2] : #g1의 값이 g2의 값보다 작다면
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else: #g2의 값이 g1 보다 작다면
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1) :
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6,8,3,9,10,1,2,4,7,5]
merge(d)
print(d)

