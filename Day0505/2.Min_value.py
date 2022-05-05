# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어 보세요.

def find_min(n):
    a = len(n)
    Min_value = n[0]

    for i in range(1,a):
        if n[i] < Min_value:
            Min_value = n[i]

    return Min_value

li = [11,4,2,3,6,7,5]
print(find_min(li))