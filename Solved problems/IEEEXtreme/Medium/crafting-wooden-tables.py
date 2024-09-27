# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/crafting-wooden-tables/

# Results: 100%

# solved by ilyes, October 24th, 2023
# Explanation below the code

def max_craft(C, N, P, W):
    if (C*N>=W or P<=C):
        return W//C
    else:
        k=0
        ava=N*P
        remn=W
        while (ava>remn):
            k+=1
            ava-=P
            remn-=C
        return k
    
C, N, P, W = map(int, input().split())
ans=max_craft(C, N, P, W)
print(ans)

# There are two cases:

# Case 1: W<=C*N or P<=C
# Base case W<=C*N means that
# we can place C pieces in each slot
# and there will be 0 or more free slots
# but it does not matter because each table
# is crafted by removing the C pieces freeing
# the slot, then the table can be placed
# on this same slot
# Base case P<=C means that we take pieces 
# from at least two slots to craft a table, 
# one of the two slots will be free so we can
# place the table in it and so on
# Then, we can craft all the pieces except
# the remaining pieces less than C
# That's why we take the quotient of W/C

# Case 2: W>=C*N and P>=C
# we try to distribute the wooden pieces
# by placing C pieces in each of the k slots
# such that the remaining pieces should be
# more than C in each of the remaining slots
# to complete filling the N-k slots with all the pieces
# illustration: 
# |S1|, |S2|, ..., |Sk|, | Sk+1 |, ..., | Sn |
# |C |, |C |, ..., |C |, |C+ak+1|, ..., |C+an|
# Where Si: ith slot
# ai>0 => slots Sk+1, ..., Sn have more than C pieces
# to find k, we use it as a counter and at each iteration
# we check if the available space >= remaining pieces
# If it is true, we can place C pieces on the (k+1)th slot
# we increment k and update the available space (ava-=P) 
# and the remaining pieces (remn-=C) for the next iteration
# we use a while loop and once it is terminated, the obtained 
# k is the maximum number of tables that can be crafted