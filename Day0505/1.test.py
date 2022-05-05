# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 For 반복문으로 만들어 보세요.

#--------------------------- O(n)
def squared(n):
    s=0
    for i in range(1,n+1):
        s += (i**2)

    return s

print(squared(10))

#--------------------------- O(1)

def squared2(n):
    return n*(n+1)*(2*n+1) //6

print(squared2(10))
