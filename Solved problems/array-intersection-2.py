# problem
# https://csacademy.com/contest/interview-archive/task/array-intersection/

# result: 57.89%

def array_intersection(S1, S2):
    S=[]
    for i in S1:
        if i in S2:
            S.append(i)
            S2.remove(i)
    S=sorted(S)
    return S

N1, N2=map(int, input().split())

S1=[]
while(len(S1)!=N1):
    S1=list(map(int, input().split()))

S2=[]
while(len(S2)!=N2):
    S2=list(map(int, input().split()))

S=array_intersection(S1, S2)
print(len(S))

for j in S:
    print(j , end=" ")