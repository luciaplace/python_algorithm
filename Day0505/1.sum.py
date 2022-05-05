# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘
# n을 입력하여 1부터 n까지의 숫자를 더한 값을 출력하라.


# 방법 1
def sum_n(n):
    s=0
    for i in range(1,n+1):
        s += i
    return s

print(sum_n(10))
print(sum_n(100))

#방법 2
def sum_n2(n):
    return n*(n+1)//2

print(sum_n2(10))
print(sum_n2(100))
