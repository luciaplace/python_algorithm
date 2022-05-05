#n이라는 숫자를 입력했을 시에 1부터 n까지 연속한 숫자를 곱한 값을 구하여라

def fact(n):
    f=1
    for i in range(1,n+1):
        f *= i
    return f

print(fact(5))