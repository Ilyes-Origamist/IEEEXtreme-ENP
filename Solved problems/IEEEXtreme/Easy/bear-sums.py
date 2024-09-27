# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/bear-sums

# Result: 100%
# Solved by ilyes, October 2023

# efficient method with time complexity O(n)
# idea from here:
# https://www.geeksforgeeks.org/check-exist-two-elements-array-whose-sum-equal-sum-rest-array/

t=int(input())
for j in range(t):
    sum, n=map(int, input().split())
    arry=[]; s=set(); found = 0
    if n==0:
        empty=input()
        empty=[]
        print("!OK")
    else:
        while len(arry)!=n:
            arry=list(map(int,input().split()))

        for i in range(n):
            val=sum-arry[i]
            if val in s:
                found=1
                if(arry[i] > val):
                    print(val, arry[i])
                    break
                else:
                    print(arry[i], val)
                    break
            if arry[i] not in s:
                s.add(arry[i])
        if found==0:
            print("!OK")
    