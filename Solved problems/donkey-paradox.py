# problem:
# https://csacademy.com/contest/interview-archive/task/donkey-paradox/

# result: 100%

n, m=map(int, input().split())
a1, b1=map(int, input().split())
a2, b2=map(int, input().split())

ans=0
for i in range(1,n+1):
    for j in range(1,m+1):
        d1=abs(a1-i)+abs(b1-j)
        d2=abs(a2-i)+abs(b2-j)
        if (d1==d2):
            ans+=1
print(ans)