''' 리스트에서 특정 숫자의 위치를 찾는 알고리즘
리스트 a를 입력했을때, x값의 위치를 찾으시오. 만약 찾지 못한다면, -1을 반환하라'''

def search(a,x):
    n=len(a)
    for i in range (n):
        if x == a[i]:
            return i

    return -1

li = [33,22,11,44,6,11,77,2,3,99]
print(search(li,3))
print(search(li,100))

'''찾는 값이 나오는 모든 위치를 리스트로 반환하는 탐색 알고리즘을 만들어보세요. 만약 찾는 값이 없는 경우에는 빈 리스트를 반환하세요'''

def search_idx(a,x):
    n = len(a)
    result=[]
    for i in range(n):
        if a[i] == x:
            result.append(i)
    return result

print(search_idx(li,11))
print(search_idx(li,100))

'''다음과 같이 학생 번호와 이름이 리스트로 주어졌을때, 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로 돌려주는 함수를 작성하라
    만약 해당하는 학생 번호가 없는경우 ?를 반환하라'''

no = [39, 14, 67, 105]
name = ['justin','john','mike','summer']


def search_stu(no,name,idx):
    n = len(no)
    result = "?"
    for i in range(n):
        if no[i] == idx:
            result = name[i]

    return result

print(search_stu(no,name,39))



