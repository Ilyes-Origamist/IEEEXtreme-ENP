# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/coupon-codes

# Result: 50%
# Solved by ilyes, October 2023
# Used brute force, should be optimized

n=int(input())
codes=[]
while len(codes)!=n:
    code_in=input()
    codes.append(code_in)


ans=0
for i in range(n-1):
    for j in range(i+1,n):
        diff=0
        for s in range(14):
            if codes[i][s]!=codes[j][s]:
                diff+=1
        if diff==1:
            ans+=1

print(ans)
