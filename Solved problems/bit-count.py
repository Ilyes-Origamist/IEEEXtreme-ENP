# Problem
# https://csacademy.com/contest/interview-archive/task/bit-count/

# result: 100%

def bitcount(x:int):
    i=0
    if x==0:
        return 0
    elif x>0:
        while(x!=0):
            if x&1==1:
                i+=1
            x=x>>1
        return i
    else:
        x=abs(x)
        if x&1==1:
            k=1
        else:
            k=0
        while(x!=0):
            x=x>>1
            if x&1==1:
                i+=1
        i=32-i+k
        return i

x = int(input())
print(bitcount(x))
