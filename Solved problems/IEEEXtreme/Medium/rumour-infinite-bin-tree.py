# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/9ca8fafd184f553a903734761546a224/

# Result: 100%
# Solved by ilyes, October 2023

# Idea:
# Consider the first vortex (a)
# To go to the previous level on the tree 
# on the same branch divide by 2 
# since it is a full binary tree.
# The distance is always 1 between these two vertices
# which is the minimum distance between two levels.
# If you repeat this operation, you will reach 
# the vortex (1) which is the root of the tree
# and you just found the shortest path from (a) to (1)

# Now if you consider another vortex (b)
# and apply the same operation at the same time,
# We want to keep them at similar level, 
# or with a difference of a maximum of one level
# to eventually reach the same vortex
# and find the minimal path.
# There are two cases to consider:

# 1. (a) is greater than (b)
# In this case, either
# (a) and (b) are on the same level,
# or (a) is on a higher level than (b)'s.
# Dividing (a) by two will decrease its level by one
# If we repeat this until (a) becomes smaller than (b)
# then (a) could be on the same level than (b)
# or on a lower level.
# which brings to the second case:

# 2. (a) is smaller than (b)
# In this case, either
# (a) and (b) are on the same level,
# or (a) is on a lower level than (b)'s.
# Then here, we will lower the level of (b) instead
# (using the division by 2) until (b) becomes
# smaller than (a)
# which brings back to case 1.

# Reapeating this procedure,
# at some point we'll reach the case (a)=(b)
# they could be the root of the tree, but not necessarly.
# In this case, the minimal path between (a) and (b)
# has been found. The algorithm stops 

# It is similar to the binary search algorithm.

def shortest_distance(a, b):
    if a == b:
        return 0
    else:
        steps_a = 0
        steps_b = 0
        
        while a != b:
            if a > b:
                a = a // 2
                steps_a += 1
            else:
                b = b // 2
                steps_b += 1
        
        return steps_a + steps_b

q = int(input())

for k in range(q):
    a, b = map(int, input().split())
    d = shortest_distance(a, b)
    print(d)
