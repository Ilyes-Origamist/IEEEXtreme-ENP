# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/happy_numbers/

# Result: 20% :(
# Solved by ilyes, IEEEXtreme 17.0
# tried to reduce computation, but it wasn't effective
# used a vectors to store previous results and use them.

from typing import Set

def isHappy(k: int, stop_false: Set[int], stop_true: Set[int]):
    if k in stop_true:
        return True, 0, 1
    else:
        k_old=k
        new_k=0
        history=[k]
        while True:
            b=k%10
            new_k=0
            while (k!=0): # calculate the sum of digits square
                new_k+=b**2
                k=k//10
                b=k%10
            k=new_k
            if new_k in stop_true:
                return True, 0, k_old
            elif new_k in stop_false:
                return False, k_old, 1
            elif new_k in history :
                return False, new_k, 1
            else:
                history.append(new_k)

a, b= map(int,input().split())
ans=0
stop_false=set()
stop_true={1}
for i in range(b, a-1, -1):
    check, k_false, k_true = isHappy(i, stop_false, stop_true)
    if check:  
        ans+=1
        stop_true.add(k_true)
    else:
        stop_false.add(k_false) 

print(ans)


