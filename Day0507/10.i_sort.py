'''삽입정렬
    리스트 a를 정렬하시오'''

#1

def find_ins_idx(r,v):
    for i in range(0,len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort(a):
    result=[]
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result,value)
        result.insert(ins_idx,value)
    return result

li = [1,3,55,4,14,22,99]
print(ins_sort(li))