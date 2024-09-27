# Challenge Link:
# https://csacademy.com/ieeextreme-practice/task/ed8629419f140a5a2c923b049aba1224/

# Result: 100%
# Solved by ilyes, October 2023

# This corresponds to Knapsack 0/1 Problem
# Used dynamic programming to solve it

from typing import Tuple, List

def knapSack(Wmax: int, wt: List[int], val: List[int], n: int): 
  
    # Base Case 
    if n == 0 or Wmax == 0: 
        return 0
    # 
    weights=list(range(Wmax+1))
    T = [[0 for _ in range(Wmax+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in weights:
            new_w=w-wt[i-1]
            if (new_w>=0):
                T[i][w]=max(T[i-1][w], val[i-1]+T[i-1][new_w])
            else:
                T[i][w]=T[i-1][w]
    return T[-1][-1]

t = int(input())
for test in range(t):
    c, n = map(int, input().split())
    weight=[]
    power=[]
    while(len(weight)<n):
        ci, fi = map(int, input().split())
        weight.append(ci)
        power.append(fi)
    ans=knapSack(c,weight, power,n)
    print(ans)