# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/8761fb7efefcf1d890df1d8d91cae241/

# Result: 100%
# Solved by ilyes, October 2023

def max_h(item):
    return item[1]

n = int(input())
a = []

for i in range(n):
    name, height = input().split()
    height = int(height)
    a.append((name, height))
x = sorted(a)
y = sorted(x, key=max_h, reverse=False)

l=len(y)
ji=1
j=1
print(y[0][0], end=" ")
for i in range(l-1):
    if (y[i+1][1]==y[i][1]):
        print(y[i+1][0], end=" ")
        j+=1
    else:
        print(ji, j)
        ji=j+1
        j+=1
        print(y[i+1][0], end=" ")

print(ji, j)
    