# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/long_lines/

# Result: 40%
# Solved by tarek, IEEEXtreme 17.0

# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy


h=[]
n = get_number()
h.append(get_number())
a = get_number()
c =  get_number()
q = get_number()

for i in range(1,n):
    h.append((a*h[i-1]+c)%q)

#print(h)

count = 0
# The goal is to count how many people are noticeable
for i in range(n):
        for j in range(i + 1, n):
            if all(h[k] < h[i] for k in range(i+1, j)):
                count+= 1
            
        
print(count)