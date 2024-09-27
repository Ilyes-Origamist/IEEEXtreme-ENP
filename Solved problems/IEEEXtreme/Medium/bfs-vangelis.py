# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/979a09a0cd8c4e98dd0a690f39a55bd2/

# Result: 0%
# Using BFS (Breadth First Search)

def bfs(node, parent):
    visited[node] = True
    for nei in adj_dict[node]:
        if not visited[nei]:
            cycle_found = bfs(nei, parent=node)
            if cycle_found:
                return True
        elif nei != parent:
            return True
    return False

def detect_cycle():
    for v in vertices:
            if not visited[v]:
                if bfs(v,-1):
                    return 1
    return 0

# test cases
t = int(input())
for j in range(t):
    n, m = map(int, input().split())
    # edges list
    edges = []
    while True:
        inputs = list(map(int, input().split()))
        if len(inputs) == 2*m:
            break
    i = 0
    while i < 2*m:
        edges.append((inputs[i], inputs[i+1]))
        i += 2

    # vertices List
    vertices = []
    for k in range(n):
        vertices.append(k)
    # adjacent dictionnary
    adj_dict = {}
    for x, y in edges:
        if x not in adj_dict:
            adj_dict[x] = []
        if y not in adj_dict:
            adj_dict[y] = []
        adj_dict[x].append(y)
        adj_dict[y].append(x)

    visited = {v: False for v in vertices}
    cycle = detect_cycle()
    print(cycle)