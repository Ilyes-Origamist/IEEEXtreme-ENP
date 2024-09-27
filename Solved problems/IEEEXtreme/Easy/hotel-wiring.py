# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/hotel-wiring/

# Result: 100%
# Solved by ilyes, October 2023

from typing import List
def max_changes(N: int, K: int, room_list: List[int]):
    r=N//2; M=len(room_list); l=M; ans=0
    room=sorted(room_list)
    for i in range(M):
        if room[i]>r:
            l=i
    if l>=K-1:
        ans=K*N-sum(room[0:K])+sum(room[K:M])
    else:
        b=K-l
        if b%2==0:
            ans=K*N-sum(room[0:K])+sum(room[K:M])
        else:
            ans=K*(N-sum(room[0:K]))+N-room[K]+sum(room[K+1:M])
    return ans

test=int(input())
for t in range(test):
    M, N, K=map(int, input().split())
    rooms=[]
    while len(rooms)<M:
        rooms.append(int(input()))
    answer=max_changes(N, K, rooms)
    print(answer)
