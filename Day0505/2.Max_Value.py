# 숫자 N개가 들어있는 리스트 중에서 최대값을 출력하라

def find_max(a):
    n = len(a)
    max_value = a[0]
    for i in range(1,n):
        if a[i] > max_value:
            max_value = a[i]

    return max_value

li = [2,4,8,7,3,6]
print(find_max(li))


#숫자 n개가 있는 리스트가 있다. n개의 숫자 중 최댓값이 있는 인덱스를 출력하라

def find_max_idx(a):
    n=len(a)
    max_idx = 0
    for i in range (1,n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

maxlist = [66,22,55,33,11]
print(find_max_idx(maxlist))


