# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/mosaic1/

# Result: 100%
# Solved by ilyes, October 2023

n, cb, cp=map(int,input().split())
black=[]
black_tot=0
pink=[]
pink_tot=0
while len(black)!=n:
    bi, pi = map(int, input().split())
    black.append(bi)
    pink.append(pi)
    black_tot+=bi
    pink_tot+=pi

black_piles=(black_tot+9)//10
pink_piles=(pink_tot+9)//10
price=cb*black_piles+cp*pink_piles
print(price)