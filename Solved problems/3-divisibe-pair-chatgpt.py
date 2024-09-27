# problem:
# https://csacademy.com/contest/interview-archive/task/3-divisible-pairs/

def sum3(arry):
    count_mods = [0, 0, 0]
    for num in arry:
        count_mods[num % 3] += 1

    ans = (count_mods[0] * (count_mods[0] - 1) // 2)  # Combination formula nC2 = n*(n-1)/2
    ans += count_mods[1] * count_mods[2]  # Multiplication of count_mods[1] and count_mods[2]

    return ans

n = int(input())
arry = list(map(int, input().split()))

ans = sum3(arry)
print(ans)
