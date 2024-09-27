# problem:
# https://csacademy.com/contest/interview-archive/task/binary-stable-sort/

# result: 100%

from typing import Tuple, List

def binary_stable_sort(childs: List[Tuple[str, str]]):
    r_team = []
    b_team = []
    for i in range(len(childs)):
        if childs[i][1] == "B":
            b_team.append(childs[i])
        elif childs[i][1] == "R":
            r_team.append(childs[i])
    sorted_teams = b_team + r_team
    for i in range(len(childs)):
        childs[i] = sorted_teams[i]

n = int(input())
array = []
for i in range(n):
    name, value = input().split(' ')
    array.append((name, value))

binary_stable_sort(array)
for element in array:
    print(element[0])
