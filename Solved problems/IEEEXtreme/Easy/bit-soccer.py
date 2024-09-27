# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/bit-soccer/

# Result: 100%
# Solved by ilyes, October 2023

from typing import List
def bit_soccer(players: List[int], perf: int):
    b=0
    for score in players:
        if score<=perf:
            check=score|perf
            if check==perf:
                b|=score
                if b==perf:
                    return "YES"
    return "NO"
    
players=[]
n=int(input())
players=list(map(int, input().split()))
n_query=int(input())
for query in range(n_query):
    q=int(input())
    print(bit_soccer(players.copy(), q))
