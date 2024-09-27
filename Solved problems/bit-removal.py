# problem link
# https://csacademy.com/contest/interview-archive/task/bit-removal/

# result: 100%

def bit_removal(x, y):
    result=x & ~y
    return result

###
tests = int(input())
for test in range(tests):
    x, y = map(int, input().split(' '))
    answer = bit_removal(x, y)
    print(answer)
