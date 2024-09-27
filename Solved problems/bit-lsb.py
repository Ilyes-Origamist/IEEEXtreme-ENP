# Problem:
# https://csacademy.com/contest/interview-archive/task/least-significant-bit/

# result: 100%

def lsb(x):
    return x & -x
###
tests = int(input())
for i in range(tests):
    x = int(input())
    answer = lsb(x)
    print(answer)
