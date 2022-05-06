#a,b를 입력했을 때, 두 수의 최대 공약수를 구하시오

def find_gcd(a,b):
    i = min(a,b)
    while True:
        if a % i == 0 and b % i ==0:
            return i
        i = i - 1

print(find_gcd(12,34))

#유클리드 방식을 이용하여 최대 공약수를 구하는 프로그램을 작성하라

def ucld(a,b):
    if b == 0:
        return a
    return ucld(b,a%b)


print(ucld(12,34))