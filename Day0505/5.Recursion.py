#재귀 호출
'''재귀 호출시에는 종료 조건이 필요하다. 만약 종료 조건이 없는경우에는 재귀 에러가 발생하게 된다.

def hello():
    print('hello')
    hello()

hello()
'''

#재귀 호출을 이용하여 연속한 숫자의 곱을 구하는 알고리즘 프로그램을 작성하라
# n을 입력시 1부터 n까지 연속한 숫자를 곱한 값을 구하여라

def fact(n):
    if n<=1:
        return 1
    return n * fact(n-1)

print(fact(5))

#1부터 n까지의 합을 구하는 프로그램을 재귀 호출을 이용하여 작성하라

def sum_fact(n):
    if n<1:
        return 0
    return n + sum_fact(n-1)

print(sum_fact(10))

#숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보세요.

def find_maximum(a,b):
    if b == 1 : #숫자 1개면 그 숫자가 최대값이 됨.
        return a[0]
    max_num_1 = find_maximum(a,b-1) #find_max_1 = find_maximum(리스트, 리스트 길이 -1)
    if max_num_1 > a[b-1]:
        return max_num_1
    else:
        return a[b-1]

li = [1,2,3]
print(find_maximum(li, len(li)))



