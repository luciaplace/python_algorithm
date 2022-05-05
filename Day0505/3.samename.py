#이름이 n개 들어있는 리스트 중에서 중복되는 이름을 찾아 집합으로 출력하라.


def find_same(n):
    a = len(n)
    result = set()

    for i in range(0,a-1):
        for j in range(i+1,a):
            if n[i] == n[j]:
                result.add(n[i])

    return result

li = ['mike','tom','kelly','jason','lucia']
print(find_same(li))

#n명중 두명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어보시오

def find_pairs(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            print(a[i],"-",a[j])

print(find_pairs(li))



