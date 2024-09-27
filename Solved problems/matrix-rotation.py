# problem:
# https://csacademy.com/contest/interview-archive/task/matrix_rotations/

# result: 100%
# sloved without numpy

def rot90(A):
    R = len(A)
    C = len(A[0])
    if C!=R:
        return 0
    else:
        A90=[[0 for _ in range(C)] for _ in range(R)]
        k=0
        for j in range(C-1,-1,-1):
            for i in range(R):
                A90[k][i]=A[i][j]
            k+=1
        return A90

def add_matrices(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

N = int(input())

A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

A90=rot90(A)
A180=rot90(A90)
A270=rot90(A180)
A = add_matrices(A, A90)
A = add_matrices(A, A180)
A = add_matrices(A, A270)
ans=[[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (A[i][j]>=1):
            ans[i][j]=1
        print(ans[i][j], end=" ")
    print()
