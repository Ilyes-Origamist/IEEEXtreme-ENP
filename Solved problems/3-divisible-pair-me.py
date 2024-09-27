# problem:
# https://csacademy.com/contest/interview-archive/task/3-divisible-pairs/

# result: 50%

def sum3 (arry):
    ans=0
    n=len(arry)
    for i in range(n-1):
        for j in range(i+1,n):
            k=(arry[j]%3+arry[i]%3)%3
            if k==0:
                ans+=1
    return ans

n=int(input())
arry=[]
while len(arry)!=n:
    arry=list(map(int, input().split()))

ans=sum3(arry)
print(ans)