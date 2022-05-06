'''하노이의 탑 알고리즘
    옮기려는 원반의 개수는 n개. 원반을 옮길 도착점 기둥은 to_pos, 보조기둥은 aux_pos'''

def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:
        print(from_pos,"->",to_pos)
        return

    #n개일때
    hanoi(n-1,from_pos, aux_pos, to_pos)
    print(from_pos,'->',to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)



print(hanoi(3,1,3,2))