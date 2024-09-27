# Challenge Link
# https://csacademy.com/ieeextreme-practice/task/war_games/

# Result: 50%
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

Cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']

n = get_number()
for i in range(n):
    player1=list(input().split())
    player2=list(input().split())
    while True:
        if len(player1)==0:
            print("player 2")
            break
        elif len(player2)==0:
            print("player 1")
            break
        if player1==player2:
            print("draw")
            break
        p1=player1.pop(0)
        p2=player2.pop(0)
        v1=Cards.index(p1)
        v2=Cards.index(p2)
        if v1>v2:
            player1.append(p2)
        elif v2>v1:
            player2.append(p1)
        else:
            player1.append(p1)
            player2.append(p2)
        